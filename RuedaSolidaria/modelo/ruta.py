from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ruta(db.Model):
    __tablename__ = 'ruta'

    ID_ruta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Origen = db.Column(db.String(50), nullable=False)
    Destino = db.Column(db.String(50), nullable=False)
    Puntos = db.Column(db.JSON, nullable=False)  # Campo para almacenar puntos
    Cupos_disponibles = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, origen, destino, puntos, cupos_disponibles=0):
        self.Origen = origen
        self.Destino = destino
        self.Puntos = puntos  # Inicializa el campo de puntos
        self.Cupos_disponibles = cupos_disponibles
