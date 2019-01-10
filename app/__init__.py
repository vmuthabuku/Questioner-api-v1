from flask import Flask
from .instance.config import app_config
from .api.v1.endpoints.meetups_endpoints import meetup_print
from .api.v1.endpoints.question_endpoints import questions_print



def create_app(config):
    """Receives the necessary configuration and passes to create_app"""

    app = Flask(__name__)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(meetup_print)
    app.register_blueprint(questions_print)

    return app