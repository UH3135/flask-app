import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import create_app, db

class UserCRUDTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.app.debug = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    
    
    def tearDown(self) -> None:
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    
    def test_create_user(self):
        response = self.client.post('/user', json={"name": "Alice", "email": "alice@example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())
    
    
    def test_delete_user(self):
        self.client.post('/user', json={"name": "Alice", "email": "alice@example.com"})
        response = self.client.delete('/user', json={"name": "Alice"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('User deleted', response.get_json()['message'])
    

    def test_show_user(self):
        response = self.client.post('/user', json={"name": "Alice", "email": "alice@example.com"})
        response = self.client.get('/user')
        self.assertEqual(response.status_code, 200)
        # self.assertIn('id', response.get_json())



if __name__ == "__main__":
    unittest.main()