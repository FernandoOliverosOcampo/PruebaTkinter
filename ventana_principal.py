import tkinter as tk
from tkinter import *
from Ventana_Registro import *
# --------VENTANA-----------

class Ventana():
    def __init__(self):
        self.root = tk.Tk()
        self.DecoracionVentana()
        self.ConfigurarVentana()
        self.ElementosVentana()
        self.root.mainloop()

    def ConfigurarVentana(self):
        # Tomamos el ancho de la ventana
        wtotal = self.root.winfo_screenwidth()
        htotal = self.root.winfo_screenheight()
        # Tamaño de la ventana
        wventana = 500
        hventana = 300
        # Calculamos la posición
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        # Se aplica al la geometria de la ventana
        self.root.geometry(str(wventana)+"x"+str(hventana) + "+"+str(pwidth)+"+"+str(pheight))

    def DecoracionVentana(self):
        self.root.title("Ventana prueba")
        self.root.config(bg="white")
        self.root.iconbitmap(
            r'C:\Users\ferni\Downloads\Datos\Documentos\Fercho\Python\Practica tkinter\icon.ico')
        self.root.resizable(0, 0)

    def ElementosVentana(self):
        #TITULO
        self.lblTitulo = Label(self.root, text="INICIO DE SESIÓN", background="white", font=('MS Reference Sans Serif','15','bold')).pack(pady=15)
      
        #USUARIO
        self.lblUsuario = Label(self.root, text="Usuario: ", background="white",font=('MS Reference Sans Serif','10','bold')).pack(anchor="w",padx=100)
        self.txtUsuario = Entry(self.root,relief="sunken",bg="#f7f9fc",width=30,justify="left", font=('MS Reference Sans Serif', 12 )).pack(pady=5)
      
        #CONTRASEÑA
        self.lblContraseña = Label(self.root, text="Contraseña:", background="white", font=('MS Reference Sans Serif','10','bold')).pack(anchor="w",padx=100)
        self.txtContraseña = Entry(self.root, relief="sunken", bg="#f7f9fc",width=30, justify="left",font=('MS Reference Sans Serif', 12 ),show="*").pack(pady=10)
        #BOTONES
        self.btnFrame = Frame(self.root, background="white")  
        self.btnFrame.pack(pady=10)

        self.btnIngresar = Button(self.btnFrame, text="Ingresar", width=10, height=1, background="blue", fg="white", font=('MS Reference Sans Serif', 11, ) ).pack(padx=10,side="left")
        self.btnRegistrar = Button(self.btnFrame, text="Registrate", width=10, height=1, background="blue", command=Ventana_Registro_Vista,fg="white",font=('MS Reference Sans Serif', 11 )).pack(padx=10,side="left")
