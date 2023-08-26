from Modelo.Modelo_inicio_sesion import Modelo_inicio
from Vista.ventana_principal import Ventana
import tkinter as tk

class Controlador_inicio_sesion:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = Modelo_inicio()
        self.vista = Ventana(self.root, self)

    def iniciar_sesion(self, usuario, contraseña):
        return self.modelo.iniciar_sesion(usuario, contraseña)
    
    def cerrar_conexion(self):
        return self.modelo.cerrar_conexion()
