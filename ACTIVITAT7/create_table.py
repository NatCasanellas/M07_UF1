from connection import connect

def create_table():
    connection = connect()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contactes (
                id PRIMARY KEY,
                nom VARCHAR(50),                  
                cognom VARCHAR(50)
                email VARCHAR(50)
                telefon VARCHAR(15)
                direccio VARCHAR(100)                    
            );
        """)
        connection.commit()
        cursor.close()
        connection.close()