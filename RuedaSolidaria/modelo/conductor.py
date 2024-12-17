from collections import namedtuple
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ConductorModel(db.Model):
    __tablename__ = 'Conductor'  # El nombre de la tabla en la base de datos

    conductor_ID = db.Column(db.Integer, primary_key=True)  # Clave primaria
    pnombre_cond = db.Column(db.String(50), nullable=False)  # Primer nombre del conductor
    snombre_cond = db.Column(db.String(50), nullable=False)  # Segundo nombre del conductor
    appaterno_cond = db.Column(db.String(50))  # Apellido paterno del conductor
    apmaterno_cond = db.Column(db.String(50))  # Apellido materno del conductor
    inst_ID = db.Column(db.Integer, db.ForeignKey('Establecimiento.est_ID'), nullable=False)  # ID de establecimiento
    id_tipo_usuario = db.Column(db.Integer, db.ForeignKey('tipo_usuario.id_tipo_usuario'), nullable=False)  # ID del tipo de usuario


    def __repr__(self):
        return f'<Conductor {self.pnombre_cond} {self.snombre_cond} {self.appaterno_cond} {self.apmaterno_cond}>'
    def listar_conductores(self):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil FROM Conductor"
            self.cursor.execute(query)
            conductores = self.cursor.fetchall()

            Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil')
            conductores = [Conductor(*conductor) for conductor in conductores]

            return conductores
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return []
        finally:
            self.cursor.close()  
            self.connection.close()


    def buscar_conductor(self, conductor_ID):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil FROM Conductor WHERE conductor_ID = %s"
            self.cursor.execute(query, (conductor_ID,))
            conductor = self.cursor.fetchone()

            if conductor:
                Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil')
                return Conductor(*conductor)
            return None
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return None
        finally:
            self.cursor.close()  
            self.connection.close()


    def actualizar_conductor(self, conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil=None):
        try:
            # Si foto_perfil es proporcionada, actualiza también la columna de foto de perfil
            if foto_perfil:
                query = """
                UPDATE Conductor 
                SET pnombre_cond = %s, snombre_cond = %s, appaterno_cond = %s, apmaterno_cond = %s, inst_ID = %s, foto_perfil = %s 
                WHERE conductor_ID = %s
                """
                self.cursor.execute(query, (pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, foto_perfil, conductor_ID))
            else:
                query = """
                UPDATE Conductor 
                SET pnombre_cond = %s, snombre_cond = %s, appaterno_cond = %s, apmaterno_cond = %s, inst_ID = %s 
                WHERE conductor_ID = %s
                """
                self.cursor.execute(query, (pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, conductor_ID))

            self.connection.commit()  
            return self.cursor.rowcount 
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return 0
        finally:
            self.cursor.close()  
            self.connection.close()

    def eliminar_conductor(self, conductor_ID):
        try:
            query = "DELETE FROM Conductor WHERE conductor_ID = %s"
            self.cursor.execute(query, (conductor_ID,))
            self.connection.commit()  
            return self.cursor.rowcount 
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return 0
        finally:
            self.cursor.close()  
            self.connection.close()
