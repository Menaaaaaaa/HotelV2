import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password='',
                database=self.database
            )
            print("Conexión establecida.")
            return True
        except Error as err:
            print("Error al conectar a la base de datos:", err)
            self.connection = None
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")

    def is_connected(self):
        return self.connection is not None and self.connection.is_connected()

    def execute_query(self, query, params=None):
        if not self.is_connected():
            print("No hay conexión a la base de datos.")
            return None
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            print("Consulta exitosa.")
            if query.strip().lower().startswith('select'):
                result = cursor.fetchall()
                if not result:
                    print("")
                    return None
                return result
        except Error as err:
            print("Error:", err)
            return None
        finally:
            cursor.close()