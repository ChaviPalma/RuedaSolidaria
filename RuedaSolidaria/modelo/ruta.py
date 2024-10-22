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

    def crear_ruta(self, ID_ruta, Origen, Destino, est_ID, conductor_ID):
        try:
            query = "INSERT INTO Ruta (ID_ruta, Origen, Destino, est_ID, conductor_ID) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(query, (ID_ruta, Origen, Destino, est_ID, conductor_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_rutas(self):
        try:
            query = "SELECT ID_ruta, Origen, Destino, est_ID, conductor_ID FROM Ruta"
            self.cursor.execute(query)
            rutas = self.cursor.fetchall()

        
            Ruta = namedtuple('Ruta', 'ID_ruta, Origen, Destino, est_ID, conductor_ID')
            rutas = [Ruta(*ruta) for ruta in rutas]

            return rutas
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_ruta(self, ID_ruta):
        try:
            query = "SELECT * FROM Ruta WHERE ID_ruta = %s"
            self.cursor.execute(query, (ID_ruta,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_ruta(self, ID_ruta, Origen, Destino, est_ID, conductor_ID):
        try:
            query = "UPDATE Ruta SET Origen = %s, Destino = %s, est_ID = %s, conductor_ID = %s WHERE ID_ruta = %s"
            self.cursor.execute(query, (Origen, Destino, est_ID, conductor_ID, ID_ruta))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_ruta(self, ID_ruta):
        try:
            query = "DELETE FROM Ruta WHERE ID_ruta = %s"
            self.cursor.execute(query, (ID_ruta,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()