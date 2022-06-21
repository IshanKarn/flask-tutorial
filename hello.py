from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

# @app.route('/a')
def hello_a():
    return 'Hello a'
app.add_url_rule("/a", "a", hello_a)

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello, %s!" %name

@app.route('/guest/<name>')
def hello_guest(name):
    return "Hello %s as guest user!" %name

from flask import redirect, url_for
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_name', name='Admin'))
    else:
        return redirect(url_for('hello_guest', name=name))

if __name__ == '__main__':
    app.run()