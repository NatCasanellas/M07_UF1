from connection import connection

def create_contact(nom, cognom, email, telefon, direccio):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO contactes (nom, cognom, email, telefon, direccio)
            VALUES (%s, %s, %s, %s, %s, %s);
        """, (nom, cognom, email, telefon, direccio))
        connection.commit()
        cursor.close()
        connection.close()