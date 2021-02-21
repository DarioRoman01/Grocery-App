"""Grocery server configuration."""

# Flask
from flask import Flask, request, jsonify

# json
import json

# DB connection
from backend import get_sql_connection

# Products data
from backend import (
    get_all_products,
    delete_product,
    get_uoms,
    insert_new_product,
    update_product,
    insert_order,
    get_all_orders
)

app = Flask(__name__)

conn = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_prodcuts():
    products = get_all_products(conn)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/deleteProduct', methods=['POST'])
def remove_product():
    return_id = delete_product(conn, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/getUOM', methods=['GET'])
def retrieve_uoms():
    uoms = get_uoms(conn)
    response = jsonify(uoms)
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def add_product():
    request_payload = json.loads(request.form['data'])
    product_id = insert_new_product(conn, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/updateProduct', methods=['POST'])
def update_products():
    product_id = request.form['product_id']
    col = request.form['column']
    val = request.form['value']
    return_id = update_product(conn, col, val, product_id)
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_orders():
    orders = get_all_orders(conn)
    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

@app.route('/insertOrder', methods=['POST'])
def create_order():
    request_payload = json.loads(request.form['data'])
    order_id = insert_order(conn, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-origin', '*')
    return response


if __name__ == "__main__":
    print('Starting python Flask server for grocery store managment system')
    app.run(port=5000)