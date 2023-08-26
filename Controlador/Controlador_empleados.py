from Vista.Ventana_registro_Empleados import Registro_Datos_Empleados
from Modelo.Modelo_empleados import Modelo
import tkinter as tk

class Controlador_empleados:
    def __init__(self, root):
        self.root = root
        self.modelo = Modelo()
        self.vista = Registro_Datos_Empleados(self.root, self)

    def insertar_empleados(self, nombre, correo, numero, trabajo, genero):
        return self.modelo.registrar_empleados(nombre, correo, numero, trabajo, genero)
    
    def datos_combo_genero(self):
        return self.modelo.datos_combo_genero()
    
    def datos_combo_trabajo(self):
        return self.modelo.datos_combo_trabajo()
    
    def retorno_elementos(self):
        return self.modelo.retorno_elementos()
    
    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
    
