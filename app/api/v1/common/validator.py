def check_using_id(list_name, other_id):
    """use the relevant id to find item in a product carts list"""

    my_item = next((item for item in list_name if item[
                   'item_id'] == other_id), None)

    if my_item:
        return my_item
    return False

def check_empty(s):
    if s == '':
        return "cannot be blank"

def find_answers_to_a_question(list_name, question_id):
    """find all the answers posted to a question"""

    my_items = [element for element in list_name if element[
        'question_id'] == question_id]

    if my_items:
        return my_items
    return False

