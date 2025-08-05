from models.user import UserModel
from tests.base_test import BaseTest
import json

class UserTest(BaseTest):
    def test_register_user(self):
        response = self.client.post('/register', json={'username': 'test', 'password': '1234'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(UserModel.find_by_username('test'))
        self.assertDictEqual({'message': 'User created successfully'}, json.loads(response.data))

    def test_register_and_login(self):
        self.client.post('/register', json={'username': 'test', 'password': '1234'})
        response = self.client.post('/login', json={'username': 'test', 'password': '1234'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', json.loads(response.data))

    def test_register_duplicate_user(self):
        self.client.post('/register', json={'username': 'test', 'password': '1234'})
        response = self.client.post('/register', json={'username': 'test', 'password': '1234'})
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual({'message': 'A user with that username already exists'}, json.loads(response.data))

    def test_login_non_existent_user(self):
        response = self.client.post('/login', json={'username': 'test', 'password': '1234'})
        self.assertEqual(response.status_code, 401)

    def test_login_wrong_password(self):
        self.client.post('/register', json={'username': 'test', 'password': '1234'})
        response = self.client.post('/login', json={'username': 'test', 'password': 'wrong_password'})
        self.assertEqual(response.status_code, 401)
