from connection import connect

def update_contact(id, nom=None, cognom=None, email=None, telefon=None, direccio=None):
    connection = connect()
    if connection:
        cursor = connection.cursor()
        query = """
            UPDATE contactes
            SET nom = COALESCE(%s, nom),
                cognom = COALESCE(%s, cognom),
                email = COALESCE(%s, email),
                telefon = COALESCE(%s, telefon),
                direccio = COALESCE(%s,  direccio)
            WHERE id = %s;    
        """
        cursor.execute(query, (nom, cognom, email, telefon direccio, id))
        connection.commit()
        cursor.close()
        connection.close()
