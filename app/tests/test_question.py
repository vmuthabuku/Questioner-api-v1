import unittest
from flask import json
import json
from datetime import datetime

from app import create_app

class Questioner(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.question_items = {'createdOn': str( datetime.now() ), 'createdBy':'James', 'meetup':'Android', 'title':'feels','body':'vevev evree rver','votes':'0' }

    def test_post_question(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/questions', data=json.dumps(self.question_items), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

