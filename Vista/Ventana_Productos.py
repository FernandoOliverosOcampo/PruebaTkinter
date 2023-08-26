import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry

class Ventana_Registro_Productos(tk.Toplevel):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
        self.Decorar_Ventana()
        self.actualizar_tabla()
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
        self.Tabla_datos()
        # NOMBRE
        self.label_nombre = Label(self, text="Nombre Producto: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.label_nombre.pack(anchor="w", padx=118)
        self.txt_nombre = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_nombre.pack(pady=5, anchor="w", padx=120)

        # PRECIO
        self.lbl_precio = Label(self, text="Precio:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_precio.place(x=468,y=290)
        self.txt_precio = Entry(self, width=29, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_precio.place(x=470,y=317)
        # STOCK
        self.lbl_stock = Label(self, text="Stock:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_stock.pack(anchor="w", padx=118)
        self.txt_stock = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_stock.pack(pady=5, anchor="w", padx=120)
         # DESCRIPCION
        self.label_descripcion = Label(self, text="Descripcion: ", font=('MS Reference Sans Serif', 10, 'bold'), bg="white")
        self.label_descripcion.pack(anchor="w", padx=118)
        self.txt_descripcion = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_descripcion.pack(pady=5, anchor="w", padx=120)
        # FECHA
        self.lbl_fecha = Label(self, text="Fecha:", bg='white', font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_fecha.place(x=468,y=348)  
        self.calendar = DateEntry(self, width=27, height=4,font=('MS Reference Sans Serif', 11)) 
        self.calendar.config(headersbackground='#364c55', headersforeground="#fff", background="#fff", foreground="#000")
        self.calendar.place(x=470,y=372)
        
        # BOTON
        self.btn_update = Button(self, text="Actualizar", font=("MS Reference Sans Serif", 10, "bold"), width=15, height=1, bg="#ea1608", fg="white")
        self.btn_update.pack(padx=80 ,side="left")
        self.btn_registrar = Button(self, text="Registrar", bg="#ea1608", font=('MS Reference Sans Serif', 10, 'bold'), width=15, height=1, fg='white', command=self.registrar_productos)
        self.btn_registrar.pack(padx=80, side="left")
        self.btn_eliminar = Button(self, text="Eliminar", width=15, height=1, font=("MS Reference Sans Serif", 10, "bold"), fg="white", bg="#ea1608")
        self.btn_eliminar.pack(padx=80, side="right")


    def Tabla_datos(self):
        self.lista = ttk.Treeview(self, columns=(1,2,3,4,5,6), show="headings", height="5")
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure("Treeview.Heading", background="#ea1608", relief="flat", foreground="white", font=('MS Reference Sans Serif',10, 'bold'))
        self.lista.heading(1,text="Id")
        self.lista.heading(2, text="Nombre producto")
        self.lista.heading(3, text="Descripcion")
        self.lista.heading(4, text="Precio producto")
        self.lista.heading(5, text="Marca")
        self.lista.heading(6, text="Fecha")
        self.lista.column(1, width=30, anchor=CENTER)
        self.lista.column(2, width=200, anchor=CENTER)
        self.lista.column(3, width=200, anchor=CENTER)
        self.lista.column(4, width=200, anchor=CENTER)
        self.lista.column(5, width=100, anchor=CENTER)
        self.lista.column(6, width=100, anchor=CENTER)
        self.lista.pack(pady=10)
        
    def registrar_productos(self):
        nombre = self.txt_nombre.get()
        descripcion = self.txt_descripcion.get()
        stock = self.txt_stock.get()
        precio = self.txt_precio.get()
        fecha = self.calendar.get_date()
        
        if nombre and descripcion and stock and precio:
            if self.controlador.insertar_producto(nombre, descripcion, stock, precio, fecha):
                messagebox.showinfo(title="Exito", message="Datos del producto ingresado con exito")
                self.actualizar_tabla()
            else:
                messagebox.showerror(title="Error!", message="No se pudieron ingresar los datos")
        else:
            messagebox.showwarning(title="Verificación", message="Por favor rellene los campos y verifiquen que no estén vacios")

    def actualizar_tabla(self):
        self.lista.delete(*self.lista.get_children())
        productos = self.controlador.obtener_productos()
        for producto in productos:
            self.lista.insert("", "end", values=producto)