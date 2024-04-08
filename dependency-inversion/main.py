if __name__ == "__main__":
    mysql_db = MySQL(host="localhost", user="root", password="12345", database="dependency_inversion")
    mongodb_db = MongoDB(host="localhost", port=27017, database="dependency_inversion")
 
    manejador = ManejadorDatos()
    manejador.procesar(mysql_db)
    manejador.procesar(mongodb_db)