import json
from app.factory import create_app
from flask import request

application = create_app()


def handler(event, context):
    method = event['requestContext']['http']['method']
    path = event['requestContext']['http']['path']
    with application.test_request_context(
            path=path, method=method, headers=event['headers'], data=event.get('body', "")):
        response = application.full_dispatch_request(request.json)
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(),
    }
