from collections import namedtuple
import mysql.connector

class ConductorModel:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='RuedaSolidaria'
        )
        self.cursor = self.connection.cursor()

    def listar_conductores(self):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID FROM Conductor"
            self.cursor.execute(query)
            conductores = self.cursor.fetchall()

            Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID')
            conductores = [Conductor(*conductor) for conductor in conductores]

            return conductores
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return []
        finally:
            self.cursor.close()  
            self.connection.close()

    def buscar_conductor(self, conductor_ID):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID FROM Conductor WHERE conductor_ID = %s"
            self.cursor.execute(query, (conductor_ID,))
            conductor = self.cursor.fetchone()

            if conductor:
                Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID')
                return Conductor(*conductor)
            return None
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return None
        finally:
            self.cursor.close()  
            self.connection.close()

    def actualizar_conductor(self, conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID):
        try:
            query = """
            UPDATE Conductor 
            SET pnombre_cond = %s, snombre_cond = %s, appaterno_cond = %s, apmaterno_cond = %s, inst_ID = %s 
            WHERE conductor_ID = %s
            """
            self.cursor.execute(query, (pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, conductor_ID))
            self.connection.commit()  
            return self.cursor.rowcount 
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return 0
        finally:
            self.cursor.close()  
            self.connection.close()

    def eliminar_conductor(self, conductor_ID):
        try:
            query = "DELETE FROM Conductor WHERE conductor_ID = %s"
            self.cursor.execute(query, (conductor_ID,))
            self.connection.commit()  
            return self.cursor.rowcount 
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            return 0
        finally:
            self.cursor.close()  
            self.connection.close()
