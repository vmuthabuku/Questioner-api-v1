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
        self.meetup_items = {'createdOn': str( datetime.now() ), "location":"west", "topic":"java", "happeningOn":"12-2-2","tags":"jam"}


    def test_post_item(self):
        """Testing posting product description."""

        response = self.client.post(
            '/api/v1/meetups', data=json.dumps(self.meetup_items), content_type='application/json')
        res = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)

    

  

if __name__=='__main__':
    unittest.main()