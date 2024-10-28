import unittest
from app import create_app
from app.config import TestingConfig

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.client = self.app.test_client()

    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertFalse(self.app.config['DEBUG'])

if __name__ == "__main__":
    unittest.main()
