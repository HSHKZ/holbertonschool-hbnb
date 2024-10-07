# app/tests/test_review_api.py
import unittest
from app import create_app, db
from app.models.review_model import Review
from app.models.user_model import User
from app.models.place_model import Place

class TestReviewAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Ajouter un utilisateur et un lieu pour les tests
        self.user = User(username='testuser')
        self.place = Place(name='Test Place', description='A test place')
        db.session.add(self.user)
        db.session.add(self.place)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_review(self):
        response = self.client.post('/reviews', json={
            'user_id': self.user.id,
            'place_id': self.place.id,
            'text': 'Great place!'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('Great place!', response.data.decode())

    def test_create_review_empty_text(self):
        response = self.client.post('/reviews', json={
            'user_id': self.user.id,
            'place_id': self.place.id,
            'text': ''
        })
        self.assertEqual(response.status_code, 400)

    def test_get_review(self):
        review = Review(user_id=self.user.id, place_id=self.place.id, text='Nice place!')
        db.session.add(review)
        db.session.commit()

        response = self.client.get(f'/reviews/{review.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Nice place!', response.data.decode())

    def test_update_review(self):
        review = Review(user_id=self.user.id, place_id=self.place.id, text='Nice place!')
        db.session.add(review)
        db.session.commit()

        response = self.client.put(f'/reviews/{review.id}', json={'text': 'Updated review!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated review!', response.data.decode())

    def test_delete_review(self):
        review = Review(user_id=self.user.id, place_id=self.place.id, text='Delete me!')
        db.session.add(review)
        db.session.commit()

        response = self.client.delete(f'/reviews/{review.id}')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
