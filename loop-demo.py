from flask import Flask, render_template

app = Flask(__name__)

@app.route('/result')
def show_result():
    result={'physics':85, 'chemistry':56, 'mathematics':75, 'english':95}
    return render_template('jinja2_loop.html', result = result)

if __name__ == '__main__':
    app.run()