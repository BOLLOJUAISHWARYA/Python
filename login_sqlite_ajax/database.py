import sqlite3

conn = sqlite3.connect('database.db')
print('opened')
conn.execute(""" CREATE TABLE details(id int UNIQUE ,name VARCHAR(255) ,city CHAR(25) ,pin varchar(255),password varchar(255))""")
print('Table created')
conn.close()
