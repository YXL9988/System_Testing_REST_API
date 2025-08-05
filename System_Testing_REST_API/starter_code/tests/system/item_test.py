from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest
import json

class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        self.client.post('/register', json={'username': 'test', 'password': '1234'})
        auth_request = self.client.post('/login', json={'username': 'test', 'password': '1234'})
        auth_token = json.loads(auth_request.data)['access_token']
        self.auth_headers = {'Authorization': f'Bearer {auth_token}'}

    def test_get_item_no_auth(self):
        resp = self.client.get('/item/test')
        self.assertEqual(resp.status_code, 401)

    def test_get_item_not_found(self):
        resp = self.client.get('/item/test', headers=self.auth_headers)
        self.assertEqual(resp.status_code, 404)

    def test_get_item(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 19.99, 1).save_to_db()
        resp = self.client.get('/item/test', headers=self.auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'name': 'test', 'price': 19.99, 'store_id': 1}, json.loads(resp.data))

    def test_delete_item(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 19.99, 1).save_to_db()
        resp = self.client.delete('/item/test', headers=self.auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'message': 'Item deleted'}, json.loads(resp.data))

    def test_create_item(self):
        StoreModel('test').save_to_db()
        resp = self.client.post('/item/test',
                                json={'price': 17.99, 'store_id': 1},
                                headers=self.auth_headers)
        self.assertEqual(resp.status_code, 201)
        self.assertIsNotNone(ItemModel.find_by_name('test'))
        self.assertDictEqual({'name': 'test', 'price': 17.99, 'store_id': 1}, json.loads(resp.data))

    def test_create_duplicate_item(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 17.99, 1).save_to_db()
        resp = self.client.post('/item/test',
                                json={'price': 17.99, 'store_id': 1},
                                headers=self.auth_headers)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('already exists', json.loads(resp.data)['message'])

    def test_put_item_create(self):
        StoreModel('test').save_to_db()
        resp = self.client.put('/item/test',
                               json={'price': 17.99, 'store_id': 1},
                               headers=self.auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
        self.assertDictEqual({'name': 'test', 'price': 17.99, 'store_id': 1}, json.loads(resp.data))

    def test_put_update_item(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 5.99, 1).save_to_db()
        resp = self.client.put('/item/test',
                               json={'price': 17.99, 'store_id': 1},
                               headers=self.auth_headers)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
        self.assertDictEqual({'name': 'test', 'price': 17.99, 'store_id': 1}, json.loads(resp.data))

    def test_item_list(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 17.99, 1).save_to_db()
        resp = self.client.get('/items')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'items': [{'name': 'test', 'price': 17.99, 'store_id': 1}]}, json.loads(resp.data))