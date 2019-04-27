from unittest import TestCase
from app import app


class TestBaseClass(TestCase):

    def setUp(self):
        self.client = app.test_client()
