from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from config import ConfiguracionBd



db = SQLAlchemy()


def create_apli():
    app = Flask(__name__)
    app.config.from_object( ConfiguracionBd
)

    db.init_app(app)

    migrate = Migrate(app, db)

    from .controlador.usuario_controlador import usuarios_bp
    app.register_blueprint(usuarios_bp)
    return app