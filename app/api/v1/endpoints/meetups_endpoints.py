from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.meetup_models import Meetup
from ..common import validator

app = Flask(__name__)

meetup_print = Blueprint("products", __name__)
api = Api(meetup_print, prefix="/api/v1")

meetups=[]

parser = reqparse.RequestParser()
parser.add_argument('createdOn', required=True, help="Name cannot be blank!")
parser.add_argument('location', type=str, required=True, help="price can only be an integer")
parser.add_argument('topic', type=str, required=True, help="quantity can only be an integer")
parser.add_argument('happeningOn', required=True, help="Description cannot be blank")
parser.add_argument('tags', required=True, help="tags cannot be blank")


class get_all(Resource):

    """"
    This class gets all questions and posts a question
    """

    def get(self):
        """This handles getting all products in a cart"""
        return {'data':meetups,
                'status':200}, 200

    def post(self):
        """This handles posting a product"""
        data = parser.parse_args()

        id_count = 1
        for meetup in meetups:
            id_count += 1

        new_item = Meetup(data['createdOn'], data['location'], data['topic'], data['happeningOn'],data['tags'])
        new_item_dict = new_item.make_dict(id_count)

        meetups.append(new_item_dict)
        return {'message': 'Your item has been added successfully',
                'data':new_item_dict,
                'status':201}, 201 

api.add_resource(get_all, "/meetups")