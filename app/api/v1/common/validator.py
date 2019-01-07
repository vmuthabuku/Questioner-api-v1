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


