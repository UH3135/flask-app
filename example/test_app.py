import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import create_app, db

class UserCRUDTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
    
    
    def tearDown(self) -> None:
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


    def test_csrf_token(self):
        response = self.client.get('/csrf_token')
        self.assertEqual(response.status_code, 200)
        self.assertIn('csrf_token', response.get_json())

    
    def test_create_user_without_csrf(self):
        response = self.client.post('/user', json={"name": "Alice", 'password': 'qwerqwer9', "email": "alice@example.com"})
        self.assertEqual(response.status_code, 400)

    
    def test_create_user(self):
        response = self.client.get('/csrf_token')
        csrf_token = response.get_json()['csrf_token']

        response = self.client.post(
            "/user",
            json={"name": "Alice", 'password': 'qwerqwer9', "email": "alice@example.com"},
            headers={'X-CSRFToken': csrf_token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())
    
    
    def test_delete_user(self):
        response = self.client.get('/csrf_token')
        csrf_token = response.get_json()['csrf_token']

        self.client.post(
            '/user',
            json={"name": "Alice", 'password': 'qwerqwer9', "email": "alice@example.com"},
            headers={'X-CSRFToken': csrf_token}
        )
        response = self.client.delete(
            '/user',
            json={"name": "Alice"},
            headers={'X-CSRFToken': csrf_token}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('User deleted', response.get_json()['message'])
    

    def test_show_user(self):
        response = self.client.post('/user', json={"name": "Alice", 'password': 'qwerqwer9', "email": "alice@example.com"})
        response = self.client.get('/user')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()