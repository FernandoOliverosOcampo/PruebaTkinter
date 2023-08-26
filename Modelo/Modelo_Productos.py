import pymysql

class Modelo:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        self.cursor = self.conexion.cursor()
    def insertar_producto(self, nombre, descripcion, stock, precio, fecha):
        try:
            query = "INSERT INTO productos (Nombre_producto, Descripcion, Precio_producto, Marca_producto, Fecha_producto) VALUES (%s, %s, %s, %s, %s)"
            datos = (nombre, descripcion, precio, stock, fecha)
            self.cursor.execute(query, datos)
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error en la inserción:", e)
            return False

    def obtener_productos(self):
        try:
            sql = "SELECT * FROM productos"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        
        except Exception as e:
            print("Error al obtener productos:", e)
            return []

    def cerrar_conexion(self):
        self.conexion.close()