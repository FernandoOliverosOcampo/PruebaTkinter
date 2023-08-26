from Vista.Ventana_Ventas import Ventana_ventas

class Controlador_Ventas:
    def __init__(self, root):
        self.root = root
        self.vista = Ventana_ventas(self.root, self)
    