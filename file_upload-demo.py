from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

#Configs
# Specify upload folder
app.config['UPLOAD_FOLDER'] = 'C:/Users/ishan/Desktop/Flask Practice (TutorialsPoint)/files'
# Limit upload size
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024 

@app.route('/upload')
def upload():
    return render_template('upload-demo.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
        return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)