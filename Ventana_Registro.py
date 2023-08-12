import tkinter as tk
from tkinter import *
import pymysql
from tkinter import messagebox


class Ventana_registro_Datos():

    def __init__(self):
        self.root = tk.Tk()
        self.Configurar_Ventana()
        self.Decoracion_Ventana()
        self.Elementos_Ventana()

    def Configurar_Ventana(self):
        # Tamaño de la pantalla
        htotal = self.root.winfo_screenheight()
        wtotal = self.root.winfo_screenwidth()
        # tamaño de la ventana
        hventana = 400
        wventana = 400
        # Calculo
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        # Geometria de la ventana
        self.root.geometry(str(wventana)+"x"+str(hventana) +
                           "+"+str(pwidth)+"+"+str(pheight))

    def Decoracion_Ventana(self):
        self.root.title("Registro usuarios")
        self.root.config(background="white")
        self.root.resizable(0, 0)

    def Elementos_Ventana(self):
        # titulo
        self.lblTitulo = Label(self.root, text="Registro de usuarios", font=('MS Reference Sans Serif', '15', 'bold'), bg="white")
        self.lblTitulo.pack(pady=10)
        #nombre
        self.lbl_nombre = Label(self.root, text="Nombre: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_nombre.pack(anchor="w", padx=50)
        self.txt_nombre = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12))
        self.txt_nombre.pack(pady=10)
        #usuario
        self.lbl_usuario = Label(self.root, text="Usuario: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_usuario.pack(anchor="w", padx=50)
        self.txt_usuario = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12))
        self.txt_usuario.pack(pady=10)
        #contraseña
        self.lbl_contraseña = Label(self.root, text="Contraseña: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_contraseña.pack(anchor="w", padx=50)
        self.txt_contraseña = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12), show="*")
        self.txt_contraseña.pack(pady=10)
        #boton
        self.b1 = Button(self.root, text="Registrate", width=10, height=1, background="blue", fg="white", font=('MS Reference Sans Serif', 11))
        self.b1.pack(padx=10)

    # def registrar_usuario(self):
    #     nombre = self.txt_nombre.get()
    #     usuario = self.txt_usuario.get()
    #     contraseña = self.txt_contraseña.get()
    #     # Realizar la conexión a la base de datos
        
    #     if len(nombre) !=0 and len(usuario)  !=0  and len(contraseña)!=0 :
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

    #             messagebox.showinfo(message="Usuario registrado con éxito.", title="Exito")

    #         except:
    #             messagebox.showerror(message="Error al registrar el usuario:",title="Error")
    #     else:
    #         messagebox.showerror(message="Verifique que los campos esten llenos", title="Campos vacios")