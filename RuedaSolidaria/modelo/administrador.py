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

    def crear_administrador(self, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario, estado='A'):
        try:
            query = """
                INSERT INTO Administrador (pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario, estado))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def buscar_administrador(self, admin_ID):
        try:
            query = """
                SELECT admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, fecha_creacion, estado, id_tipo_usuario
                FROM Administrador WHERE admin_ID = %s
            """
            self.cursor.execute(query, (admin_ID,))
            result = self.cursor.fetchone()

            if result:
                Administrador = namedtuple('Administrador', 'admin_ID pnombre_admin snombre_admin apaterno_admin amaterno_admin email contrasena telefono fecha_creacion estado id_tipo_usuario')
                return Administrador(*result)
            return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    def listar_administradores(self):
        try:
            query = """
                SELECT admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, fecha_creacion, estado, id_tipo_usuario
                FROM Administrador
            """
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            Administrador = namedtuple('Administrador', 'admin_ID pnombre_admin snombre_admin apaterno_admin amaterno_admin email contrasena telefono fecha_creacion estado id_tipo_usuario')
            return [Administrador(*result) for result in results]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def actualizar_administrador(self, admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario):
        try:
            query = """
                UPDATE Administrador
                SET pnombre_admin = %s, snombre_admin = %s, apaterno_admin = %s, amaterno_admin = %s, email = %s, contrasena = %s, telefono = %s, id_tipo_usuario = %s
                WHERE admin_ID = %s
            """
            self.cursor.execute(query, (pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario, admin_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def eliminar_administrador(self, admin_ID):
        try:
            query = "DELETE FROM Administrador WHERE admin_ID = %s"
            self.cursor.execute(query, (admin_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def cerrar_conexion(self):
        # Método para cerrar la conexión y el cursor
        self.cursor.close()
        self.connection.close()
