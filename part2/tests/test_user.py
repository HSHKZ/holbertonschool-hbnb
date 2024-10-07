# tests/test_user.py

import unittest
from app.api import create_app

class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['email'], 'test@example.com')

    def test_get_user(self):
        # Supposons qu'un utilisateur avec l'ID '1' existe
        response = self.client.get('/api/v1/users/1')
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        # Supposons qu'un utilisateur avec l'ID '1' existe
        response = self.client.put('/api/v1/users/1', json={
            'first_name': 'UpdatedName'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['first_name'], 'UpdatedName')
