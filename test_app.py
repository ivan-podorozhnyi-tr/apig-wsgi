import pytest

from app import alb_lambda_handler, app as flask_app


@pytest.fixture
def elb_event():
    event = {
        "requestContext": {
            "elb": {
                "targetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:XXXXXXXXXXX:targetgroup/sample/6d0ecf831eec9f09"
            }
        },
        "httpMethod": "GET",
        "path": "/browse/hello",
        "queryStringParameters": {},
        "headers": {
            "host": "lambda-YYYYYYYY.elb.amazonaws.com",
            "accept-encoding": "gzip",
            "accept-language": "en-US,en;q=0.5",
            "X-Forwarded-Proto": "http"  # todo: X-Forwarded-Proto is necessary
        },
        "body": "",
        "isBase64Encoded": False
    }
    return event


def test_app_lambda_handler(elb_event):
    response = alb_lambda_handler(elb_event, {})
    assert response["body"] == "Hello World!"


def test_hello_world():
    with flask_app.test_client() as c:
        response = c.get("/browse/hello")
        assert response.status == "200 OK"
        assert response.data == b"Hello World!"
