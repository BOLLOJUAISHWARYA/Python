from flask import Flask,render_template,request,jsonify
import os

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
    try:
      id = request.form.get('id')
      name = request.form.get('name')
      city = request.form.get('city')
      pin = request.form.get('pin')
      password = request.form.get('pwd')

      with sql.connect('database.db') as con:
          cur = con.cursor()
          cur.execute('''INSERT INTO details(id,name,city,pin,password) VALUES (?,?,?,?,?)''',(id,name,city,pin,password))
          con.commit()
          msg = "Added"

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
            c = cur.execute(f"SELECT * from details WHERE name='{name}' AND password='{password}'")
            rows = c.fetchall()
            return render_template("result.html",rows=rows)
    con.close()

@app.route("/update")
def update():
    return render_template("update.html")


@app.route("/updaterecord", methods=["POST"])
def updaterecord():

    id = request.form['id']
    name = request.form['name']
    city = request.form['city']
    pin = request.form['pin']
    password = request.form['pwd']
    with sql.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute(f"UPDATE details SET name ='{name}',city ='{city}',pin ='{pin}',password ='{password}' WHERE id ='{id}'")
            con.commit()
            msg = "updated"
        except:
            msg = "can't update"
    return msg
    conn.close()

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form['string']
    with sql.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute(f"DELETE from details WHERE id = '{id}'")
            msg = "record successfully deleted"

        except:
            msg = "can't be deleted"
        finally:
            return jsonify(msg)
    con.close()


app.run()