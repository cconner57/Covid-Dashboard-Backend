from app import app
from unittest import TestCase
from flask import session
from models import db, User
import os

os.environ['DATABASE_URL'] = "postgresql:///covid-19-test"

db.create_all()

class FlaskTests(TestCase):
    def setUp(self):
        User.query.delete()

        db.session.commit()

        u = User(
            email="test@test.com",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test2@test.com",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.add(u2)
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        User.query.delete()

        db.session.commit()

    def test_repr(self):
        u = User.query.filter_by(username='testuser').one()

        self.assertEqual(repr(u), f'<User #{u.id}: {u.email}, {u.password}>')

    def test_signup(self):
        self.assertTrue(User.signup('test3@test.com', 'testpassword'))
        db.session.rollback()
        self.assertTrue(User.signup('test3@test.com', 'testpassword'))

    def test_authenticate(self):
        u1 = User.query.filter_by(username='testuser').one()

        self.assertFalse(User.authenticate('fakeuser', 'HASHED_PASSWORD'))