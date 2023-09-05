import os

from flask import Flask


def create_app(test_config=None):
    # creating and configuring application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # if exists, load the instance configuration
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load basic test config
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return 'Hello, Samus'
    
    return app