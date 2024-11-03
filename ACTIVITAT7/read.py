from connection import connect

def read_contacts():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * from contactes;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        connection.close()    