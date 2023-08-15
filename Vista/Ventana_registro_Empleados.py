import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk

class Registro_Datos_Empleados(tk.Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.Imagen_Ventana()
        self.Decoracion_Ventana()
        self.mainloop()
        
    def Decoracion_Ventana(self):
        self.title("Registro de empleados")
        self.iconbitmap("imagenes/icon.ico")
        self.config(bg="white")
        self.Dimensiones_Ventana()
        self.Elementos_ventana()

    def Dimensiones_Ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 600
        wventana = 900

        pwidht = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidht)+"+"+str(pheight))

    def Imagen_Ventana(self):
        try:
            self.bg = Image.open("imagenes/descarga1.png")
            # new_width = 400  # Nuevo ancho en píxeles
            # new_height = 300  # Nuevo alto en píxeles
            # self.bg = self.bg.resize((new_width, new_height),Image.LANCZOS)
            self.background_img = ImageTk.PhotoImage(self.bg)
            self.lbl_imagen = tk.Label(self, image=self.background_img,bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("Error al cargar la imagen:", e)

    def Elementos_ventana(self):
        # TITULO
        self.label_titulo = Label(self, text="Registro de usuarios", bg="white", font=("MS Reference Sans Serif", 15, 'bold'))
        self.label_titulo.pack(pady=10)
        # NOMBRE
        self.label_nombre = Label(self, text="Nombre Completo: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.label_nombre.pack(anchor="w", padx=28)
        self.txt_nombre = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_nombre.pack(pady=5, anchor="w", padx=30)
        # CORREO
        self.label_correo = Label(self, text="Correo electronico: ", font=('MS Reference Sans Serif', 10, 'bold'), bg="white")
        self.label_correo.pack(anchor="w", padx=28)
        self.txt_correo = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_correo.pack(pady=5, anchor="w", padx=30)
        # NUMERO
        self.lbl_numero = Label(self, text="Numero de telefono:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_numero.pack(anchor="w", padx=28)
        self.txt_numero = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_numero.pack(pady=5, anchor="w", padx=30)
        # TRABAJO
        self.lbl_trabajos = Label(self, text="Trabajo a cargo:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_trabajos.pack(anchor="w", padx=28)
        self.list_trabajo = ttk.Combobox(self, width=35, height=3,font=('MS Reference Sans Serif', 10))
        self.list_trabajo.pack(pady=5, anchor="w", padx=30)
        self.list_trabajo['values'] = self.Datos_Combo_Trabajo()
        # GENERO
        self.lbl_genero = Label(self, text="Genero:", bg='white', font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_genero.pack(anchor="w", padx=28)
        self.list_genero = ttk.Combobox(self, width=35, height=2, font=('MS Reference Sans Serif', 10))
        self.list_genero.pack(anchor="w", padx=30, pady=5)
        self.list_genero['values'] = self.Datos_Combo_Genero()
        
        # BOTON
        self.btn_registrar = Button(self, text="Registrar", bg="blue", font=('MS Reference Sans Serif', 10), width=15, height=1, fg='white', command=self.Registrar_Empleado)
        self.btn_registrar.pack(pady=15, side="bottom")

#CONEXION DE LA BASE DE DATOS
    def Datos_Combo_Trabajo(self):
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        try:
           cursor = conexion.cursor()
           query="SELECT trabajo FROM trabajo"
           cursor.execute(query)
           data=[]
           for rows in cursor:
                data.append(rows[0])
           return(data)
                    
        except Exception as e:
           print("El error esta en:", e)

    def Datos_Combo_Genero(self):
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="bd_prueba"
        )
        try:
           cursor = conexion.cursor()
           query="SELECT genero FROM genero"
           cursor.execute(query)
           data=[]
           for rows in cursor:
               data.append(rows[0])
           return(data)
        except Exception as e:
            print("El error esta en: ", e)

    def Registrar_Empleado(self):
        nombre = self.txt_nombre.get()
        correo = self.txt_correo.get()
        numero = self.txt_numero.get()
        trabajo = self.list_trabajo.get()
        genero = self.list_genero.get()

        if len(nombre) != 0 and len(correo) != 0 and len(numero) != 0 and len(trabajo)!=0 and len(genero) !=0:
            try:
                conexion = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="",
                    db="bd_prueba"
                )
                cursor = conexion.cursor()
                query = "INSERT INTO empleados (Nombre_completo, Correo_electronico, Numero_Telefono, Trabajo_cargo, Genero) VALUES (%s, %s, %s, %s, %s)"
                datos = (nombre, correo, numero, trabajo, genero)
                cursor.execute(query, datos)
                conexion.commit()
                conexion.close()
                messagebox.showinfo(title="Datos insertados", message="Los datos fueron ingresados exitosamente")
                

            except Exception as e:
                messagebox.showerror(title="Error!!!", message="Error en la conexion")
                print("error en: ", e)
        else:
            messagebox.showerror(title="Error!!!", message="Los campos estan vacios, por favor llenelos")
    

    