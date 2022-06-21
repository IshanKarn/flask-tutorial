from flask import Flask, request, render_template, url_for
import sqlite3 as sql


app = Flask(__name__)

@app.route('/enternew')
def new_student():
    return render_template('student-db.html')

@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        try:
            name = request.form['name']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
        
            with sql.connect('demo-database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) \
                    VALUES (?,?,?,?)", (name, addr, city, pin))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            con.close() 
            return render_template('result-db.html', msg=msg)

@app.route('/list')
def list():
    con = sql.connect('demo-database.db')
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template('list-db.html', rows=rows)

@app.route('/')
def index():
    return render_template('home-db.html')

if __name__ == '__main__':
    app.run(debug=True)