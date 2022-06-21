from flask import Flask, render_template

app = Flask(__name__)

@app.route('/score/<int:score>')
def result(score):
    return render_template('jinja2_conditional.html', marks=score)

if __name__ == '__main__':
    app.run()