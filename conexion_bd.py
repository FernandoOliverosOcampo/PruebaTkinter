from Ventana_Registro import Ventana_Registro_Vista
import tkinter as tk
from tkinter import messagebox
import pymysql

class Ventana_Registro_Controlador():
    def __init__(self):
        self.view = Ventana_Registro_Vista()
        self.view.b1.config(command= self.registrar_usuario)

    def registrar_usuario(self):
        nombre = self.view.txt_nombre.get()
        usuario = self.view.txt_usuario.get()
        contraseña = self.view.txt_contraseña.get()
        # Realizar la conexión a la base de datos
        
        if len(nombre) !=0 and len(usuario)  !=0  and len(contraseña)!=0 :
            try:
                conexion = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    db="bd_prueba"
                )
                cursor = conexion.cursor()
                # Insertar los datos en la tabla
                query = "INSERT INTO usuario (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
                datos = (nombre, usuario, contraseña)
                cursor.execute(query, datos)

                # Confirmar y cerrar la conexión
                conexion.commit()
                conexion.close()

                messagebox.showinfo(message="Usuario registrado con éxito.", title="Exito")

            except:
                messagebox.showerror(message="Error al registrar el usuario:",title="Error")
        else:
            messagebox.showerror(message="Verifique que los campos esten llenos", title="Campos vacios")


   



























# import pymysql
# import tkinter as tk
# from tkinter import messagebox
# from Ventana_Registro import Ventana_registro_Datos

# class Registro_Controlador():
#     def __init__(self):
#         self.view = Ventana_registro_Datos()
#         self.view.b1.config(self.registrar_usuario)
        
#     def registrar_usuario(self):
#         nombre = self.view.txt_nombre.get()
#         usuario = self.view.txt_usuario.get()
#         contraseña = self.view.txt_contraseña.get()
#         try:
#             conexion = pymysql.connect(
#                 host="localhost",
#                 user="root",
#                 password="",
#                 db="bd_prueba"
#             )

#             cursor = conexion.cursor()

#             # Insertar los datos en la tabla
#             query = "INSERT INTO usuario (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
#             datos = (nombre, usuario, contraseña)
#             cursor.execute(query, datos)

#             # Confirmar y cerrar la conexión
#             conexion.commit()
#             conexion.close()

#             print("Usuario registrado con éxito.")

#         except:
#             print("Error al registrar el usuario:")

#     # def registro_usuarios(self):
        # nombre = self.view.txt_nombre.get()
        # usuario = self.view.txt_usuario.get()
        # contraseña = self.txt_contraseña.get()

        # bd=pymysql.connect(
        #     host="localhost",
        #     user="root",
        #     password="",
        #     db="bd_prueba"
        # )
        # fcursor= bd.cursor()

        # if len(nombre) !=0 and len(usuario)  !=0  and len(contraseña)!=0 :
            
        #     sql="INSERT INTO usuario (nombre, usuario, contrasena) VALUES ('{0}','{1}','{2}')".format(nombre, usuario,contraseña)

        #     try:
        #         fcursor.execute(sql)
        #         bd.commit()
        #         messagebox.showinfo(message="Registro exitoso", title="Aviso")
        #     except:
        #         bd.rollback()
        #         messagebox.showinfo(message="registro anulado", title="aviso")
        #     finally:
        #         fcursor.close()
        #         bd.close()
        # else: 
        #     messagebox.showinfo(title="Error", message="Los campos no pueden estar vacio")