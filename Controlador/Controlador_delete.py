from Modelo.Modelo_delete import Modelo_delete
from Vista.Ventana_Delete_empleado import Ventana_Borrar
import tkinter as tk

class Controlador_eliminar:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo_delete()
        self.vista = Ventana_Borrar(self.root, self)

    def eliminar_empleado(self, id_empleado):
        return self.modelo.eliminar_empleado(id_empleado)
    
    def cerrar_conexion(self):
        return self.modelo.cerrar_conexion()