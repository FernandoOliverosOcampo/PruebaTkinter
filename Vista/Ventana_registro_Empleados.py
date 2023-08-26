import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Controlador.Controlador_update import Controlador_update
from Controlador.Controlador_delete import Controlador_eliminar

class Registro_Datos_Empleados(tk.Toplevel):
    def __init__(self,root, controlador):
        super().__init__(root)
        self.root = root
        self.controlador = controlador
        self.Imagen_Ventana()
        self.Decoracion_Ventana()
        self.Actualizar_Tabla() 
        self.grab_set()#bloquea la ventana  
        self.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.mainloop()

    def Decoracion_Ventana(self):
        self.title("Registro de empleados")
        self.iconbitmap("imagenes/F1.ico")
        self.config(bg="white")
        self.resizable(0,0)
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
            self.background_img = ImageTk.PhotoImage(self.bg)
            self.lbl_imagen = tk.Label(self, image=self.background_img,bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("Error al cargar la imagen:", e)

    def Elementos_ventana(self):
        # TITULO
        self.label_titulo = Label(self, text="Registro de usuarios", bg="white", font=("MS Reference Sans Serif", 15, 'bold'))
        self.label_titulo.pack(pady=10)
        #TABLA
        self.Tabla_datos()
        # NOMBRE
        self.label_nombre = Label(self, text="Nombre Completo: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.label_nombre.pack(anchor="w", padx=118)
        self.txt_nombre = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_nombre.pack(pady=5, anchor="w", padx=120)
        # CORREO
        self.label_correo = Label(self, text="Correo electronico: ", font=('MS Reference Sans Serif', 10, 'bold'), bg="white")
        self.label_correo.pack(anchor="w", padx=118)
        self.txt_correo = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief='groove', bg="#f7f9fc")
        self.txt_correo.pack(pady=5, anchor="w", padx=120)
        # NUMERO
        self.lbl_numero = Label(self, text="Numero de telefono:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_numero.place(x=468,y=310)
        self.txt_numero = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_numero.place(x=470,y=338)
        # TRABAJO
        self.lbl_trabajos = Label(self, text="Trabajo a cargo:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_trabajos.pack(anchor="w", padx=118)
        self.list_trabajo = ttk.Combobox(self, width=35, height=3,font=('MS Reference Sans Serif', 10))
        self.list_trabajo.state(["readonly"])
        self.list_trabajo.pack(pady=5, anchor="w", padx=120)
        self.list_trabajo['values'] = self.controlador.datos_combo_trabajo()
        # GENERO
        self.lbl_genero = Label(self, text="Genero:", bg='white', font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_genero.place(x=468,y=368)
        self.list_genero = ttk.Combobox(self, width=35, height=2, font=('MS Reference Sans Serif', 10))
        self.list_genero.state(["readonly"])
        self.list_genero.place(x=470,y=393)
        self.list_genero['values'] = self.controlador.datos_combo_genero()
        
        # BOTON
        self.btn_update = Button(self, text="Actualizar", font=("MS Reference Sans Serif", 10, "bold"), width=15, height=1, bg="#ea1608", fg="white", command=self.ventana_update)
        self.btn_update.pack(padx=80 ,side="left")
        self.btn_registrar = Button(self, text="Registrar", bg="#ea1608", font=('MS Reference Sans Serif', 10, 'bold'), width=15, height=1, fg='white', command=self.Registrar_Empleado)
        self.btn_registrar.pack(padx=80, side="left")
        self.btn_eliminar = Button(self, text="Eliminar", width=15, height=1, font=("MS Reference Sans Serif", 10, "bold"), fg="white", bg="#ea1608", command=self.ventana_eliminar)
        self.btn_eliminar.pack(padx=80, side="right")


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
        self.lista.column(2, width=220)
        self.lista.column(3, width=200)
        self.lista.column(4, width=200)
        self.lista.column(5, width=100)
        self.lista.column(6, width=100)
        self.lista.pack(pady=10)

    def cerrar(self):
        self.grab_release()  
        self.destroy() 


    def Registrar_Empleado(self):
        nombre = self.txt_nombre.get()
        correo = self.txt_correo.get()
        numero = self.txt_numero.get()
        trabajo = self.list_trabajo.get()
        genero = self.list_genero.get()

        if nombre and correo and numero and trabajo and genero:
            if self.controlador.insertar_empleados(nombre, correo, numero, trabajo, genero):
                messagebox.showinfo(title="Correcto!", message="El empleado fue ingresado correctamente")
                self.Actualizar_Tabla()
            else:
                messagebox.showerror(title="Error!", message="Hubo un error al ingresar el empleado")
               
        else:
            messagebox.showwarning(title="Verificación", message="Por favor rellene los campos y verifiquen que no estén vacios")

    def Actualizar_Tabla(self):
        self.lista.delete(*self.lista.get_children())  
        empleados = self.controlador.retorno_elementos() 
        for empleado in empleados:
            self.lista.insert('', 'end', values=empleado)

    def ventana_update(self):
        ventana = Controlador_update(self.root)

    def ventana_eliminar(self):
        ventana =  Controlador_eliminar(self.root)