from flask_sqlalchemy import SQLAlchemy
import mysql.connector

class UsuarioModel:
    def __init__(self):
        
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'RuedaSolidaria'
        )
        self.cursor =  self.connection.cursor()

    def crear_usuario(self, email, contrasena):
        try:
            query = "INSERT INTO USUARIOS (EMAIL, CONTRASENA) VALUES (%s, %s)"
            self.cursor.execute(query, (email, contrasena))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error, {err}")
        finally:
            self.cursor.close()
            self.connection.close()
    
   
    def listar_usuarios(self):  # <-- Quita user_ID y email de aquí
        try:
            query = "SELECT user_ID, email, admin_ID, conductor_ID, alumno_ID FROM USUARIOS"
            self.cursor.execute(query)
            usuarios = self.cursor.fetchall()

            # (Optional) If you want to use namedtuples:
            from collections import namedtuple
            # Asegúrate de que la namedtuple tenga todas las columnas de la consulta
            Usuario = namedtuple('Usuario', 'user_ID, email, admin_ID, conductor_ID, alumno_ID')  
            usuarios = [Usuario(*usuario) for usuario in usuarios]

            return usuarios
        except mysql.connector.Error as err:
            print(f"Error, {err}")
        finally:
            self.cursor.close()
            self.connection.close()