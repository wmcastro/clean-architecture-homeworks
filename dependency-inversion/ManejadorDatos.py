class ManejadorDatos:
    def procesar(self, base_datos):
        base_datos.guardar("Guardando datos")
        datos_leidos = base_datos.leer()
        print("Datos leídos:", datos_leidos)