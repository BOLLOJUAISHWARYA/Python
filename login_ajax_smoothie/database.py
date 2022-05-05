import sqlite3

conn = sqlite3.connect('database.db')
print('opened')
conn.execute(""" CREATE TABLE details(id integer primary key autoincrement ,name VARCHAR(255),username VARCHAR(255) NOT NULL UNIQUE  ,city CHAR(25) ,pin varchar(255),password varchar(255) NOT NULL )""")
print('Table created')
conn.close()
