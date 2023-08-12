import tkinter as tk
from tkinter import *
from conexionbd import funcionPrueba
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
        htotal = self.root.winfo_screenwidth()
        # Tamaño de la ventana
        wventana = 500
        hventana = 300
        # Calculamos la posición
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2.5-hventana/1)
        # Se aplica al la geometria de la ventana
        self.root.geometry(str(wventana)+"x"+str(hventana) +
                           "+"+str(pwidth)+"+"+str(pheight))

    def DecoracionVentana(self):
        self.root.title("Ventana prueba")
        self.root.config(bg="white")
        self.root.iconbitmap(
            r'C:\Users\ferni\Downloads\Datos\Documentos\Fercho\Python\Practica tkinter\icon.ico')
        self.root.resizable(0, 0)

    def ElementosVentana(self):
        #TITULO
        self.lblTitulo = Label(self.root, text="Inicio de sesión", background="white", font=('Roboto','15','bold')).pack(pady=15)
      
        #USUARIO
        self.lblUsuario = Label(self.root, text="Usuario", background="white",font=('Roboto','10','bold')).pack()
        self.lblUsuario.grid(row=1, column=2)
        self.txtUsuario = Entry(self.root,relief="solid",width=30,justify="left", font=('Roboto', 12 )).pack(pady=5)
      
        #CONTRASEÑA
        self.lblTitulo = Label(self.root, text="Contraseña", background="white", font=('Roboto','10','bold')).pack()
        self.txtContraseña = Entry(self.root,relief="solid",width=30,justify="left",font=('Roboto', 12 )).pack(pady=10)
        #BOTONES
        self.btnFrame = Frame(self.root, background="white")  
        self.btnFrame.pack()

        self.btnIngresar = Button(self.btnFrame, text="Ingresar", width=10, height=1, background="blue", fg="white", command=funcionPrueba ).pack(padx=10,side="left")
        self.btnRegistrar = Button(self.btnFrame, text="Registrate", width=10, height=1, background="blue", fg="white").pack(padx=10,side="left")
        
        
        
Ventana()
