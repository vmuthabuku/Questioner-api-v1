from datetime import datetime

class Question():
    """This is the question model"""
    def __init__(self, createdBy, title, body):
        self.createdBy = createdBy
        self.title = title
        self.body = body

    def make_dict(self, questionid):
        """ making the question a dictionary """
        return dict(
            createdOn =  str( datetime.now() ),
            createdBy = self.createdBy,
            title = self.title,
            body = self.body,
            upvote = 0,
            downvote = 0,
            questionid = questionid
        )
