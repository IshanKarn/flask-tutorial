from msilib.schema import ODBCAttribute
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'studyik14@gmail.com'
app.config['MAIL_PASSWORD'] = 'tyizncafgwdozjuv'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    msg = Message('Hello', sender = 'studyik14@gmail.com', recipients = ['ishankarn14@gmail.com', 'choudharypushkar889@gmail.com'])
    msg.body = "Mail sent from development server @T3"
    mail.send(msg)
    return "Sent"

if __name__=="__main__":
    app.run(debug=True)