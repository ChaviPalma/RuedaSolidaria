
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Asignacion(db.Model):
    __tablename__ = 'asignaciones'
    id_asig = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alumno_ID = db.Column(db.Integer, db.ForeignKey('alumnos.alumno_ID'), nullable=False)
    ruta_ID = db.Column(db.Integer, db.ForeignKey('ruta.id'), nullable=False)
    conductor_ID = db.Column(db.Integer, db.ForeignKey('conductores.conductor_ID'), nullable=False)
    fecha_asignacion = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)

    # Relaciones
    alumno = db.relationship('Alumno', backref='asignaciones')
    ruta = db.relationship('Ruta', backref='asignaciones')
    conductor = db.relationship('Conductor', backref='asignaciones')

    def __repr__(self):
        return f"<Asignacion(id_asig={self.id_asig}, alumno_ID={self.alumno_ID}, ruta_ID={self.ruta_ID}, conductor_ID={self.conductor_ID})>"
