import unittest
from app import create_app, db
from app.models.user import User
from flask_jwt_extended import create_access_token

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        self.client = self.app.test_client()
        user = User(username='testuser')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_login_and_access_protected_route(self):
        # Test login
        response = self.client.post('/api/v1/login', json={
            'username': 'testuser',
            'password': 'password123'
        })
        data = response.get_json()
        self.assertIn('access_token', data)

        # Test access to protected route
        headers = {
            'Authorization': f"Bearer {data['access_token']}"
        }
        response = self.client.get('/api/v1/users/me', headers=headers)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
