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
        self.question_items = {'createdBy':'James', 'title':'feels','body':'vevev evree rver' }
        self.upvote_items = {'':''}
        self.question_blank = {'createdBy':'James', 'title':'','body':'no title' }
        self.question_blank_createdBy = {'createdBy':'', 'title':'ttrrtrt','body':'no title' }
    
    def test_post_question(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_items), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_upvote(self):
        """ Testing the upvote functionality"""
        response = self.client.patch(
            '/api/v1/questions/1/upvote', data=json.dumps(self.upvote_items), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_blank_question_created(self):
        """Testing posting a blank question."""
        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_blank_createdBy), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_blank_title(self):
        """Testing posting a blank question."""
        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_blank), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
    

    

    


    

