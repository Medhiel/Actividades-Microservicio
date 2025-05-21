from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, AnonymousUserMixin
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
   

    from app.routes import main, eventos_bp
    from app.auth_routes import auth
    from app.forms import EventoForm, ChangePasswordForm, LoginForm, RegisterForm

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(eventos_bp)  # <-- AGREGA ESTA LÍNEA

    return app

from app import models