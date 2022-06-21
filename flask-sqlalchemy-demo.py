from flask import Flask, request, flash, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'development_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.sqlite3"

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin 

@app.route('/')
def show_all():
    return render_template('sqlalchemy-demo_home.html', students = students.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'],
            request.form['city'], request.form['addr'], 
            request.form['pin']) 

            db.session.add(student)
            db.session.commit()

            flash('Record added successfully')
            return redirect(url_for('show_all'))
    return render_template('sqlalchemy-demo_add-row.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)