from flask import Flask, request, render_template, url_for
from forms import ContactForm1

app = Flask(__name__)
app.secret_key= 'dev_key'

@app.route('/contact1', methods=['GET', 'POST'])
def contact():
    form = ContactForm1()
    return render_template('contact-demo1.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)