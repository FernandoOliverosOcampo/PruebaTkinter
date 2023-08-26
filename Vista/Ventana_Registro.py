import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from imagenes import *

class Ventana_Registro_Vista(tk.Toplevel):

    def __init__(self,root,controlador):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
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
        self.b1 = Button(self, text="Registrate", width=15, height=1, background="#ea1608", fg="white", font=('MS Reference Sans Serif', 10,'bold'),command=self.registrar_usuario)
        self.b1.pack(padx=10)
    
    def registrar_usuario(self):
        nombre = self.txt_nombre.get()
        usuario = self.txt_usuario.get()
        contraseña = self.txt_contraseña.get()

        if nombre and usuario and contraseña:
            if self.controlador.registrar_usuarios(nombre, usuario, contraseña):
                messagebox.showinfo(title="Confirmación", message="El usuario fue ingresado satisfactoriamente")
            else:
                messagebox.showerror(title="Error!",message="Hubo un error")
        else:
            messagebox.showwarning(title="verificación", message="Los campos estan vacios, verifique que cada campo este lleno por favor")
        