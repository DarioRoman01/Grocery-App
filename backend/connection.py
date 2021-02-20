# db
import psycopg2

# Config
from backend import config

__conn = None

def get_sql_connection():
    print('Oppening postgresql connection...')
    global __conn

    if __conn is None:
        # read connection parameters
        params = config()

        # Connnect to the db
        __conn = psycopg2.connect(**params)

    return __conn