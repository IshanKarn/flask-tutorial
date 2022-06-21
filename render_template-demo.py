from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    # html file must be inside templates folder (in application folder)
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()