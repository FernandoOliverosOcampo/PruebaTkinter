import pymysql

class Modelo():
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        self.cursor = self.conexion.cursor()

    def registrar_empleados(self, nombre, correo, numero, trabajo, genero):
        try:
            query = "INSERT INTO empleados (Nombre_completo, Correo_electronico, Numero_Telefono, Trabajo_cargo, Genero) VALUES (%s, %s, %s, %s, %s)"
            datos = (nombre, correo, numero, trabajo, genero)
            self.cursor.execute(query, datos)
            self.conexion.commit()
            return True
        except Exception as e:
            print("El error esta en: ", e)
            return False

    def datos_combo_genero(self):
        try:
           query="SELECT genero FROM genero"
           self.cursor.execute(query)
           data=[]
           for rows in self.cursor:
               data.append(rows[0])
           return(data)
        except Exception as e:
            print("El error esta en: ", e)

    def datos_combo_trabajo(self):
        try:
           query="SELECT trabajo FROM trabajo"
           self.cursor.execute(query)
           data=[]
           for rows in self.cursor:
               data.append(rows[0])
           return(data)
        except Exception as e:
            print("El error esta en: ", e)

    def retorno_elementos(self):
        try:
            sql = "SELECT * FROM empleados"
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        except Exception as e:
            print("Error en la conexion, se encuentra en", e)
            return []
        
    def cerrar_conexion(self):
        self.conexion.close()