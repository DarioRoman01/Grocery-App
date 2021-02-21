"""Orders data accsess."""

# db
import psycopg2

# utlils
from datetime import datetime

now = datetime.now()

def insert_order(conn, order):
    cursor = conn.cursor()

    # create order
    order_data = (order['customer_name'], order['total'], now)

    order_query = ("insert into orders"
                   "(customer_name, total, datetime)"
                   "values(%s, %s, %s);")

    cursor.execute(order_query, order_data)

    # get id of the order
    get_oder_id = ('select * from orders order by order_id desc limit 1')
    cursor.execute(get_oder_id)

    id_ = []
    for (oder_id, customer_name, total, datetime) in cursor:
        id_.append(oder_id)
    order_id = id_[0]

    # create order_detail
    order_detail_query = ("INSERT INTO order_details" 
                          "(order_id, product_id, quantity, total_price)"
                          "VALUES (%s, %s, %s, %s)")

    order_detail_data = []
    for order_detail_record in order['order_details']:
        order_detail_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price']),
        ])

    cursor.executemany(order_detail_query, order_detail_data)

    conn.commit()

    return order_id



def get_all_orders(conn):
    cursor = conn.cursor()

    query = ('SELECT * FROM orders')

    cursor.execute(query)

    response = []

    for (oder_id, customer_name, total, datetime) in cursor:
        response.append({
            'order_id': oder_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': datetime
        })

    return response

if __name__ == "__main__":
    print('lo que sea')