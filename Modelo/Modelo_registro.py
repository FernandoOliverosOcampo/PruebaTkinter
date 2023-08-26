import pymysql

class Modelo_registro:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        self.cursor = self.conexion.cursor()
    def registrar_usuario(self, nombre, usuario, contraseña):
        try: 
            query = "INSERT INTO usuario (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
            datos = (nombre, usuario, contraseña)
            self.cursor.execute(query, datos)
            self.conexion.commit()
            return True
        except Exception as e:
            print("El error esta en: ", e)
            return False

    def cerrar_conexion(self):
        self.conexion.close()
