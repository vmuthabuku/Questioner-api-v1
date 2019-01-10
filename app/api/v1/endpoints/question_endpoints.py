from flask import Flask, Blueprint, jsonify, make_response, request
from flask_restplus import Api,Resource,reqparse
from ..model.question_models import Question, Votes, DownVote
from ..common import validator

app = Flask(__name__)

questions_print = Blueprint("question", __name__)
api = Api(questions_print, prefix="/api/v1")

questions=[]
votes = []

parser = reqparse.RequestParser()
parser.add_argument('createdOn', required=True, help="createdOn cannot be blank!")
parser.add_argument('createdBy', type=str, required=True, help="createdBy can only be an integer")
parser.add_argument('meetup', type=str, required=True, help="meetup can only be an integer")
parser.add_argument('title', required=True, help="title cannot be blank")
parser.add_argument('body', required=True, help="body cannot be blank")
parser.add_argument('votes', required=True, help="votes cannot be blank")


class Questions(Resource):

    """"
    This class gets all questions and posts a question
    """

    def post(self):
        """This handles posting a meetup"""
        data = parser.parse_args()

        id_count = 1
        for question in questions:
            id_count += 1

        new_item = Question(data['createdOn'], data['createdBy'], data['meetup'], data['title'],data['body'],data['votes'])
        new_item_dict = new_item.make_dict(id_count)

        questions.append(new_item_dict)
        return {'message': 'Your item has been added successfully',
                'data':new_item_dict,
                'status':201}, 201 

class GetSpecific(Resource):
    """Get a specific question"""
    parser = reqparse.RequestParser()
    parser.add_argument('upvote', required=True, help="votes cannot be blank!")
    
    @classmethod
    def get(cls, questionid):
        check_id = validator.check_using_id(questions,int(questionid))
        if check_id:
            return check_id, 200
        return {'message':'no such id'}
    @classmethod
    def patch(self,questionid):
        data = GetSpecific.parser.parse_args()
        new = Votes(data['upvote'])
        new_item = new.make_dictionary()
        return{"votes":new_item,
               'questionid':questionid}

        

                
api.add_resource(Questions, "/questions")
api.add_resource(GetSpecific, "/questions/<questionid>/upvote")
#api.add_resource(GetSpecific, "/questions/<questionid>/downvote")
