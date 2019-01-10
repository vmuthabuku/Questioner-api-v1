from datetime import datetime

class Question():
    """This is the question model"""
    def __init__(self, createdOn, createdBy, meetup, title, body, votes):
        """ This is the question model"""
        self.createdOn = str( datetime.now() )
        self.createdBy = createdBy
        self.meetup = meetup
        self.title = title
        self.body = body
        self.votes = votes

    def make_dict(self, item_id):
        """ making the question a dictionary """
        return dict(
            createdOn = self.createdOn,
            createdBy = self.createdBy,
            meetup = self.meetup,
            title = self.title,
            body = self.body,
            votes = self.votes,
            item_id = item_id
        )

