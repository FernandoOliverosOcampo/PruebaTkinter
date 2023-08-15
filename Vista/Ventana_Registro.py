import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from imagenes import *

class Ventana_Registro_Vista(tk.Toplevel):

    def __init__(self,root):
        super().__init__(root)
        self.configurar_ventana()
        self.Elementos_Ventana()
        self.ventana_bonita()

    def configurar_ventana(self):
        self.title("Registro de usuario") #Aplica un titulo a la ventana
        self.resizable(0,0)  #Evita que se pueda redimensionar la ventana
        self.iconbitmap("imagenes/F1.ico")
        self.dimensiones_ventana()

    def dimensiones_ventana(self):
             # Tamaño de la pantalla
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()
        # tamaño de la ventana
        hventana = 500
        wventana = 400
        # Calculo
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        # Geometria de la ventana
        self.geometry(str(wventana)+"x"+str(hventana) + "+"+str(pwidth)+"+"+str(pheight))

    def Elementos_Ventana(self):
        try:
            self.bg = Image.open("imagenes/descarga1.png")
            # new_width = 400  # Nuevo ancho en píxeles
            # new_height = 300  # Nuevo alto en píxeles
            # self.bg = self.bg.resize((new_width, new_height),Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(self.bg)
            self.lbl_imagen = Label(self, image=self.background_img,bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("Error al cargar la imagen:", e)
            
    def ventana_bonita(self):
        self.config(bg="white")
        self.lblTitulo = Label(self, text="Registro de usuarios", font=('MS Reference Sans Serif', '15', 'bold'), bg="white")
        self.lblTitulo.pack(pady=10)
        self.lbl_nombre = Label(self, text="Nombre: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_nombre.pack(anchor="w", padx=50)
        self.txt_nombre = Entry(self, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12))
        self.txt_nombre.pack(pady=10)
        self.lbl_usuario = Label(self, text="Usuario: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_usuario.pack(anchor="w", padx=50)
        self.txt_usuario = Entry(self, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12))
        self.txt_usuario.pack(pady=10)

        self.lbl_contraseña = Label(self, text="Contraseña: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_contraseña.pack(anchor="w", padx=50)
        self.txt_contraseña = Entry(self, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif', 12), show="*")
        self.txt_contraseña.pack(pady=10)
        #regresar
      
        self.b1 = Button(self, text="Registrate", width=10, height=1, background="#ea1608", fg="white", font=('MS Reference Sans Serif', 11,'bold'),command=self.registrar_usuario)
        self.b1.pack(padx=10)
    
    def registrar_usuario(self):
        nombre = self.txt_nombre.get()
        usuario = self.txt_usuario.get()
        contraseña = self.txt_contraseña.get()
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