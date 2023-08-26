import pymysql

class Modelo_inicio:
    def __init__(self):
        self.conexion  = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"

        )
        self.cursor = self.conexion.cursor()

    def iniciar_sesion(self, usuario, contraseña):
        try:
            query = "SELECT contraseña FROM usuario WHERE usuario = %s and contraseña=%s"
            data =(usuario, contraseña)
            self.cursor.execute(query, data) 
            return self.cursor.fetchall() 
        except Exception as e:
            print("El error esta en: ", e)
    def cerrar_conexion(self):
        self.conexion.close()