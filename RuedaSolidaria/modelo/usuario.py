from flask_sqlalchemy import SQLAlchemy
from RuedaSolidaria import db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'

    user_ID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    contrasena = db.Column(db.String(255), nullable=False)
    admin_ID = db.Column(db.Integer, db.ForeignKey('Administrador.admin_ID'))
    conductor_ID = db.Column(db.Integer, db.ForeignKey('Conductor.conductor_ID'))
    alumno_ID = db.Column(db.Integer, db.ForeignKey('Alumnos.alumno_ID'))

    def __repr__(self):
        return f'<Usuario {self.user_ID}>'

    def __init__(self, id, email, password, admin_id, conductor_id, alumno_id):
        self.id = id
        self.email = email
        self.password = password
        self.admin_id = admin_id
        self.conductor_id = conductor_id
        self.alumno_id = alumno_id