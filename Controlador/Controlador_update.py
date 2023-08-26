import tkinter as tk
from Modelo.Modelo_update import Modelo_update
from Vista.Ventana_update_empleado import Ventana_Update

class Controlador_update:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo_update()
        self.vista = Ventana_Update(self.root, self)

    def actualizar_empleado(self, nombre, correo, numero, trabajo, genero, id):
        return self.modelo.actualizar_empleado(nombre,correo,numero, trabajo, genero, id)
    def combo_id(self):
        return self.modelo.Datos_Combo_Id()
    def combo_trabajo(self):
        return self.modelo.Datos_Combo_Trabajo()
    def combo_genero(self):
        return self.modelo.Datos_Combo_Genero()
    
    def cerrar_conexion(self):
        return self.modelo.cerrar_conexion()