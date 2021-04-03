import mysql.connector
from mysql.connector import Error

def connect():
    """ Connection to MYSQL DB"""

    conn = None
    database_name = "xxx"
    try:
        conn = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="xxx",
                                       database=database_name)
        if conn.is_connected():
            print('Connected to MYSQL DB')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    connect()
