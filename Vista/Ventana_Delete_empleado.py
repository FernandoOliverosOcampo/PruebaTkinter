import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

class Ventana_Borrar(tk.Toplevel):
    def __init__(self,root, controlador):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
        self.Decorar_Ventana()
        self.grab_set()
        self.protocol("WV_DELETE_WINDOW",self.cerrar)

    def Decorar_Ventana(self):
        self.config(bg="white")
        self.title("Borrar empleado")
        self.iconbitmap("imagenes/F1.ico")
        self.Dimensiones_ventana()
        self.Imagen_Ventana()
        self.Elementos_Ventana()

    def Dimensiones_ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 400
        wventana = 500

        pwidth = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
    def cerrar(self):
        self.grab_release()
        self.destroy()
    def Imagen_Ventana(self):
        try:
            self.imagen = Image.open("imagenes/descarga1.png")
            self.background = ImageTk.PhotoImage(self.imagen)
            self.lbl_imagen = Label(self, image=self.background, bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("El error esta en: ", e)

    def Elementos_Ventana(self):
        self.lbl_titulo = Label(self, text="Borrar Empleado", font=("MS Reference Sans Serif", 15, 'bold'), bg="white")
        self.lbl_titulo.pack()
        self.lbl_contenido = Label(self, text="Para borrar el empleado debe ingresar el id", bg="white", font=("MS Reference Sans Serif", 10, 'bold'))
        self.lbl_contenido.pack(pady=15)
        self.lbl_titulo_id = Label(self, text="ID:",bg="white", font=("MS Reference Sans Serif", 10, 'bold'))
        self.lbl_titulo_id.pack(pady=5)
        self.txt_id = Entry(self, bg="#f7f9fc", font=("MS Reference Sans Serif", 10))
        self.txt_id.pack(pady=15)
        self.btn_eliminar = Button(self, text="Eliminar", width=15, height=1,font=("MS Reference Sans Serif", 10, 'bold'),fg="white", bg="#ea1608", command=self.Eliminar_Empleado)
        self.btn_eliminar.pack(pady=15)

    def Eliminar_Empleado(self):
        id_empleado = self.txt_id.get()
        if len(id_empleado)!=0:
            try:
                self.controlador.eliminar_empleado(id_empleado)
                messagebox.showinfo(title="Registro eliminado",message="El registro fue eliminado satisfactoriamente")
                self.destroy()
            except Exception as e:
                messagebox.showerror(title="Error!", message="No se pudo eliminar el registro")
                print("El error esta en:",e)
        else:
            messagebox.showwarning(title="Verificación", message="El campo a eliminar esta vacio")
            