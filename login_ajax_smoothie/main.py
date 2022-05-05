from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Homepage.html')


@app.route('/login', methods=["POST","GET"])
def login():
    username = request.form.get('username-login')
    password = request.form.get('password-login')

    with sql.connect('database.db') as con:

        cur = con.cursor()
        c = cur.execute(f"SELECT * from details WHERE username='{username}' AND password='{password}'")
        if not c.fetchone():
            msg = "Please get registered"
            return jsonify(msg)
        else:
            con.row_factory = sql.Row
            cur = con.cursor()
            c = cur.execute(f"SELECT * from details WHERE username='{username}' AND password='{password}'")
            rows = c.fetchall()
            return render_template("login.html", rows=rows)

@app.route('/update', methods=["POST","GET"])
def update():
    id = request.form.get('id')
    name = request.form.get('name')
    city = request.form.get('city')
    pin = request.form.get('pin')
    password = request.form.get('password')
    with sql.connect('database.db') as con:
        try:
            cur = con.cursor()
            cur.execute(f"UPDATE details SET name='{name}',city='{city}',pin='{pin}',password='{password}' WHERE id='{id}'")
            con.commit()
            msg = "updated your details..!"
            return jsonify(msg)

        except:
            con.rollback()
            msg = "Error..!couldn't update"
            return jsonify(msg)


    con.close()

@app.route("/delete", methods=["POST","GET"])
def delete():
    id = request.form.get('string')

    with sql.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute(f"DELETE from details WHERE id = '{id}'")
            msg = "Deleted successfully"

        except:
            msg = "can't delete"

        finally:
            return jsonify(msg)



@app.route('/registration', methods=["POST","GET"])
def registration():
    name = request.form.get('name')
    username = request.form.get('username')
    city = request.form.get('city')
    pin = request.form.get('pin')
    password = request.form.get('password')

    with sql.connect('database.db') as con:
        try:
            cur = con.cursor()
            cur.execute('''INSERT INTO details(name,username,city,pin,password) VALUES (?,?,?,?,?)''',
                        (name,username,city, pin, password))
            con.commit()
            msg = "Thank you for getting registered..!"
            return jsonify(msg)

        except:
            con.rollback()
            msg = "username is already taken.."
            return jsonify(msg)


    con.close()


app.run(host='0.0.0.0',port=5000)
