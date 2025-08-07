from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json

class StoreTest(BaseTest):
    def test_create_store(self):
        resp = self.client.post('/store/test')

        self.assertEqual(resp.status_code, 201)
        self.assertIsNotNone(StoreModel.find_by_name('test'))
        self.assertDictEqual({'id':1,'name':'test','items':[]},json.loads(resp.data))

    def test_create_duplicate_store(self):
        self.client.post('/store/test')
        resp = self.client.post('/store/test')
        self.assertEqual(resp.status_code, 400)
        self.assertDictEqual({'message': "A store with name '{}' already exists.".format('test')}, json.loads(resp.data))

    def test_delete_store(self):
        StoreModel('test').save_to_db()
        resp = self.client.delete('/store/test')

        self.assertEqual(resp.status_code, 200)
        self.assertIsNone(StoreModel.find_by_name('test'))
        self.assertDictEqual({'message':'Store deleted'},json.loads(resp.data))


    def test_find_store(self):
        StoreModel('test').save_to_db()
        resp = self.client.get('/store/test')

        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'id':1,'name':'test','items':[]},json.loads(resp.data))

    def test_store_not_found(self):
        resp = self.client.get('/store/test')

        self.assertEqual(resp.status_code, 404)
        self.assertDictEqual({'message':'Store not found'}, json.loads(resp.data))

    def test_store_found_with_items(self):
        StoreModel('test').save_to_db()
        ItemModel('test',19.99,1).save_to_db()

        resp = self.client.get('/store/test')
        self.assertEqual(resp.status_code,200)
        self.assertDictEqual({'id':1,'name':'test','items':[{'name':'test','price':19.99,'store_id':1}]},json.loads(resp.data))

    def test_store_list(self):
        StoreModel('test').save_to_db()

        resp = self.client.get('/stores')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'stores':[{'id':1,'name':'test','items':[]}]}, json.loads(resp.data))

    def test_store_list_with_items(self):
        StoreModel('test').save_to_db()
        ItemModel('test', 19.99, 1).save_to_db()

        resp = self.client.get('/stores')
        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual({'stores': [{'id':1,'name': 'test', 'items': [{'name':'test','price':19.99,'store_id':1}]}]}, json.loads(resp.data))