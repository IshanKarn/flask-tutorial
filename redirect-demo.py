from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

login_attempt = 0

@app.route('/')
def index():
    return render_template('redirect-demo_login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global login_attempt
    login_attempt += 1
    if login_attempt > 3:
        login_attempt = 0
        return 'Login attempt reached!'
    if request.method == 'POST' and request.form['user'] == 'admin':
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)