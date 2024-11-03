import psycopg2
from psycopg2 import sql

#per saber quina es la database, el user i el password mirar el .yml
conn = psycopg2.connect(
    database="postgres",
    user='user_postgres',
    password='pass_postgres',
    host='localhost',
    port='5432'
)

#per fer la conexio s'utilitza el metode cursor()
connection = conn.cursor()

print(connection)