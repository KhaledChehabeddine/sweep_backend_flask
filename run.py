"""Summary: Local Application Configurator

Creates an application instance before configuring and running it locally
"""

from app.factory import create_application

if __name__ == '__main__':
    application = create_application()
    application.config['DEBUG'] = True

    application.run(host='127.0.0.1')
