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

@app.route("/items")
def return_items():
    items = get_items()
    return items


@app.route('/send', methods=['GET', 'POST'])
def get_item():
    data = request.get_json()
    item = data['item']
    item_id = data['item_id']

    send_item(item,item_id)

    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})


@app.route('/delete', methods=['GET', 'POST'])
def delete_item():
    data = request.get_json()
    item_id = (data['item_id'])
    
    delete_items(item_id)
    # Devolver una respuesta JSON
    return jsonify({'message': 'Received'})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10510)