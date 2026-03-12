from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace('reviews', description='Review operations')

review_input_model = api.model('ReviewInput', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating of the place (1-5)'),
    'place_id': fields.String(required=True, description='ID of the place')
    # user_id retiré — on le récupère depuis le token
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(required=True, description='Text of the review'),
    'rating': fields.Integer(required=True, description='Rating (1-5)'),
})


@api.route('/')
class RegisterReview(Resource):

    @jwt_required()
    @api.expect(review_input_model, validate=True)
    @api.response(201, 'Review successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new review"""
        current_user_id = get_jwt_identity()
        review_data = api.payload

        # user_id forcé à l'utilisateur connecté
        review_data['user_id'] = current_user_id

        try:
            new_review = facade.create_review(review_data)
        except ValueError as e:
            return {"error": str(e)}, 400

        return {
            'id': new_review.id,
            'text': new_review.text,
            'rating': new_review.rating,
            'user_id': new_review.user.id,
            'place_id': new_review.place.id
        }, 201

    @api.response(200, 'List of reviews retrieved successfully')
    def get(self):
        """Retrieve a list of all reviews — public"""
        reviews = facade.get_all_reviews() or []
        return [
            {
                "id": r.id,
                "text": r.text,
                "rating": r.rating,
                "user_id": r.user.id,
                "place_id": r.place.id
            }
            for r in reviews
        ], 200


@api.route('/<review_id>')
class ReviewIDResource(Resource):

    @api.response(200, 'Review details retrieved successfully')
    @api.response(404, 'Review not found')
    @jwt_required()
    def get(self, review_id):
        """Get review details by ID — public"""
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user.id,
            "place_id": review.place.id
        }, 200

    @jwt_required()
    @api.expect(review_update_model, validate=True)
    @api.response(200, 'Review updated successfully')
    @api.response(403, 'Unauthorized')
    @api.response(404, 'Review not found')
    def put(self, review_id):
        """Update a review — author or admin only"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin')

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        # Seul l'auteur ou un admin peut modifier
        if review.user.id != current_user_id and not is_admin:
            return {"error": "Unauthorized"}, 403

        try:
            updated = facade.update_review(review_id, api.payload)
        except ValueError as e:
            return {"error": str(e)}, 400

        return {"message": "Review updated successfully"}, 200

    @jwt_required()
    @api.response(200, 'Review deleted successfully')
    @api.response(403, 'Unauthorized')
    @api.response(404, 'Review not found')
    def delete(self, review_id):
        """Delete a review — author or admin only"""
        current_user_id = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin')

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        return {"message": "Review deleted successfully"}, 200


@api.route('/reviews')
class ReviewList(Resource):
    @api.expect(review_update_model, validate=True)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Create a new review"""
        current_user = int(get_jwt_identity())
        review_data = api.payload

        place_id = review_data.get("place_id")
        text = review_data.get("text")
        rating = review_data.get("rating")

        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == current_user:
            return {"error": "You cannot review your own place"}, 403

        existing_reviews = facade.get_reviews_by_place(place_id)

        for review in existing_reviews:
            if review.user_id == current_user:
                return {"error": "You already reviewed this place"}, 400

        review_data["user_id"] = current_user
        new_review = facade.create_review(review_data)

        return {
            "id": new_review.id,
            "text": new_review.text,
            "rating": new_review.rating,
            "user_id": new_review.user.id,
            "place_id": new_review.place.id
        }, 201


@api.route('/reviews/<review_id>')
class ReviewResource(Resource):

    @api.expect(review_update_model, validate=True)
    @api.response(200, 'Review updated successfully')
    @api.response(404, 'Review not found')
    @api.response(403, 'Unauthorized action')
    @api.response(204, 'Review deleted successfully')
    @jwt_required()
    def put(self, review_id):
        """Update a review"""
        current_user = int(get_jwt_identity())

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        if review.user_id != current_user:
            return {"error": "Unauthorized action"}, 403

        review_data = api.payload

        facade.update_review(review_id, review_data)

        updated_review = facade.update_review(review_id, review_data)

        return {
            "id": review.id,
            "text": review.text,
            "rating": review.rating,
            "user_id": review.user_id,
            "place_id": review.place_id
        }, 200

    def delete(self, review_id):

        current_user = int(get_jwt_identity())

        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404

        if review.user_id != current_user:
            return {"error": "Unauthorized action"}, 403

        success = facade.delete_review(review_id)
        if not success:
            return {"error": "Failed to delete review"}, 500

        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200
