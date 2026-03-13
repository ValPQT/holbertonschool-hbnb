from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.services import facade
from app import bcrypt

api = Namespace('users', description='User operations')


user_model = api.model('User', {
    'first_name': fields.String(required=True),
    'last_name': fields.String(required=True),
    'email': fields.String(required=True),
    'password': fields.String(required=True)
})

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String(),
    'last_name': fields.String()
})


@api.route('/')
class UserList(Resource):

    @jwt_required()
    @api.expect(user_model, validate=True)
    @api.response(201, 'User created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'Password required')
    @api.response(403, 'Admin privileges required')
    def post(self):
        """Register a new user — admin only"""
        claims = get_jwt()

        if not claims.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403

        user_data = api.payload
        email = user_data.get('email')
        password = user_data.get('password')

        data = api.payload
        email = data.get('email')
        password = data.get('password')

        if not email:
            return {'error': 'Email required'}, 400
        if not password:
            return {'error': 'Password required'}, 400

        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400

        try:
            new_user = facade.create_user(data)
        except ValueError as e:
            return {'error': str(e)}, 400

        return {'id': new_user.id, 'message': 'User created successfully'}, 201

    @jwt_required()
    @api.response(200, 'List of users retrieved')
    def get(self):
        """Retrieve all users — admin only"""
        claims = get_jwt()
        if not claims.get('is_admin'):
            return {'error': 'Admin access required'}, 403

        users = facade.get_all_users()
        return [
            {'id': u.id, 'first_name': u.first_name,
             'last_name': u.last_name, 'email': u.email}
            for u in users
        ], 200


@api.route('/<user_id>')
class UserResource(Resource):

    @api.response(200, 'User retrieved')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email}, 200

    @jwt_required()
    @api.expect(user_update_model, validate=True)
    @api.response(200, 'User updated')
    @api.response(403, 'Unauthorized')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update user — own profile or admin"""
        current_user = get_jwt_identity()
        claims = get_jwt()
        is_admin = claims.get('is_admin', False)

        if current_user != user_id and not is_admin:
            return {'error': 'Unauthorized'}, 403

        user = facade.get_user_by_id(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = api.payload

        # Un user normal ne peut pas changer email/password
        if not is_admin:
            if 'email' in data or 'password' in data:
                return {'error': 'Unauthorized: cannot modify email or password'}, 403

        # Si admin change l'email, vérifier qu'il n'est pas déjà pris
        if is_admin and 'email' in data:
            existing_user = facade.get_user_by_email(data['email'])
            if existing_user and existing_user.id != user_id:
                return {'error': 'Email already in use'}, 400

        updated_user = facade.update_user(user_id, data)
        if not updated_user:
            return {'error': 'Invalid input data'}, 400

        return {
            'id': updated_user.id,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'email': updated_user.email
        }, 200
