from flask import Flask, request, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('redirect-demo_login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['user'] == 'admin':
        return redirect(url_for('success'))
    abort(401)

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)