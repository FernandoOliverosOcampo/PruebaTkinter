from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Ventana_ventas(tk.Toplevel):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
        self.Decorar_ventana()
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cerrar)

    def Decorar_ventana(self):
        self.title("Ventana ventas")
        self.iconbitmap("imagenes/F1.ico")
        self.resizable(0,0)
        self.config(bg="white")
        self.Dimensiones_ventana()
        self.Imagen_ventana()

    def Dimensiones_ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 650
        wventana = 1000

        pwidth = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def Imagen_ventana(self):
        try:
            self.imagen = Image.open("imagenes/descarga1.png")
            self.background = ImageTk.PhotoImage(self.imagen)
            self.lbl_imagen = Label(self, image=self.background, bg="white")
            self.lbl_imagen.pack(pady=10)
        except Exception as e:
            print("El error esta en: ",e)
    def cerrar(self):
        self.grab_release()
        self.destroy()