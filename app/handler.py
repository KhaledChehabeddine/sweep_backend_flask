import json

application = create_app()


def handler(event, context):
    response = application.full_dispatch_request(request.json)
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(),
    }
