import mysql.connector
from collections import namedtuple

class ViajeModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_viaje(self, viaje_ID, ID_ruta, alumno_ID, fecha, hora, calificacion, comentario=None):
        try:
            query = "INSERT INTO Viaje (viaje_ID, ID_ruta, alumno_ID, fecha, Hora, calificacion, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(query, (viaje_ID, ID_ruta, alumno_ID, fecha, hora, calificacion, comentario))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_viajes(self):
        try:
            query = "SELECT viaje_ID, ID_ruta, alumno_ID, fecha, Hora, calificacion, comentario FROM Viaje"
            self.cursor.execute(query)
            viajes = self.cursor.fetchall()

            Viaje = namedtuple('Viaje', 'viaje_ID, ID_ruta, alumno_ID, fecha, Hora, calificacion, comentario')
            viajes = [Viaje(*viaje) for viaje in viajes]

            return viajes
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_viaje(self, viaje_ID):
        try:
            query = "SELECT * FROM Viaje WHERE viaje_ID = %s"
            self.cursor.execute(query, (viaje_ID,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_viaje(self, viaje_ID, ID_ruta, alumno_ID, fecha, hora, calificacion, comentario=None):
        try:
            query = "UPDATE Viaje SET ID_ruta = %s, alumno_ID = %s, fecha = %s, Hora = %s, calificacion = %s, comentario = %s WHERE viaje_ID = %s"
            self.cursor.execute(query, (ID_ruta, alumno_ID, fecha, hora, calificacion, comentario, viaje_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_viaje(self, viaje_ID):
        try:
            query = "DELETE FROM Viaje WHERE viaje_ID = %s"
            self.cursor.execute(query, (viaje_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()
