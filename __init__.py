from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
# En __init__.py
    app = Flask(__name__, template_folder='../templates')
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:loki@localhost:3306/RuedaSolidaria'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'  

    db.init_app(app)

    # Registro del blueprint de usuarios
    from .controlador.usuario_controlador import usuarios_bp
    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')  

    return app
