from datetime import datetime

class Meetup():
    """This is the product model"""

    def __init__(self, createdOn, location, topic, happeningOn, tags):
        """This is the meetup model"""
        self.createdOn = str( datetime.now() )
        self.location = location
        self.topic = topic
        self.happeningOn = happeningOn
        self.tags = tags


    def make_dict(self, item_id):
        """receives the item as an object and turns it to a dict"""
        return dict(
            createdOn = self.createdOn,
            location = self.location,
            topic = self.topic,
            happeningOn = self.happeningOn,
            tags = self.tags,
            item_id = item_id
            
        )
class Rsvp():
    def __init__(self,status,topic):
        self.status = status
        self.topic = topic
    def make_dic(self):
        return dict (
            status = self.status,
            topic = self.topic
        )
        