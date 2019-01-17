from datetime import datetime

class Meetup():
    """This is the meetup model"""

    def __init__(self, location, topic, happeningOn, tags ):
        self.location = location
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags


    def make_dict(self, meetupid):
        """receives the item as an object and turns it to a dict"""
        return dict(
            createdOn = str( datetime.now() ),
            location = self.location,
            topic = self.topic,
            happeningOn = self.happeningOn,
            tags = self.tags,
            meetupid = meetupid
            
        )
class Rsvp():
    """This is the rsvp model"""
    def __init__(self,status):
        self.status = status
    def make_dic(self):
        """receives the item as an object and turns it to a dict"""
        return dict (
            status = self.status
            
        )
        