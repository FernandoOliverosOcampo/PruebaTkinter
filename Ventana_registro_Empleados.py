import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import pymysql

class Registro_Datos_Empleados():
    def __init__(self):
        self.root = tk.Tk()
        self.Decoracion_Ventana()
        self.root.mainloop()
        
     

    def Decoracion_Ventana(self):
        self.root.title("Registro de empleados")
        self.root.iconbitmap("imagenes/icon.ico")
        self.root.config(bg="white")
        self.Dimensiones_Ventana()
       
        self.Elementos_ventana()

    def Dimensiones_Ventana(self):
        htotal = self.root.winfo_screenheight()
        wtotal = self.root.winfo_screenwidth()

        hventana = 600
        wventana = 900

        pwidht = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidht)+"+"+str(pheight))

    def Elementos_ventana(self):
        # TITULO
        self.label_titulo = Label(self.root, text="Registro de usuarios", bg="white", font=("MS Reference Sans Serif", 15, 'bold'))
        self.label_titulo.pack(pady=10)
        # NOMBRE
        self.label_nombre = Label(self.root, text="Nombre Completo: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.label_nombre.pack(anchor="w", padx=28)
        self.txt_nombre = Entry(self.root, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_nombre.pack(pady=5, anchor="w", padx=30)
        # CORREO
        self.label_correo = Label(self.root, text="Correo electronico: ", font=('MS Reference Sans Serif', 10, 'bold'), bg="white")
        self.label_correo.pack(anchor="w", padx=28)
        self.txt_correo = Entry(self.root, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_correo.pack(pady=5, anchor="w", padx=30)
        # NUMERO
        self.lbl_numero = Label(self.root, text="Numero de telefono:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_numero.pack(anchor="w", padx=28)
        self.txt_numero = Entry(self.root, width=30, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_numero.pack(pady=5, anchor="w", padx=30)
        # TRABAJO
        self.lbl_trabajos = Label(self.root, text="Trabajo a cargo:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_trabajos.pack(anchor="w", padx=28)
        self.list_trabajo = ttk.Combobox(self.root, width=35, height=2,font=('MS Reference Sans Serif', 10))
        self.list_trabajo.pack(pady=5, anchor="w", padx=30)
        self.opciones = ["Ingeniero", "Secretaria", "Doctor"]
        self.list_trabajo['values'] = self.opciones
        # GENERO
        self.lbl_genero = Label(self.root, text="Genero:", bg='white', font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_genero.pack(anchor="w", padx=28)
        self.list_genero = ttk.Combobox(self.root, width=35, height=2, font=('MS Reference Sans Serif', 10))
        self.list_genero.pack(anchor="w", padx=30, pady=5)
        self.opciones_genero = ["Mujer", "Hombre", "Otro"]
        self.list_genero['values'] = self.opciones_genero
        # BOTON
        self.btn_registrar = Button(self.root, text="Registrar", bg="blue", font=('MS Reference Sans Serif', 10), width=15, height=1, fg='white', command=self.Registrar_Empleado)
        self.btn_registrar.pack(pady=15, side="bottom")

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
                self.root.destroy()

            except Exception as e:
                messagebox.showerror(title="Error!!!", message="Error en la conexion")
                print("error en: ", e)
        else:
            messagebox.showerror(title="Error!!!", message="Los campos estan vacios, por favor llenelos")
