import pymysql

class Modelo_delete:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"

        )
        self.cursor = self.conexion.cursor()

    def eliminar_empleado(self, id_empleado):
        try:
            query ="DELETE FROM empleados WHERE Nombre_completo=%s"
            data = (id_empleado)
            self.cursor.execute(query, data)
            self.conexion.commit()
        except Exception as e:
            print("El error esta en: ", e)

    def mostrar_empleados(self):
        try:
            query = "SELECT Nombre_completo FROM empleados"
            self.cursor.execute(query)
            data = []
            for row in self.cursor:
                data.append(row[0])
            return(data)
        except Exception as e:
            print("El error esta en: ", e)

    def cerrar_conexion(self):
        self.conexion.close()