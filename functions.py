from bbdd import *



def send_item_to_db(item,item_id,table):

    try:
        write_db(item, item_id, table)
        result = "Writed succesfully"
    except Exception as e:
        result = f"Error writing: {e}"
    return result



def get_items(table):
    items_list=[]
    items = read_db("ITEM", table)
    for item in items:
        item = item[0]
        items_list.append(item)

    return items_list



def delete_items(item_id, table):
    try:
        delete_from_db(item_id, table)
        result = "deleted succesfully"
    except Exception as e:
        result = f"Error deleting: {e}"
    return result




def get_tables():
    try:
        result = get_tables_from_db()
    except Exception as e:
        result = f"Error deleting: {e}"
    return result



def create_tables(table):
    try:
        create_table_db(table)
        result = f"Created table {table} succesfully"
    except Exception as e:
        result = f"Error writing: {e}"
    return result



def remove_tables(table):
    try:
        remove_table_from_db(table)
        result = "deleted succesfully"
    except Exception as e:
        result = f"Error deleting: {e}"
    return result