"""Grocery server configuration."""

# Flask
from flask import Flask, request, jsonify

# DB connection
from backend import get_sql_connection

# Products data
from backend.products_dao import (
    get_all_products,
)

app = Flask(__name__)

conn = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_prodcuts():
    products = get_all_products(conn)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-origin', '*')
    return response

if __name__ == "__main__":
    print('Starting python Flask server for grocery store managment system')
    app.run(port=5000)