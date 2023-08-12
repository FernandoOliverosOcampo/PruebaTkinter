import pymysql
from tkinter import messagebox
from Ventana_Registro import Ventana_registro

class Conexion_Bd():
    def __init__(self):
        self.view = Ventana_registro()
        self.view.btn_registrar.config(self.registro_usuarios)

    def registro_usuarios(self):
       
        bd=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        
        if len(self.view.txt_nombre.get()) !=0 and len(self.view.txt_usuario.get())  !=0  and len(self.view.txt_contraseña.get()) !=0 :
            fcursor= bd.cursor()
            sql="INSERT INTO usuario (nombre, usuario, contrasena) VALUES ('{0}','{1}','{2}')".format(self.view.txt_nombre.get(),self.view.txt_usuario.get(),self.view.txt_contraseña.get())

            try:
                fcursor.execute(sql)
                bd.commit()
                messagebox.showinfo(message="Registro exitoso", title="Aviso")
            except:
                bd.rollback
                messagebox.showinfo(message="registro anulado", title="aviso")
        else: 
            messagebox.showinfo(title="Error", message="Los campos no pueden estar vacio")