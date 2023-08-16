import tkinter as tk
from formulario import VentanaFormulario

class VentanaMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        
        self.imagen_principal = tk.PhotoImage(file="imagenes/descarga.png")
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.menu.add_command(label="Abrir Formulario", command=self.abrir_formulario)
        
        self.label_imagen_principal = tk.Label(self.root, image=self.imagen_principal)
        self.label_imagen_principal.pack()
        
    def abrir_formulario(self):
        ventana_formulario = VentanaFormulario(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaMenu(root)
    root.mainloop()
