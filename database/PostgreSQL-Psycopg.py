import psycopg2
from psycopg2 import OperationalError
conn = psycopg2.connect(
    host = "localhost",
    dbname = "postgres",
    user = "postgres",
    password = "root",
    port = "5432"
)
cur = conn.cursor()


#do smth
cur.execute(""" CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender Char
);
""")
cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'John', 25, 'M'),
(2, 'Jane', 30, 'F'),
(3, 'Bob', 40, 'M'),
(4, 'Engeline', 19, 'F'),
""")

conn.commit()


cur.close()
conn.close()