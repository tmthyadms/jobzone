from flask import Flask, render_template
from flask_session import Session
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/jobzone"
app.config["CORS_HEADERS"] = "Content-Type"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
mongo = PyMongo(app)
CORS(app)
Session(app)

@cross_origin()
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

from modules import auth, business, job_posting, job_seeker

if __name__ == "__main__":
    app.run(port=6001, debug=True)

# https://www.digitalocean.com/community/tutorials/how-to-use-web-forms-in-a-flask-application#step-2-setting-up-forms
# https://medium.com/techcrush/how-to-render-html-file-in-flask-3fbfb16b47f6