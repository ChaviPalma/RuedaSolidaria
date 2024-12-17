from collections import namedtuple
import mysql.connector

class AlumnoModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def crear_alumno(self, alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto=None):
        try:
            query = """
            INSERT INTO Alumnos (alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def actualizar_alumno(self, alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto=None):
        try:
            query = """
            UPDATE Alumnos 
            SET pnombre_alum = %s, snombre_alum = %s, apaterno_alum = %s, amaterno_alum = %s, inst_ID = %s, foto = %s
            WHERE alumno_ID = %s
            """
            self.cursor.execute(query, (pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto, alumno_ID))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def eliminar_alumno(self, alumno_ID):
        try:
            query = "DELETE FROM Alumnos WHERE alumno_ID = %s"
            self.cursor.execute(query, (alumno_ID,))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_alumnos(self):
        try:
            query = "SELECT alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto FROM Alumnos"
            self.cursor.execute(query)
            alumnos = self.cursor.fetchall()

            Alumno = namedtuple('Alumno', 'alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto')
            alumnos = [Alumno(*alumno) for alumno in alumnos]

            return alumnos
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            self.cursor.close()
            self.connection.close()

    def buscar_alumno(self, alumno_ID):
        try:
            query = "SELECT * FROM Alumnos WHERE alumno_ID = %s"
            self.cursor.execute(query, (alumno_ID,))
            alumno_data = self.cursor.fetchone() 
            if alumno_data:
                Alumno = namedtuple('Alumno', 'alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID, foto')
                alumno = Alumno(*alumno_data)
                return alumno 
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            self.cursor.close()
            self.connection.close()
