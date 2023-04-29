"""Summary: AWS Lambda Application Configurator

Creates an application instance before configuring and running it on an AWS Lamda, named application_entry_point
"""
from app.factory import create_application

application = create_application()


# noinspection PyUnusedLocal
# pylint: disable=unused-argument
def handler(event, context) -> dict:
    """
    :param event: The Lambda Event containing the request data (path, headers and so on)
    :param context: The Lambda Context runtime methods and attributes (not needed for now)
    :return: Dictionary containing the response data, along with its necessary headers and status code
    """
    with application.test_request_context(path=event['requestContext']['http']['path'],
                                          method=event['requestContext']['http']['method'], headers=event['headers'],
                                          data=event.get('body', '')):
        response = application.full_dispatch_request()
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(),
    }
