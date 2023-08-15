from tkinter import *
from PIL import Image, ImageTk
from Ventana_registro_Empleados import Registro_Datos_Empleados

class Ventana_Menu():
    def __init__(self):
        self.root = Tk()
        self.Elementos_Ventana()
        self.Detalles_Ventana()
        self.Menu()
        self.root.mainloop()

    def Detalles_Ventana(self):
        self.root.title("Menu Principal")
        self.root.iconbitmap("imagenes/icon.ico")
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

    def Elementos_Ventana(self):
        try:
            self.bg = Image.open("imagenes/descarga.png")
            # new_width = 400  # Nuevo ancho en píxeles
            # new_height = 300  # Nuevo alto en píxeles
            # self.bg = self.bg.resize((new_width, new_height),Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(self.bg)
            self.lbl_imagen = Label(self.root, image=self.background_img)
            self.lbl_imagen.pack()
        except Exception as e:
            print("Error al cargar la imagen:", e)

    def Menu(self):
        #configurar menu
        menu = Menu(self.root)
        self.root.config(menu=menu)
        #Añadir los items
        filemenu = Menu(menu, tearoff=0)
        editmenu = Menu(menu,tearoff=0)
        helpmenu = Menu(menu, tearoff=0)
        exitmenu = Menu(menu, tearoff=0)
        subopciones = Menu(menu, tearoff=0)

        menu.add_cascade(label="Archivo", menu=filemenu)
        menu.add_cascade(label="Editar", menu=editmenu)
        menu.add_cascade(label="Ayuda", menu=helpmenu)
        menu.add_cascade(label="Cerrar", menu=exitmenu)

        #subopciones
        
        subopciones.add_command(label="Registro empleados", command=Registro_Datos_Empleados)
        subopciones.add_command(label="registro datos")

        #cascada de los items
        filemenu.add_cascade(label="Registro", menu=subopciones)

        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de ...")

        exitmenu.add_command(label="Salir",command=self.root.quit)
 


