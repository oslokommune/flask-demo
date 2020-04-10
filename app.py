# https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, world!"
