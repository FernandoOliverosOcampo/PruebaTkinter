# from Ventana_Registro import Ventana_Registro_Vista
# import tkinter as tk
# from tkinter import messagebox
# import pymysql

# class Ventana_Registro_Controlador():
#     def __init__(self):
#         self.view = Ventana_Registro_Vista()

#         self.view.b1.config(command= self.registrar_usuario)

#     def registrar_usuario(self):
#         nombre = self.view.txt_nombre.get()
#         usuario = self.view.txt_usuario.get()
#         contraseña = self.view.txt_contraseña.get()
#         bd=pymysql.connect(
#             host="localhost",
#             user="root",
#             password="",
#             db="bd_prueba"
#         )
#         fcursor=bd.cursor()

#         if len(nombre) !=0 and len(usuario)  !=0  and len(contraseña)!=0:

        
#             sql="INSERT INTO usuario (nombre, usuario, contraseña) VALUES('{0}', '{1}','{2}')".format(nombre, usuario, contraseña)

#             try:
#                 fcursor.execute(sql)
#                 bd.commit()
#                 messagebox.showinfo(message="Registro exitoso", title="Aviso")
#                 self.ventana_principal()

#             except:
#                 bd.rollback
#                 messagebox.showinfo(message="Registro anulado", title="Aviso")    

#             bd.close()
#         else:
#             messagebox.showinfo(title="Error", message="Los campos no pueden estar vacio")


   