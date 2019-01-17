from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.meetup_models import Meetup, Rsvp
from ..utils import validator

app = Flask(__name__)

meetup_print = Blueprint("products", __name__)
api = Api(meetup_print, prefix="/api/v1")

meetups=[]
rsvp=[]

parser = reqparse.RequestParser()
parser.add_argument('location', type=str, required=True, help="location cannot be blank")
parser.add_argument('topic', type=str, required=True, help="topic cannot be blank")
parser.add_argument('happeningOn', required=True, help="happening on cannot be blank")
parser.add_argument('tags', required=True, help="tags cannot be blank")

class get_meetups(Resource):
    """This handles getting all available meetups"""
    def get(self):
        return {'data':meetups,
                'status':200}, 200    


class get_all(Resource):

    """"
    This handles posting a new meetup
    """

    def post(self):
        """This handles posting a meetup"""
        data = parser.parse_args()
        location = data.get('location')
        topic = data.get('topic')
        happeningOn = data.get('happeningOn')
        tags = data.get('tags')

        for item in (data['location'],data['topic'],data['happeningOn'],data['tags']):            
            if validator.check_empty(item):
                 for index in data:
                        if data[index] == item:
                            return{'error':'The {} field cannot be empty'.format(index)},400
        
        validate = validator.check_meetup_duplicate(meetups, data['topic'])
        if validate:
               return {"message": validate}, 409
           

        id_count = 1
        for meetup in meetups:
            id_count += 1

        new_item = Meetup(data['location'], data['topic'], data['happeningOn'],data['tags'])
        new_item_dict = new_item.make_dict(id_count)
        meetups.append(new_item_dict)
        return {'message': 'Your item has been added successfully',
                'data':new_item_dict,
                'status':201}, 201 
        
class get_specific(Resource):
    """Get a specific meetup"""
    @classmethod
    def get(cls, meetupid):
        try:
            type(int(meetupid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400
        check_id = validator.check_id(meetups,int(meetupid))
        if check_id:
            return check_id, 200
        return {'error':'the id {} does not exist'.format(meetupid)}, 404

    @classmethod
    def duplicate(cls, meetupid):
        try:
            type(int(meetupid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400
        check_id = validator.check_id(meetups,int(meetupid))
        if check_id:
            return {'error':'the id {} does not exist'.format(meetupid)}, 404

class Rsv(Resource):
    """This handles to rsvp for a specific meetup"""
    parser = reqparse.RequestParser()
    parser.add_argument('status',required=True, help="status cannot be empty")
    def post(self,meetupid):
        data = Rsv.parser.parse_args()
        status = data.get('status')

        if validator.check_empty(data['status']):
             for index in data:
                        if data[index] == data['status']:
                            return{'error':'The {} field cannot be empty'.format(index)},400
        
        try:
            type(int(meetupid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400    

        check_id = validator.check_id(meetups,int(meetupid))
        if not check_id:
            return {'error':'the id {} does not exist'.format(meetupid)}, 404
        if status == "yes" or status == "no" or status ==  "maybe":
            new = Rsvp(data['status'])
            new_item = new.make_dic()
            rsvp.append(new_item)
            return{'status':new_item,
                'meetupid':meetupid},201
        return {"error":"The status {} is invalid, The status can either be yes, no or maybe".format(status)}, 400            

        

api.add_resource(get_all, "/meetups")
api.add_resource(get_meetups, "/meetups/upcoming")
api.add_resource(get_specific, "/meetups/<meetupid>")
api.add_resource(Rsv, "/meetups/<meetupid>/rsvps")
