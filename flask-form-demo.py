from flask import Flask, request, redirect, url_for, render_template, flash, abort
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development_key'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact-form.html', form=form)
        else:
            return render_template('success.html')
    elif request.method=='GET':
        return render_template('contact-form.html', form=form)

# @app.route('/success')
# def success():
#     return "<h1>Successfully sent.<h1>"

if __name__ == '__main__':
    app.run(debug=True)