import mysql.connector
from collections import namedtuple

class TipoUsuarioModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='loki',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def listar_tipos_usuario(self):
        try:
            query = "SELECT id_tipo_usuario, descripcion FROM tipo_usuario"
            self.cursor.execute(query)
            results = self.cursor.fetchall()  # Recupera todos los resultados

            if results:
                # Devuelve una lista de namedtuple con los resultados
                return [namedtuple('TipoUsuario', 'id_tipo_usuario descripcion')(*result) for result in results]
            else:
                return []  # Retorna una lista vacía si no hay resultados

        except mysql.connector.Error as err:
            print(f"Error al consultar los tipos de usuario: {err}")
            return []  # En caso de error, retornamos una lista vacía
        finally:
            self.cursor.close()  # Cerrar el cursor después de la consulta
            self.connection.close()  # Cerrar la conexión a la base de datos
