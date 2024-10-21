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