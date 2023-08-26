from Modelo.Modelo_registro import Modelo_registro
from Vista.Ventana_Registro import Ventana_Registro_Vista
import tkinter as tk

class Controlador_registro:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo_registro()
        self.vista = Ventana_Registro_Vista(self.root, self)
 
    def registrar_usuarios(self, nombre, usuario, contraseña):
        return self.modelo.registrar_usuario(nombre, usuario, contraseña)
    
    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()