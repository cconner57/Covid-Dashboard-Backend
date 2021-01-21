from app import app
from unittest import TestCase
from flask import session
from models import db, User
import os

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

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
        app.config['TESTING'] = True
