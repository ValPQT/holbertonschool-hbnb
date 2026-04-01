from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade

api = Namespace('reviews', description='Review operations')


review_input_model = api.model('ReviewInput', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True),
    'place_id': fields.String(required=True)
})

review_update_model = api.model('ReviewUpdate', {
    'text': fields.String(required=True),
    'rating': fields.Integer(required=True)
})


@api.route('/')
class ReviewList(Resource):

    @api.response(200, 'Reviews retrieved successfully')
    def get(self):
        """Get all reviews"""

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


    @jwt_required()
    @api.expect(review_input_model, validate=True)
    @api.response(201, 'Review created')
    def post(self):
        """Create a review"""

        current_user = get_jwt_identity()
        data = api.payload

        place = facade.get_place(data["place_id"])
        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == current_user:
            return {"error": "You cannot review your own place"}, 403

        existing_reviews = facade.get_reviews_by_place(data["place_id"])

        for review in existing_reviews:
            if review.user.id == current_user:
                return {"error": "You already reviewed this place"}, 400

        data["user_id"] = current_user

        new_review = facade.create_review(data)

        return {
            "id": new_review.id,
            "text": new_review.text,
            "rating": new_review.rating,
            "user_id": new_review.user.id,
            "place_id": new_review.place.id
        }, 201


@api.route('/<review_id>')
class ReviewResource(Resource):

    @api.response(200, 'Review retrieved')
    @api.response(404, 'Review not found')
    def get(self, review_id):
        """Get review by id"""

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
    @api.response(200, 'Review updated')
    @api.response(403, 'Unauthorized')
    def put(self, review_id):
        """Update review"""

        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404

        if review.user.id != current_user and not is_admin:
            return {"error": "Unauthorized"}, 403

        facade.update_review(review_id, api.payload)

        return {"message": "Review updated successfully"}, 200


    @jwt_required()
    @api.response(200, 'Review deleted')
    def delete(self, review_id):
        """Delete review"""

        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get("is_admin", False)

        review = facade.get_review(review_id)

        if not review:
            return {"error": "Review not found"}, 404

        if review.user.id != current_user and not is_admin:
            return {"error": "Unauthorized"}, 403

        facade.delete_review(review_id)

        return {"message": "Review deleted successfully"}, 200
