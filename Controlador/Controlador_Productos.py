from Modelo.Modelo_Productos import Modelo
import tkinter as tk
from Vista.Ventana_Productos import Ventana_Registro_Productos

class Controlador_productos:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo()
        self.vista = Ventana_Registro_Productos(self.root, self)

    def insertar_producto(self, nombre, descripcion, stock, precio, fecha):
        return self.modelo.insertar_producto(nombre, descripcion, stock, precio, fecha)

    def obtener_productos(self):
        return self.modelo.obtener_productos()

    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()