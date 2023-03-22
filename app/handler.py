from app.factory import create_application

application = create_application()


def handler(event, context):
    method = event['requestContext']['http']['method']
    path = event['requestContext']['http']['path']
    with application.test_request_context(
            path=path, method=method, headers=event['headers'], data=event.get('body', "")):
        response = application.full_dispatch_request()
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(),
    }
