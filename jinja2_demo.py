from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return render_template('hello_jinja2.html', name=name)

if __name__ == '__main__':
    app.run()