"""uoms data access."""

#db
import psycopg2

def get_uoms(conn):
    """Get all the uoms."""

    cursor = conn.cursor()
    query = ('SELECT * FROM uom')
    cursor.execute(query)

    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    
    return response

if __name__ == "__main__":
    print('lo que sea')




