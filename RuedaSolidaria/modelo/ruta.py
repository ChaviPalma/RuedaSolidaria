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


import mysql.connector
from collections import namedtuple

class RutaModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_ruta(self, origen, destino, puntos, cupos_disponibles=0):
        try:
            query = """
                INSERT INTO ruta (origen, destino, puntos, cupos_disponibles) 
                VALUES (%s, %s, %s, %s)
            """
            self.cursor.execute(query, (origen, destino, puntos, cupos_disponibles))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_rutas(self):
        try:
            query = "SELECT id, origen, destino, puntos, cupos_disponibles FROM ruta"
            self.cursor.execute(query)
            rutas = self.cursor.fetchall()

            # Definir una tupla nombrada para un acceso más claro a los datos
            Ruta = namedtuple('Ruta', 'id origen destino puntos cupos_disponibles')
            rutas = [Ruta(*ruta) for ruta in rutas]

            return rutas
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_ruta(self, id, origen, destino, puntos, cupos_disponibles):
        try:
            query = """
                UPDATE ruta 
                SET origen = %s, destino = %s, puntos = %s, cupos_disponibles = %s
                WHERE id = %s
            """
            self.cursor.execute(query, (origen, destino, puntos, cupos_disponibles, id))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            print(f"Error al actualizar la ruta: {err}")

    def eliminar_ruta(self, id):
        try:
            query = "DELETE FROM ruta WHERE id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()