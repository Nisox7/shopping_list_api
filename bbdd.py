import pymysql
from env import database_user,database_table,database_host,database_name,database_password

def connect():
    try:
        connection = pymysql.connect(host=database_host,
                                user=database_user,
                                password=database_password,
                                db=database_name)
        #print("Conexión correcta")
        cursor = connection.cursor()
        
        return connection, cursor

    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)

    

#--------------------------

def write_db(item, item_id):
    
    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]

    try:
        cursor.execute(f"INSERT INTO {database_table} VALUES ('{item_id}','{item}',DEFAULT)")
        connection.commit()
        #print("db written correctly")
        connection.close()
    except Exception as e:
        print(f"error writing db:\n{e}")

#--------------------------

def read_db(args):

    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]


    cursor.execute(f"SELECT {args} FROM {database_table}")
    read = cursor.fetchall()

    connection.close()

    return read

def delete_from_db(item_id):
    ddbb = connect()
    connection=ddbb[0]
    cursor=ddbb[1]

    try:
        cursor.execute(f"DELETE FROM {database_table} WHERE ITEM_ID='{item_id}'")
        connection.commit()
        #print("db written correctly")
        connection.close()
    except Exception as e:
        print(f"error deleting item on db:\n{e}")