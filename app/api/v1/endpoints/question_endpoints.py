from flask import Flask, Blueprint, jsonify, make_response, request
from flask_restplus import Api,Resource,reqparse
from ..model.question_models import Question
from ..common import validator
from .meetups_endpoints import meetups

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

    def post(self):
        """This handles posting a question"""
        data = parser.parse_args()
        createdBy = data.get('createdBy')
        title = data.get('title')
        body = data.get('body')

        for item in (data['createdBy'],data['title'],data['body']):            
            if validator.check_empty(item):
                return{'error':'cannot be empty {}'.format(item)},400
            
        
        validate = validator.check_question_duplicate(questions,data['title'])
        if validate:
            return {"message": validate}, 409

        #m_id = meetups[0]['meetupid']                               

        id_count = 1
        for question in questions:
            id_count += 1

        new_item = Question(data['createdBy'], data['title'],data['body'])
        new_item_dict = new_item.make_dict(id_count)

        questions.append(new_item_dict)
        return {'message': 'Your item has been added successfully',
                'data':new_item_dict,
                'status':201}, 201 

class UpVote(Resource):
    """This handles upvoting a specific question"""
    @classmethod
    def get(cls, questionid):
        """This handles getting a specific question"""
        check_id = validator.check_using_id(questions,int(questionid))
        if check_id:
            return check_id, 200
        return {'error':'the id {} does not exist'.format(questionid)}, 400         

    
    @classmethod
    def patch(self,questionid):
        check_id = validator.check_using_id(questions,int(questionid))
        if not check_id:
            return {'error':'the id {} does not exist'.format(questionid)}, 400   
        q_db = questions[0]['upvote']+1
        questions[0]['upvote'] = q_db      
        return{"upvote":questions[0]['upvote'],
               'questionid':questionid}, 200

    

class DownVote(Resource):
    """This handles downvoting a specific question"""

    @classmethod
    def patch(self,questionid):
        check_id = validator.check_using_id(questions,int(questionid))
        if not check_id:
            return {'error':'the id {} does not exist'.format(questionid)}, 400   
        q_db = questions[0]['downvote']+1
        questions[0]['downvote'] = q_db      
        return{"downvote":questions[0]['downvote'],
               'questionid':questionid}, 200
        

                
api.add_resource(Questions, "/questions")
api.add_resource(UpVote, "/questions/<questionid>/upvote")
api.add_resource(UpVote, "/questions/<questionid>")
api.add_resource(DownVote, "/questions/<questionid>/downvote")
