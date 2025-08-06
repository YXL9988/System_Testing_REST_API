from unittest import TestCase
from app import create_app
from db import db
from flask_jwt_extended import JWTManager

class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(jwt_secret_key='test-jwt-secret-key', database_uri='sqlite:///')
        cls.app.config['DEBUG'] = False
        cls.app.config['PROPAGATE_EXCEPTIONS'] = True
        JWTManager(cls.app)

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
