from app.factory import create_app
import configparser
import os.path

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join('config.ini')))

if __name__ == '__main__':
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']

    app.run(host='0.0.0.0')
