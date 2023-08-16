import tkinter as tk
from tkinter import *
from Vista.Ventana_Registro import Ventana_Registro_Vista
from Vista.Ventana_Menu import Ventana_Menu
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk
# --------VENTANA-----------

class Ventana():
    def __init__(self):
        self.root = tk.Tk()
        self.DecoracionVentana()
        self.ConfigurarVentana()
        self.Elementos_Ventana()
        self.ElementosVentana()
        self.root.mainloop()

    def ConfigurarVentana(self):
        # Tomamos el ancho de la ventana
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        # Tamaño de la ventana
        wventana = 500
        hventana = 370
        # Calculamos la posición
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        # Se aplica al la geometria de la ventana
        self.root.geometry(str(wventana)+"x"+str(hventana) + "+"+str(pwidth)+"+"+str(pheight))

    def DecoracionVentana(self):
        self.root.title("Ventana prueba")
        self.root.config(bg="white")
        self.root.iconbitmap("imagenes/F1.ico")
        self.root.resizable(0, 0)
        

    def Elementos_Ventana(self):
        try:
            self.bg = Image.open("imagenes/descarga1.png")
            # new_width = 400  # Nuevo ancho en píxeles
            # new_height = 300  # Nuevo alto en píxeles
            # self.bg = self.bg.resize((new_width, new_height),Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(self.bg)
            self.lbl_imagen = Label(self.root, image=self.background_img,bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("Error al cargar la imagen:", e)


    def ElementosVentana(self):
        #TITULO
        self.lbl_titulo = Label(self.root, text="INICIO DE SESIÓN", background="white", font=('MS Reference Sans Serif','15','bold'))
        self.lbl_titulo.pack(pady=15)
      
        #USUARIO
        self.lbl_usuario = Label(self.root, text="Usuario: ", background="white",font=('MS Reference Sans Serif','10','bold'))
        self.lbl_usuario.pack(anchor="w",padx=100)
        self.txt_usuario = Entry(self.root,relief="sunken",bg="#f7f9fc",width=30,justify="left", font=('MS Reference Sans Serif', 12 ))
        self.txt_usuario.pack(pady=5)
      
        #CONTRASEÑA
        self.lbl_contraseña = Label(self.root, text="Contraseña:", background="white", font=('MS Reference Sans Serif','10','bold'))
        self.lbl_contraseña.pack(anchor="w",padx=100)

        self.txt_contraseña = Entry(self.root, relief="sunken", bg="#f7f9fc",width=30, justify="left",font=('MS Reference Sans Serif', 12 ),show="*")
        self.txt_contraseña.pack(pady=10)
        #BOTONES
        self.btnFrame = Frame(self.root, background="white")  
        self.btnFrame.pack(pady=10)

        self.btn_ingresar = Button(self.btnFrame, text="Ingresar", width=15, height=1, background="#ea1608",  activebackground="red",fg="white", font=('MS Reference Sans Serif', 10,'bold' ), command=self.inicio_de_sesion )
        self.btn_ingresar.pack(padx=10,side="left")
        self.btn_registrar = Button(self.btnFrame, text="Registrate", width=15, height=1, background="#ea1608", command=self.Abrir_Registro,fg="white",font=('MS Reference Sans Serif', 10, 'bold'))
        self.btn_registrar.pack(padx=10,side="left")
    
    def inicio_de_sesion(self):
        usuario = self.txt_usuario.get()
        contraseña = self.txt_contraseña.get()

        if len(usuario) !=0 and len(contraseña) !=0:
           conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
            )
           cursor = conexion.cursor()
           cursor.execute("SELECT contraseña FROM usuario WHERE usuario='"+usuario+"' and contraseña='"+contraseña+"'")

           if cursor.fetchall():
                messagebox.showinfo(title="Inicio de sesión", message="Inicio de sesión correcto")
                self.root.destroy()
                Ventana_Menu()
           else:
                messagebox.showerror(title="Error!",message="Usuario y contraseña incorrectos")
           conexion.close()
        else:
            messagebox.showerror(message="Error al ingresar, los campos estan vacios", title="Error!")

    def Abrir_Registro(self):
        Ventana_Registro_Vista(self.root)
       