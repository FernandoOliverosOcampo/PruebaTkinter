import tkinter as tk
from tkinter import *

class Ventana_Menu():
    def __init__(self):
        self.root = tk.Tk()
        self.Detalles_Ventana()

    def Detalles_Ventana(self):
        self.root.title("Menu Principal")
        self.root.iconbitmap(
            r'C:\Users\ferni\Downloads\Datos\Documentos\Fercho\Python\Practica tkinter\icon.ico')
        self.root.state('zoomed')
        self.root.resizable(0,0)
        self.Dimensiones_Ventana()
        self.root.config(background="white")
    def Dimensiones_Ventana(self):
       #tamaño de la patalla
       wtotal = self.root.winfo_screenwidth()
       htotal = self.root.winfo_screenheight()
       #valores
       wventana = wtotal
       hventana = htotal 
       self.root.geometry(str(wventana)+"x"+str(hventana)+"+0+0")
       
    