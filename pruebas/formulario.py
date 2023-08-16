import tkinter as tk

class VentanaFormulario(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Ventana Formulario")
        
        self.imagen_formulario = tk.PhotoImage(file="imagenes/descarga.png")
        
        self.label_imagen = tk.Label(self, image=self.imagen_formulario)
        self.label_imagen.pack()
        
        # Aquí puedes agregar los elementos de tu formulario
