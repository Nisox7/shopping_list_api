#!/usr/bin/python
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from functions import *

@app.route("/")
def main_page():
    x = ("Api status: Working!")
    return x



@app.route('/items', methods=['GET', 'POST'])
def return_items():

    data = request.get_json()['list']
    
    read_list = get_items(data)
    print(read_list)
    print(type(read_list))

    # Devolver una respuesta JSON
    return jsonify({'message': 'Received', 'elements': read_list})



@app.route('/send', methods=['GET', 'POST'])
def get_item():
    data = request.get_json()
    item = data['item']
    item_id = data['item_id']
    local_list = data['list']

    send_item_to_db(item,item_id,local_list)

    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})


@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    data = request.get_json()
    item_id = (data['item_id'])
    local_list = data['list']
    
    delete_items(item_id,local_list)
    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})



@app.route("/lists/list")
def return_lists():
    lists = get_tables()
    return lists



@app.route('/lists/create', methods=['GET', 'POST'])
def create_list():
    data = request.get_json()
    list_name = data['list']
    create_tables(list_name)
    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})



@app.route('/lists/delete', methods=['GET', 'POST'])
def remove_list():
    data = request.get_json()
    list_name = data['list']

    remove_tables(list_name)

    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10510)