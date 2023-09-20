from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return 'No file part'

    files = request.files.getlist('files')

    for file in files:
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

    return 'Files uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
