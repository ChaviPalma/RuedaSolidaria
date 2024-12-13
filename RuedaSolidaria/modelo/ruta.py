
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

   
    def crear_ruta(cls, origen, destino, puntos, cupos_disponibles=0):
        nueva_ruta = cls(origen=origen, destino=destino, puntos=puntos, cupos_disponibles=cupos_disponibles)
        db.session.add(nueva_ruta)
        db.session.commit()


    def listar_rutas(cls):
        return cls.query.all()

    def actualizar_ruta(cls, id, origen, destino, puntos, cupos_disponibles):
        ruta = cls.query.get(id)
        if ruta:
            ruta.origen = origen
            ruta.destino = destino
            ruta.puntos = puntos
            ruta.cupos_disponibles = cupos_disponibles
            db.session.commit()
        else:
            raise ValueError("Ruta no encontrada.")

   
    def eliminar_ruta(cls, id):
        ruta = cls.query.get(id)
        if ruta:
            db.session.delete(ruta)
            db.session.commit()
        else:
            raise ValueError("Ruta no encontrada.")
