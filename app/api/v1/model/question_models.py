from datetime import datetime

class Question():
    """This is the question model"""
    def __init__(self, createdBy, meetup, title, body):
        self.createdBy = createdBy
        self.meetup = meetup
        self.title = title
        self.body = body

    def make_dict(self, item_id):
        """ making the question a dictionary """
        return dict(
            createdOn =  str( datetime.now() ),
            createdBy = self.createdBy,
            meetup = self.meetup,
            title = self.title,
            body = self.body,
            upvote = 0,
            downvote = 0,
            item_id = item_id
        )
