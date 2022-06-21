from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def static_demo():
    return render_template('jinja2_staticfile.html')

if __name__ == '__main__':
    app.run(debug=True)