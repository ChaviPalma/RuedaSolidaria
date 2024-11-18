from collections import namedtuple
import mysql.connector


class UsuarioModel:
    def __init__(self, user_ID, email, admin_ID=None, conductor_ID=None, alumno_ID=None, id_tipo_usuario=None):
        self.user_ID = user_ID
        self.email = email
        self.admin_ID = admin_ID
        self.conductor_ID = conductor_ID
        self.alumno_ID = alumno_ID
        self.id_tipo_usuario = id_tipo_usuario
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_usuario(self, email, contrasena, id_tipo_usuario):
        try:
            query = "INSERT INTO USUARIOS (EMAIL, CONTRASENA, id_tipo_usuario) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (email, contrasena, id_tipo_usuario))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_tipos_usuario(self):
        try:
            # Consulta para obtener los tipos de usuario
            query = "SELECT id_tipo_usuario, descripcion FROM tipo_usuario"
            self.cursor.execute(query)
            tipos_usuario = self.cursor.fetchall()

            if tipos_usuario:
                print("Tipos de usuario encontrados:", tipos_usuario)
            else:
                print("No se encontraron tipos de usuario.")

            # Usamos namedtuple para estructurar los resultados
            TipoUsuario = namedtuple('TipoUsuario', 'id_tipo_usuario, descripcion')
            tipos_usuario = [TipoUsuario(*tipo) for tipo in tipos_usuario]

            return tipos_usuario
        except mysql.connector.Error as err:
            print(f"Error, {err}")
            return []  # Retorna lista vacía si ocurre un error
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_usuario(self, email):
        try:
            query = "SELECT * FROM USUARIOS WHERE EMAIL = %s"
            self.cursor.execute(query, (email,))
            return self.cursor.fetchone()  # Retorna una tupla con los datos del usuario
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None  # Devuelve None si hay un error
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_usuario(self, email, contrasena, id_tipo_usuario):
        try:
            query = "UPDATE USUARIOS SET CONTRASENA = %s, id_tipo_usuario = %s WHERE EMAIL = %s"
            self.cursor.execute(query, (contrasena, id_tipo_usuario, email))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_usuario(self, email):
        try:
            query = "DELETE FROM USUARIOS WHERE EMAIL = %s"
            self.cursor.execute(query, (email,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

  
    def listar_usuarios(self):
        try:
            query = "SELECT user_ID, email, admin_ID, conductor_ID, alumno_ID, id_tipo_usuario FROM USUARIOS"
            self.cursor.execute(query)
            usuarios = self.cursor.fetchall()

            # Crear una lista para almacenar las instancias de UsuarioModel
            usuarios_obj = []
            for usuario in usuarios:
                # Crear una instancia de UsuarioModel con los datos de la base de datos
                usuario_obj = UsuarioModel(
                    user_ID=usuario[0],  # user_ID
                    email=usuario[1],  # email
                    admin_ID=usuario[2],
                    conductor_ID=usuario[3],
                    alumno_ID=usuario[4],
                    id_tipo_usuario=usuario[5]
                )
                usuarios_obj.append(usuario_obj)

            return usuarios_obj

        except mysql.connector.Error as err:
            print(f"Error al recuperar los datos del usuario: {err}")
            return []  # Devuelve lista vacía si ocurre un error

        finally:
            self.cursor.close()
            self.connection.close()