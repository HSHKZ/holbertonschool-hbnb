# tests/test_amenity.py

import unittest
from app.api import create_app

class TestAmenityAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            'name': 'Wi-Fi'
        })
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['name'], 'Wi-Fi')

    def test_get_amenity(self):
        # Supposons qu'une commodité avec l'ID '1' existe
        response = self.client.get('/api/v1/amenities/1')
        self.assertEqual(response.status_code, 200)

    def test_update_amenity(self):
        # Supposons qu'une commodité avec l'ID '1' existe
        response = self.client.put('/api/v1/amenities/1', json={
            'name': 'Updated Amenity'
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Updated Amenity')
