import json

from bbdd import *

def send_item(item,item_id):

    try:
        write_db(item, item_id)
        result = "Writed succesfully"
    except Exception as e:
        result = f"Error writing: {e}"
    return result

def get_items():
    items_list=[]
    items = read_db("ITEM")
    for item in items:
        item = item[0]
        items_list.append(item)

    items_json = json.dumps(items_list)
    return items_json

def delete_items(item_id):
    try:
        delete_from_db(item_id)
        result = "deleted succesfully"
    except Exception as e:
        result = f"Error deleting: {e}"
    return result