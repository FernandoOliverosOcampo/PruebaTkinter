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
            query ="DELETE FROM empleados WHERE id=%s"
            data = (id_empleado)
            self.cursor.execute(query, data)
            self.conexion.commit()
        except Exception as e:
            print("El error esta en: ", e)

    def cerrar_conexion(self):
        self.conexion.close()