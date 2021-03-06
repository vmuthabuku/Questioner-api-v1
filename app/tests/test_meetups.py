import unittest
from flask import json
import json
from datetime import datetime

from app import create_app

class Questioner(unittest.TestCase):
    """This class represents storemanger products posted test class"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.meetup_items = {"location":"west", "topic":"java", "happeningOn":"12-2-2","tags":"jam"}
        self.rsvp_items = {"meetupid":"1","status":"yes"}
        self.rsvp_items_no = {"meetupid":"1","status":"no"}
        self.rsvp_items_maybe = {"meetupid":"1","status":"maybe"}
        self.meetup_item = {"createdOn":"2019-01-16 01:25:17.491927","location":"west", "topic":"java", "happeningOn":"12-2-2","tags":"jam","meetupid":"1"}
        self.rsvp_wrong_status = {"meetupid":"1","status":"qww"}
        self.meetup_blank_item = {"location":"", "topic":"java", "happeningOn":"12-2-2","tags":"jam"}

    def test_post_item(self):
        """Testing posting a meetup."""

        response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_items), content_type='application/json')
        res = json.loads(response.data.decode())
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'],'Your item has been added successfully')


    def test_get_all_meetups(self):
        """getting all meetups"""
        response = self.client.get(
            '/api/v1/meetups/upcoming', data=json.dumps(self.meetup_items), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['data'], [])
    
    def test_blank_meetup(self):
        """ Handles testing blank objects in a meetup"""
        response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_blank_item), content_type='application/json')
        self.assertEqual(response.status_code, 400) 
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],'The location field cannot be empty')



    def test_get_meetup_wrong_id(self):
        """ getting a wrong meetup id"""
        response = self.client.get(
            '/api/v1/meetups/1', data=json.dumps(self.meetup_item), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'],'the id 1 does not exist')

    
    def test_rsvp(self):
        """ test rsvp a meetup"""
        response = self.client.post(
            '/api/v1/meetups/1/rsvps', data=json.dumps(self.rsvp_items), content_type='application/json')
        self.assertEqual(response.status_code, 201) 
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], {'status': 'yes'})
    
     
    def test_rsvp_no(self):
        """ test rsvp a meetup"""
        response = self.client.post(
            '/api/v1/meetups/1/rsvps', data=json.dumps(self.rsvp_items_no), content_type='application/json')
        self.assertEqual(response.status_code, 201) 
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], {'status': 'no'})

     
    def test_rsvp_maybe(self):
        """ test rsvp a meetup"""
        response = self.client.post(
            '/api/v1/meetups/1/rsvps', data=json.dumps(self.rsvp_items_maybe), content_type='application/json')
        self.assertEqual(response.status_code, 201) 
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['status'], {'status': 'maybe'})

    
    def test_rsvp_wrong_status(self):
        """ test rsvp with a wrong status"""
        response = self.client.post(
            '/api/v1/meetups/1/rsvps', data=json.dumps(self.rsvp_wrong_status), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(result['error'], 'The status qww is invalid, The status can either be yes, no or maybe')   


  

if __name__=='__main__':
    unittest.main()