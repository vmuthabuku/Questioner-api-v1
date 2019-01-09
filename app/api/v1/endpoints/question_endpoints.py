from flask import Flask, Blueprint, jsonify, make_response
from flask_restplus import Api,Resource,reqparse
from ..model.question_models import Question
from ..common import validator

app = Flask(__name__)

questions_print = Blueprint("question", __name__)
api = Api(questions_print, prefix="/api/v1")

questions=[]

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

api.add_resource(Questions, "/questions")
#api.add_resource(get_meetups, "/meetups/upcoming")
#api.add_resource(get_specific, "/meetups/<meetupid>/upvote")
