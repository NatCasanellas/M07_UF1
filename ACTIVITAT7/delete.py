from connection import connect

def delete_contact(id):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM contactes WHERE id = %s;", (id,))
        connection.commit()
        cursor.close()
        connection.close()