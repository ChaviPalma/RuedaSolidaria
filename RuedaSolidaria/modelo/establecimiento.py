import mysql.connector
from collections import namedtuple

class EstablecimientoModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_establecimiento(self, est_ID, nombre_ins, direccion):
        try:
            query = "INSERT INTO Establecimiento (est_ID, nombre_ins, direccion) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (est_ID, nombre_ins, direccion))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()


    def actualizar_establecimiento(self, est_ID, nombre_ins, direccion):
        try:
            query = "UPDATE Establecimiento SET nombre_ins = %s, direccion = %s WHERE est_ID = %s"
            self.cursor.execute(query, (nombre_ins, direccion, est_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_establecimiento(self, est_ID):
        try:
            query = "DELETE FROM Establecimiento WHERE est_ID = %s"
            self.cursor.execute(query, (est_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_establecimientos(self):
        try:
            query = "SELECT est_ID, nombre_ins, direccion FROM Establecimiento"
            self.cursor.execute(query)
            establecimientos = self.cursor.fetchall()

        
            Establecimiento = namedtuple('Establecimiento', 'est_ID, nombre_ins, direccion')  
            establecimientos = [Establecimiento(*establecimiento) for establecimiento in establecimientos]

            return establecimientos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()
