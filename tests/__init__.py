from unittest import TestCase
from app import app


class TestBaseClass(TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
