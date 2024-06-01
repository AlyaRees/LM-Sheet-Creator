from flask import Flask, request, render_template
import os
from flask_dropzone import Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.update(
    UPLOADED_PATH = os.path.join(basedir, 'uploads'),
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    