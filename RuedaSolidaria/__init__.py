# RuedaSolidaria/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/RuedaSolidaria'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = ''

    db.init_app(app)

    from .controlador.usuario_controlador import usuarios_bp
    app.register_blueprint(usuarios_bp)

    return app