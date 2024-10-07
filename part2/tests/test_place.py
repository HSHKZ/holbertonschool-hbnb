# tests/test_place.py

import unittest
from app.api import create_app

class TestPlaceAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_place(self):
        response = self.client.post('/api/v1/places/', json={
            'name': 'Cozy Cottage',
            'price': 120.50,
            'latitude': 48.8566,
            'longitude': 2.3522,
            'owner_id': '1234-abcd'  # Simulate valid owner ID
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Cozy Cottage')

    def test_get_place(self):
        # Supposons qu'une place avec l'ID '1' existe
        response = self.client.get('/api/v1/places/1')
        self.assertEqual(response.status_code, 200)

    def test_update_place(self):
        # Supposons qu'une place avec l'ID '1' existe
        response = self.client.put('/api/v1/places/1', json={
            'name': 'Updated Place'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Updated Place')
