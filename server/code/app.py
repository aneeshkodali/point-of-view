#### IMPORTS

## imports from python
from flask import Flask

## imports from project


#### APP SETUP

# initialize app
app = Flask(__name__)


#### ENDPOINT CONFIG
@app.route('/')
def index():
    return 'Hello World'


#### RUN APP
if __name__ == "__main__":
    app.run(debug=True)
