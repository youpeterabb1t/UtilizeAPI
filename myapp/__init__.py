from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment

import atexit
from config import config

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
#simulator run
from .pub_api.agent import agent_initiate


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)  # modified 20191108
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.py')
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .mailing import mailing as mail_blueprint
    app.register_blueprint(mail_blueprint, url_prefix='/mailing')
    agent_initiate.delay()
    return app

