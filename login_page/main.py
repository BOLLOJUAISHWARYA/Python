from flask import Flask,render_template,request

import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('database.db')
conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enter')
def new():
    return render_template('new.html')

@app.route('/add',methods=['POST'])
def add():
    if request.method == 'POST':
        try:
          id = request.form['id']
          name = request.form['name']
          city = request.form['city']
          pin = request.form['pin']
          password = request.form['pwd']

          with sql.connect('database.db') as con:
              cur = con.cursor()
              cur.execute('''INSERT INTO details(id,name,city,pin,password) VALUES (?,?,?,?,?)''',(id,name,city,pin,password))
              msg= "Added"

        except:
            con.rollback()
            msg = "Error..!couldn't insert"

        finally:
            return msg
            con.close()

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/check',methods=['POST','GET'])
def check():
    name = request.form['name']
    password = request.form['pwd']

    with sql.connect('database.db') as con:
        cur = con.cursor()
        c = cur.execute(f"SELECT * from details WHERE name='{name}' AND password='{password}'")
        if not c.fetchone():
            return render_template('new.html')
        else:
            con.row_factory = sql.Row
            cur = con.cursor()
            c = cur.execute(f"SELECT * from details WHERE name='{name}'")
            rows = c.fetchall()
            return render_template("result.html",rows=rows)

app.run()