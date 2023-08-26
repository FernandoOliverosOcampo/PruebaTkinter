from tkinter import *
from PIL import Image, ImageTk
from Vista.Ventana_registro_Empleados import Registro_Datos_Empleados
from Vista.Ventana_update_empleado import Ventana_Update
from Vista.Ventana_Delete_empleado import Ventana_Borrar
from Controlador.Controlador_Productos import Controlador_productos
from Controlador.Controlador_empleados import Controlador_empleados
class Ventana_Menu():
    def __init__(self):
        self.root = Tk()
        self.Elementos_Ventana()
        self.Menu()
        self.Detalles_Ventana()
        self.root.mainloop()

    def Detalles_Ventana(self):
        self.root.title("Menu Principal")
        self.root.iconbitmap("imagenes/F1.ico")
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
            self.lbl_imagen = Label(self.root, image=self.background_img,bg="white")
            self.lbl_imagen.place(x=570, y=200)
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
        subopciones_registro = Menu(menu, tearoff=0)


        menu.add_cascade(label="Registro", menu=filemenu)
        menu.add_cascade(label="Ventas", menu=editmenu)
        menu.add_cascade(label="Ayuda", menu=helpmenu)
        menu.add_cascade(label="Cerrar", menu=exitmenu)

        #subopciones
        
        subopciones.add_command(label="Registro empleados", command=self.ventana_empleado)
        subopciones.add_command(label="Registro productos", command=self.ventana_producto)
        subopciones_registro.add_command(label="Actualizar empleados", command=self.ventana_update)
        subopciones_registro.add_command(label="Actualizar productos", command=self.ventana_update)


        #cascada de los items
        filemenu.add_cascade(label="Registro", menu=subopciones)
        filemenu.add_cascade(label="Actualizar", menu=subopciones_registro)

        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de ...")

        exitmenu.add_command(label="Salir",command=self.root.quit)
 

    #VENTANAS MENU
    def ventana_empleado(self):
        registro = Controlador_empleados(self.root)
    def ventana_producto(self):
        producto = self.controlador = Controlador_productos(self.root)
    def ventana_update(self):
        update = Ventana_Update(self.root, self)
    def ventana_borrar(self):
        borrar = Ventana_Borrar(self.root, self)
    