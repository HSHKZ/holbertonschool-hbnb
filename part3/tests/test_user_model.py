import unittest
from app import create_app, db
from app.models.user import User

class UserModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        user = User(username='testuser')
        user.set_password('password123')
        self.assertNotEqual(user.password_hash, 'password123')
        self.assertTrue(user.check_password('password123'))

if __name__ == "__main__":
    unittest.main()
