from collections import namedtuple
import mysql.connector

class ConductorModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='loki',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def listar_conductores(self):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID FROM Conductor"
            self.cursor.execute(query)
            conductores = self.cursor.fetchall()

            # Crear namedtuple para los conductores
            Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID')
            conductores = [Conductor(*conductor) for conductor in conductores]

            return conductores
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return []  # Retorna una lista vacía en caso de error
        finally:
            self.cursor.close()  # Asegúrate de cerrar el cursor
            self.connection.close()  # Cierra la conexión solo si se ha abierto previamente
