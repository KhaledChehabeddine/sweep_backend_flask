"""Summary: Application Configurator

Creates an application instance that registers all the project's blueprints
"""

from flask import Flask, Response, redirect, render_template, url_for
from flask.logging import create_logger
from app.controllers.account.account_category_item_controller import account_category_item_api_v1
from app.controllers.account.account_category_controller import account_category_api_v1
from app.controllers.home.home_main_feature_item_controller import home_main_feature_item_api_v1
from app.controllers.home.home_sub_feature_controller import home_sub_feature_api_v1
from app.controllers.home.home_feature_item_controller import home_feature_item_api_v1
from app.controllers.user.user_controller import user_api_v1
from app.controllers.components.category_controller import category_api_v1
from app.controllers.components.review_controller import review_api_v1
from app.controllers.components.service_category_controller import service_category_api_v1
from app.controllers.components.service_item_controller import service_item_api_v1
from app.routes.blueprints import sweep_api_v1


def create_application() -> Flask:
    """
    :return: Flask application instance
    """
    application = Flask(__name__, template_folder='build/templates')

    application.register_blueprint(account_category_api_v1)
    application.register_blueprint(account_category_item_api_v1)
    application.register_blueprint(category_api_v1)
    application.register_blueprint(home_main_feature_item_api_v1)
    application.register_blueprint(home_sub_feature_api_v1)
    application.register_blueprint(home_feature_item_api_v1)
    application.register_blueprint(review_api_v1)
    application.register_blueprint(service_category_api_v1)
    application.register_blueprint(service_item_api_v1)
    application.register_blueprint(sweep_api_v1)
    application.register_blueprint(user_api_v1)

    logger = create_logger(application)

    @application.route('/')
    def home():
        return render_template('home.html')

    @application.errorhandler(404)
    def page_not_found(error) -> Response:
        logger.error(error)
        return redirect(url_for('home'))

    return application
