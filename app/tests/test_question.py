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
        self.downvote_items = {'':''}
        self.question_blank = {'createdBy':'James', 'title':'','body':'no title' }
        self.question_blank_createdBy = {'createdBy':'', 'title':'ttrrtrt','body':'no title' }
        self.question_blank_body = {'createdBy':'qww', 'title':'ttrrtrt','body':'' }
    
    def test_post_question(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_items), content_type='application/json')
        res = json.loads(response.data.decode())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'],'Your item has been added successfully')


    def test_upvote(self):
        """ Testing the upvote functionality"""
        response = self.client.patch(
            '/api/v1/questions/1/upvote', data=json.dumps(self.upvote_items), content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['upvote'],1)


    def test_post_blank_question_created(self):
        """Testing posting a blank question."""
        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_blank_createdBy), content_type='application/json')
        res = json.loads(response.data.decode())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['error'],'The createdBy field cannot be empty')
    
    
    def test_post_blank_title(self):
        """Testing posting a blank question."""
        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_blank), content_type='application/json')
        res = json.loads(response.data.decode())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['error'],'The title field cannot be empty')
    
    def test_post_blank_body(self):
        """Testing posting a blank body"""
        response = self.client.post(
            '/api/v1/meetups/1/questions', data=json.dumps(self.question_blank_body), content_type='application/json')
        res = json.loads(response.data.decode())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['error'],'The body field cannot be empty')