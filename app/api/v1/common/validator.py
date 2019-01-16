def check_using_id(list_name, other_id):
    """use the relevant id to find item"""

    my_item = next((item for item in list_name if item['questionid'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_id(list_name, other_id):
    """use the relevant id to find item"""

    my_item = next((item for item in list_name if item['meetupid'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_empty(s):
    if s.strip() == "":
        return "value cannot be empty"

def check_question_blank(l_name,createdBy,meetup,title,body):
    for item in l_name:
        if item['createdBy'].strip() == "":
            return "createdBy name cannot be empty"
        if item['meetup'].strip() == "":
            return "Meetup name cannot be empty"
        if item['title'].strip() == "":
            return "title name cannot be empty"
        if item['body'].strip() == "":
            return "body cannot be empty"

        

def check_question_duplicate(l_name,meetup,title):
    for item in l_name:
        if item["meetup"] == meetup:
            return "The meetup name is already in use try something else"
        if item["title"] == title:
               return "The title name is already in use try something else"

def check_meetup_duplicate(l_name,topic):
    for item in l_name:
         if item["topic"] == topic:
             return "The topic name is already in use"







