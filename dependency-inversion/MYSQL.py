import mysql.connector
 
class MySQL(BaseDatos):
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
 
    def guardar(self, datos):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tabla (columna) VALUES (%s)", (datos,))
        self.connection.commit()
        cursor.close()
 
    def leer(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT columna FROM tabla")
        datos = cursor.fetchall()
        cursor.close()
        return datos