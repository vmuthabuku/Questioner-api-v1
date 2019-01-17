from flask import Flask, Blueprint, jsonify, make_response, request
from flask_restplus import Api,Resource,reqparse
from ..model.question_models import Question
from ..utils import validator
from .meetups_endpoints import get_specific, meetups

app = Flask(__name__)

questions_print = Blueprint("question", __name__)
api = Api(questions_print, prefix="/api/v1")

questions=[]

parser = reqparse.RequestParser()
parser.add_argument('createdBy', type=str, required=True, help="createdBy cannot be empty")
parser.add_argument('title', required=True, help="title cannot be blank")
parser.add_argument('body', required=True, help="body cannot be blank")

class Questions(Resource):

    """"
    This class gets all questions and posts a question

    """
    def get(self):
        """get all questions"""
        return{"questions":questions}

    def post(self,id):
        """This handles posting a question"""
        data = parser.parse_args()
        createdBy = data.get('createdBy')
        title = data.get('title')
        body = data.get('body')

        try:
            type(int(id)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400
       
        

        for item in (data['createdBy'],data['title'],data['body']):            
            if validator.check_empty(item):
                for index in data:
                    if data[index] == item:
                        return{'error':'The {} field cannot be empty'.format(index),
                                'status':400},400
        new_meetup = get_specific.duplicate(id)
        if new_meetup:       
        
            validate = validator.check_question_duplicate(questions,data['title'])
            if validate:
                return {"message": validate,
                        'status':409}, 409                 

            id_count = 1
            for question in questions:
                id_count += 1

            new_item = Question(data['createdBy'], data['title'],data['body'])
            new_item_dict = new_item.make_dict(id_count)

            questions.append(new_item_dict)
            return {'message': 'Your item has been added successfully',
                    'data':new_item_dict,
                    'status':201,
                    'meetup':id
                    }, 201 
        return {"error":"the id {} does not exist".format(id),
                'status':404}, 404

class UpVote(Resource):
    """This handles upvoting a specific question"""
    @classmethod
    def get(cls, questionid):
        """This handles getting a specific question"""
        try:
            type(int(questionid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400  
        check_id = validator.check_using_id(questions,int(questionid))
        if check_id:
            return check_id, 200
        return {'error':'the id {} does not exist'.format(questionid),
                'status':400}, 400         

    
    @classmethod
    def patch(self,questionid):
        try:
            type(int(questionid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400  
        check_id = validator.check_using_id(questions,int(questionid))
        if not check_id:
            return {'error':'the id {} does not exist'.format(questionid),
                    'status':400}, 400   
        q_db = questions[0]['upvote']+1
        questions[0]['upvote'] = q_db  
        data = [{
           'meetup':questionid,
           'topic':questions[0]['title'],
           'downvote':questions[0]['downvote']
        }]  
        return{'values':data,
               'upvote':questions[0]['upvote'],
               'status': 200,
               }, 200


class DownVote(Resource):
    """This handles downvoting a specific question"""

    @classmethod
    def patch(self,questionid):
        try:
            type(int(questionid)) == int
        except Exception as e:
            return{"error":"status code can only be an integer",
                    'status':400}, 400  
        check_id = validator.check_using_id(questions,int(questionid))
        if not check_id:
            return {'error':'the id {} does not exist'.format(questionid),
                    'status':400}, 400 
        q_db = questions[0]['downvote']+1
        questions[0]['downvote'] = q_db    
        data = [{
            'meetup':questionid,
            'topic':questions[0]['title'],
            'upvote':questions[0]['upvote'],
        }]  
        return{

            'values':data,
            'downvote':questions[0]['downvote'],                
            'status':200}, 200
        

                
api.add_resource(Questions, "/meetups/<id>/questions")
api.add_resource(UpVote, "/questions/<questionid>/upvote")
api.add_resource(UpVote, "/questions/<questionid>")
api.add_resource(DownVote, "/questions/<questionid>/downvote")
