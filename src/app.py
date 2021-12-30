from flask import Flask
import json
from api.blueprints.home import app_home
from api.blueprints.prediction import app_predict
from api.blueprints.errors import errors
from api.blueprints.log import log


def create_app():
    app = Flask(__name__)

    with open('config.json') as config_file:
        config_data = json.load(config_file)
        app.config.update(config_data)

    app.register_blueprint(log)
    app.register_blueprint(errors)
    app.register_blueprint(app_home, url_prefix='/api')
    app.register_blueprint(app_predict, url_prefix='/api')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
