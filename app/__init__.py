from flask import Flask
from .instance.config import app_config
from .api.v1.endpoints.product_endpoints import product_print
from .api.v1.endpoints.sale_endpoints import sale_manager


def create_app(config):
    """Receives the necessary configuration and passes to create_app"""

    app = Flask(__name__)
    app.config.from_object(app_config[config])
    app.url_map.strict_slashes = False

    app.register_blueprint(product_print) 
    app.register_blueprint(sale_manager)

    return app