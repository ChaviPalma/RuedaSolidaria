from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ruta(db.Model):
    __tablename__ = 'ruta'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origen = db.Column(db.String(50), nullable=False)
    destino = db.Column(db.String(50), nullable=False)
    puntos = db.Column(db.JSON, nullable=False)  # Campo para almacenar puntos
    cupos_disponibles = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, origen, destino, puntos, cupos_disponibles=0):
        self.origen = origen
        self.destino = destino
        self.puntos = puntos  # Inicializa el campo de puntos
        self.cupos_disponibles = cupos_disponibles







