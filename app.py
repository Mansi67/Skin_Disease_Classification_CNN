
from flask import Flask

UPLOAD_FOLDER = 'C:/Users/mansi/Desktop/Study/Skin_Disease/Uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER