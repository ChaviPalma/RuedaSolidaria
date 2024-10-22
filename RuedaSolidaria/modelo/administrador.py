import mysql.connector
from collections import namedtuple

class AdministradorModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_administrador(self, admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono):
        try:
            query = """
                INSERT INTO Administrador 
                (admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_administrador(self, admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono):
        try:
            query = """
                UPDATE Administrador 
                SET pnombre_admin = %s, snombre_admin = %s, apaterno_admin = %s, amaterno_admin = %s, 
                    email = %s, contrasena = %s, telefono = %s 
                WHERE admin_ID = %s
            """
            self.cursor.execute(query, (pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, admin_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_administrador(self, admin_ID):
        try:
            query = "DELETE FROM Administrador WHERE admin_ID = %s"
            self.cursor.execute(query, (admin_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_administradores(self):
        try:
            query = "SELECT admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, telefono FROM Administrador"
            self.cursor.execute(query)
            administradores = self.cursor.fetchall()

      
            Administrador = namedtuple('Administrador', 'admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, telefono')
            administradores = [Administrador(*admin) for admin in administradores]

            return administradores
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_administrador(self, admin_ID):
        try:
            query = "SELECT * FROM Administrador WHERE admin_ID = %s"
            self.cursor.execute(query, (admin_ID,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            self.cursor.close()
            self.connection.close()
