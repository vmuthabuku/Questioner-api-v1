def check_using_id(list_name, other_id):
    """use the relevant id to find question item"""

    my_item = next((item for item in list_name if item['questionid'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_id(list_name, other_id):
    """use the relevant id to find  meetup item"""

    my_item = next((item for item in list_name if item['meetupid'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_empty(s):
    """ it handles checking for an empty string """
    if s.strip() == "":
        return "value cannot be empty"
        

def check_question_duplicate(l_name,title):
    """ it checks if the question has been duplicated"""
    for item in l_name:
        if item["title"] == title:
               return "The title name is already in use try something else"

def check_meetup_duplicate(l_name,topic):
    """ check if a meetup has a duplicate"""
    for item in l_name:
         if item["topic"] == topic:
             return "The topic name is already in use"







