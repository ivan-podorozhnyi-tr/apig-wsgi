from apig_wsgi import make_lambda_handler
from flask import Flask

app = Flask(__name__)


@app.route('/browse/hello')
def hello_world():
    return 'Hello World!'


alb_lambda_handler = make_lambda_handler(app)
