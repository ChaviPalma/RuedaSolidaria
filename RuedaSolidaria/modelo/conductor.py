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

    def crear_conductor(self, conductor_id, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_id):
        try:
            query = """
            INSERT INTO Conductor (conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (conductor_id, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_id))
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()

    def listar_conductores(self):
        try:
            query = "SELECT conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID FROM Conductor"
            self.cursor.execute(query)
            conductores = self.cursor.fetchall()

            Conductor = namedtuple('Conductor', 'conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID')
            conductores = [Conductor(*conductor) for conductor in conductores]

            return conductores
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            self.cursor.close()
            self.connection.close()
