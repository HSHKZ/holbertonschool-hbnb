import unittest
from app import create_app

class TestHbnbApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
    
    def test_status(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "OK"})

if __name__ == "__main__":
    unittest.main()
