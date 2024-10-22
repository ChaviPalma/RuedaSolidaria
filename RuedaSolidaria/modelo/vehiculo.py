import mysql.connector
from collections import namedtuple

class VehiculoModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_vehiculo(self, vehi_ID, nombre_vehi, color, patente, conductor_ID):
        try:
            query = "INSERT INTO Vehiculo (vehi_ID, nombre_vehi, color, patente, conductor_ID) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (vehi_ID, nombre_vehi, color, patente, conductor_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_vehiculos(self):
        try:
            query = "SELECT vehi_ID, nombre_vehi, color, patente, conductor_ID FROM Vehiculo"
            self.cursor.execute(query)
            vehiculos = self.cursor.fetchall()

            Vehiculo = namedtuple('Vehiculo', 'vehi_ID, nombre_vehi, color, patente, conductor_ID')
            vehiculos = [Vehiculo(*vehiculo) for vehiculo in vehiculos]

            return vehiculos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_vehiculo(self, vehi_ID):
        try:
            query = "SELECT * FROM Vehiculo WHERE vehi_ID = %s"
            self.cursor.execute(query, (vehi_ID,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_vehiculo(self, vehi_ID, nombre_vehi, color, patente, conductor_ID):
        try:
            query = "UPDATE Vehiculo SET nombre_vehi = %s, color = %s, patente = %s, conductor_ID = %s WHERE vehi_ID = %s"
            self.cursor.execute(query, (nombre_vehi, color, patente, conductor_ID, vehi_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_vehiculo(self, vehi_ID):
        try:
            query = "DELETE FROM Vehiculo WHERE vehi_ID = %s"
            self.cursor.execute(query, (vehi_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()
