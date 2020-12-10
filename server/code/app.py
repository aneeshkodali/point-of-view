#### IMPORTS

## imports from python
from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os

## imports from project
from db import db

#### APP SETUP

# initialize app
app = Flask(__name__)

# connect db
DB_URI = os.getenv('DB_URI')
app.config['MONGODB_HOST'] = DB_URI
db.init_app(app)


#### ENDPOINT CONFIG
@app.route('/')
def index():
    return 'Hello World'


#### RUN APP
if __name__ == "__main__":
    app.run(debug=True)
