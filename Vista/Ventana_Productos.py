import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk

class Ventana_Registro_Productos(tk.Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.Decorar_Ventana()
        self.mainloop()

    def Decorar_Ventana(self):
        self.title("Registro de productos")
        self.iconbitmap("imagenes/F1.ico")
        self.resizable(0,0)
        self.config(bg="white")
        self.Imagen_ventana()
        self.Elementos_Ventana()
        self.Dimensiones_Ventana()

    def Dimensiones_Ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 600
        wventana = 900

        pwidht = round(wtotal/2 -wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidht)+"+"+str(pheight))

    def Imagen_ventana(self):
        try:
            self.imagen = Image.open("imagenes/descarga1.png")
            self.background = ImageTk.PhotoImage(self.imagen)
            self.label_imagen = Label(self, image=self.background, bg="white")
            self.label_imagen.pack()
        except Exception as e:
            print("El error se encuentra en: ", e)

    def Elementos_Ventana(self):
        self.lbl_titulo = Label(self, text="Registro de productos", bg="white", font=('MS Reference Sans Serif', 15, 'bold')).pack()