import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
import pymysql

class Ventana_Registro_Productos(tk.Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.Decorar_Ventana()
        self.grab_set()#bloquea la ventana  
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.mainloop()

    def Decorar_Ventana(self):
        self.title("Registro de productos")
        self.iconbitmap("imagenes/F1.ico")
        self.resizable(0,0)
        self.config(bg="white")
        self.Imagen_ventana()
        self.Elementos_Ventana()
        self.Tabla_datos()
        self.Dimensiones_Ventana()

    def Dimensiones_Ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 600
        wventana = 900

        pwidht = round(wtotal/2 -wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidht)+"+"+str(pheight))

    def Imagen_ventana(self):
        try:
            self.imagen = Image.open("imagenes/descarga1.png")
            self.background = ImageTk.PhotoImage(self.imagen)
            self.label_imagen = Label(self, image=self.background, bg="white")
            self.label_imagen.pack()
        except Exception as e:
            print("El error se encuentra en: ", e)
            
    def cerrar(self):
        self.grab_release()  
        self.destroy() 

    def Elementos_Ventana(self):
        self.lbl_titulo = Label(self, text="Registro de productos", bg="white", font=('MS Reference Sans Serif', 15, 'bold')).pack()


    def Tabla_datos(self):
        self.lista = ttk.Treeview(self, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview.Heading", background="#ea1608", relief="flat", foreground="white", font=('MS Reference Sans Serif',10, 'bold'))
        self.lista.heading(1,text="Id")
        self.lista.heading(2, text="Nombre")
        self.lista.heading(3, text="Correo electronico")
        self.lista.heading(4, text="Numero de telefono")
        self.lista.heading(5, text="Trabajo")
        self.lista.heading(6, text="Genero")
        self.lista.column(1, width=30, anchor=CENTER)
        self.lista.column(2, width=200, anchor=CENTER)
        self.lista.column(3, width=200, anchor=CENTER)
        self.lista.column(4, width=200, anchor=CENTER)
        self.lista.column(5, width=100, anchor=CENTER)
        self.lista.column(6, width=100, anchor=CENTER)


        #Muestra los datos        
        elementos = self.Retorno_de_elementos()
        for i in elementos:
            self.lista.insert('','end', values=i)
        self.lista.pack(pady=10)
        
    def Retorno_de_elementos(self):
        try: 
            conexion = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                db="bd_prueba"
            )
            cursor = conexion.cursor()
            sql = "SELECT * FROM empleados"
            cursor.execute(sql)
            return cursor.fetchall()

        except Exception as e:
            print("Error en la conexion, se encuentra en", e)