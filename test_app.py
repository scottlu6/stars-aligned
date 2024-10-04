# test_app.py
from flask import Flask

app = Flask(__name__)


import flask
print(flask.__version__)  # This will print the version of Flask being used

@app.before_first_request
def create_tables():
    print("This runs before the first request.")

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
