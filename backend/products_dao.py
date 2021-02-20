"""Products data access."""

# DB
import psycopg2

# Config
from backend import get_sql_connection


def get_all_products(conn):
    """return all the products."""

    # create cursor
    cursor = conn.cursor()

    # execute query
    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
            "FROM products INNER JOIN uom on products.uom_id = uom.uom_id")

    cursor.execute(query)

    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

def insert_new_product(conn, product):
    """Insert a product in the db."""

    cursor = conn.cursor()

    # execute query
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    query = ("insert into products"
            "(name, uom_id, price_per_unit)"
            "values(%s, %s, %s);")

    cursor.execute(query, data)

    # save changes
    conn.commit()

    return cursor.lastrowid

def delete_product(conn, product_id):
    """Delete the specified product."""
    cursor = conn.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    conn.commit()

def update_product(conn, column, val, product_id):
    """Update the product with the specified column and value.""" 
    cursor = conn.cursor()
    query = (f'UPDATE products SET {column} = {val} WHERE product_id = {product_id}')
    cursor.execute(query)
    conn.commit()


if __name__ == "__main__":
    # conn =  get_sql_connection()
    # print(get_all_products(conn))
    # print(delete_product(conn, 13))
    print('owo')