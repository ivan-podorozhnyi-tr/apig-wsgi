# Try to setup WSGI application

### apig-wsig
`make_lambda_handler` wraps Flask WSGI application and give's lambda 
compatible function on output
```python
from apig_wsgi import make_lambda_handler
from flask import Flask

app = Flask(__name__)

@app.route('/browse/hello')
def hello_world():
    return 'Hello World!'

lambda_handler = make_lambda_handler(app)
```


### ALB Cloud Formation stack
To create CloudFormation stack:
```bash
sceptre create dev
```
Creates Application Load Balancer, Lambda function, Role for lambda, 
lambda invoke permission for ALB, ALB lambda Target group.
Watch `zappa-overview/templates/main.yaml`

### Deploy lambda
To deploy(update) your lambda source code(Flask server):
```bash
make deploy lambda_name=retrieve_lambda_name_from_cloudformation_stack
```

After deploying, ALB public domain name accessible, so you can test your app.
Open http://{ALB_domain_name}/browse/hello

http://apig-wsgi-alb-104503537.eu-central-1.elb.amazonaws.com/browse/hello - 
already deployed example
### Run locally
To run tests locally activate your virtualenv and do the following:
```bash
pip install requirements-test.txt
pytest test_app.py
```