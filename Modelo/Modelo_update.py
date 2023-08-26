import pymysql

class Modelo_update:
    def __init__(self):
        self.conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"

        )
        self.cursor = self.conexion.cursor()

    def actualizar_empleado(self, nombre, correo, numero, trabajo, genero, id):
        try:
            query ="UPDATE empleados SET Nombre_completo = %s, Correo_electronico = %s, Numero_Telefono = %s, Trabajo_cargo = %s, Genero = %s WHERE id = %s"
            data =(nombre, correo, numero, trabajo, genero, id)
            self.cursor.execute(query, data)
            self.conexion.commit()
        except Exception as e:
            print("El error esta en: ", e)

    def Datos_Combo_Id(self):
        try:
           query="SELECT id FROM empleados"
           self.cursor.execute(query)
           data=[]
           for rows in self.cursor:
                data.append(rows[0])
           return(data)
                    
        except Exception as e:
           print("El error esta en:", e)

    def Datos_Combo_Trabajo(self):
        try:
           query="SELECT trabajo FROM trabajo"
           self.cursor.execute(query)
           data=[]
           for rows in self.cursor:
                data.append(rows[0])
           return(data)
                    
        except Exception as e:
           print("El error esta en:", e)

    def Datos_Combo_Genero(self):
        try:
           query="SELECT genero FROM genero"
           self.cursor.execute(query)
           data=[]
           for rows in self.cursor:
               data.append(rows[0])
           return(data)
        except Exception as e:
            print("El error esta en: ", e)

    def cerrar_conexion(self):
        self.conexion.close()
        