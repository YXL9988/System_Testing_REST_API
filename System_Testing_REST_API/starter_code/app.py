import os
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_restful import Api

from db import db
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister, UserLogin


class JWTError(Exception):
    pass


def create_app(jwt_secret_key=None, database_uri=None):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri or os.environ.get('DATABASE_URL', 'sqlite:///data.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'Lynn123'
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['JWT_SECRET_KEY'] = jwt_secret_key or os.environ.get('JWT_SECRET_KEY', 'your-jwt-secret-key')  # Change this!
    app.config['DEBUG']= True
    api = Api(app)
    jwt = JWTManager(app)

    @app.errorhandler(JWTError)
    def auth_error_handler(err):
        return jsonify({'message':'Could not authorize. Did you include a valid Authorization header?'}),401

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        print(f"user_lookup_loader: _jwt_header={_jwt_header}, jwt_data={jwt_data}")
        from models.user import UserModel
        identity = jwt_data["sub"]
        user = UserModel.find_by_id(identity)
        print(f"user_lookup_loader: returning user={user}")
        return user

    @jwt.user_identity_loader
    def user_identity_callback(user):
        print(f"user_identity_loader: user={user}")
        return user

    # Add resources to the API
    api.add_resource(Store, '/store/<string:name>')
    api.add_resource(ItemList, '/items')
    api.add_resource(StoreList, '/stores')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(Item, '/item/<string:name>')



    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
