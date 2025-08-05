from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt_extended import create_access_token
from security import authenticate


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()
        print(f"User {user.username} saved to DB.")

        return {'message': 'User created successfully'}, 201


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self):
        data = self.parser.parse_args()
        user = authenticate(data['username'], data['password'])

        if not user:
            return {"message": "Invalid credentials"}, 401

        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}, 200