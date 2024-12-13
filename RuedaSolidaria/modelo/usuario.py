from collections import namedtuple
import mysql.connector


class UsuarioModel:
    def __init__(self, user_ID=None, email=None, admin_ID=None, conductor_ID=None, alumno_ID=None, id_tipo_usuario=None):
        self.user_ID = user_ID
        self.email = email
        self.admin_ID = admin_ID
        self.conductor_ID = conductor_ID
        self.alumno_ID = alumno_ID
        self.id_tipo_usuario = id_tipo_usuario

    @staticmethod
    def conectar():
        """Establece y retorna una conexión a la base de datos."""
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )

    def crear_usuario(self, email, contrasena, id_tipo_usuario):
        """Crea un nuevo usuario en la base de datos."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO USUARIOS (EMAIL, CONTRASENA, id_tipo_usuario) VALUES (%s, %s, %s)"
            cursor.execute(query, (email, contrasena, id_tipo_usuario))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def listar_tipos_usuario(self):
        """Lista los tipos de usuario existentes en la base de datos."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "SELECT id_tipo_usuario, descripcion FROM tipo_usuario"
            cursor.execute(query)
            tipos_usuario = cursor.fetchall()

            TipoUsuario = namedtuple('TipoUsuario', 'id_tipo_usuario, descripcion')
            return [TipoUsuario(*tipo) for tipo in tipos_usuario]
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
            connection.close()

    def buscar_usuario(self, email):
        """Busca un usuario por su correo electrónico."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM USUARIOS WHERE EMAIL = %s"
            cursor.execute(query, (email,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()
            connection.close()

    def actualizar_usuario(self, email, contrasena, id_tipo_usuario):
        """Actualiza la información de un usuario."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "UPDATE USUARIOS SET CONTRASENA = %s, id_tipo_usuario = %s WHERE EMAIL = %s"
            cursor.execute(query, (contrasena, id_tipo_usuario, email))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def eliminar_usuario(self, email):
        """Elimina un usuario por su correo electrónico."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "DELETE FROM USUARIOS WHERE EMAIL = %s"
            cursor.execute(query, (email,))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()

    def listar_usuarios(self):
        """Lista todos los usuarios en la base de datos."""
        connection = self.conectar()
        cursor = connection.cursor()
        try:
            query = "SELECT user_ID, email, admin_ID, conductor_ID, alumno_ID, id_tipo_usuario FROM USUARIOS"
            cursor.execute(query)
            usuarios = cursor.fetchall()

            usuarios_obj = []
            for usuario in usuarios:
                usuario_obj = UsuarioModel(
                    user_ID=usuario[0],
                    email=usuario[1],
                    admin_ID=usuario[2],
                    conductor_ID=usuario[3],
                    alumno_ID=usuario[4],
                    id_tipo_usuario=usuario[5]
                )
                usuarios_obj.append(usuario_obj)

            return usuarios_obj
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            cursor.close()
            connection.close()

    