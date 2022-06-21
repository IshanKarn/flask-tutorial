from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    myResponse = make_response('Response')
    myResponse.headers['customHeader'] = 'custom header'
    # myResponse.status_code = 403
    
    return myResponse

if __name__ == '__main__':
    app.run(debug=True)