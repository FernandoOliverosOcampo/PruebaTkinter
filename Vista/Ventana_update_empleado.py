import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Ventana_Update(tk.Toplevel):
    def __init__(self, root, controlador):
        super().__init__(root)
        self.root = root  # Almacena la referencia al objeto Toplevel
        self.controlador = controlador
        self.Imagen_Ventana_Update()
        self.grab_set()
        self.Decorar_ventana()
        self.protocol("WM_DELETE_WINDOW", self.Cerrar)
        self.mainloop()

    def Decorar_ventana(self):
        self.title("Actualizar empleado")
        self.iconbitmap("imagenes/F1.ico")
        self.config(bg="white")
        self.resizable(0,0)
        self.Dimensiones_Ventana()
        self.Elementos_ventana()
    def Cerrar(self):
        self.grab_release()
        self.destroy()

    def Imagen_Ventana_Update(self):
        try:
            self.imagen = Image.open("imagenes/descarga1.png")
            self.background = ImageTk.PhotoImage(self.imagen)
            self.lbl_imagen = Label(self, image=self.background,bg="white")
            self.lbl_imagen.pack()
        except Exception as e:
            print("El error se encuentra en: ", e)

    def Dimensiones_Ventana(self):
        htotal = self.winfo_screenheight()
        wtotal = self.winfo_screenwidth()

        hventana = 400
        wventana = 900

        pwidth = round(wtotal/2 - wventana/2)
        pheight = round(htotal/2 - hventana/2)

        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def Elementos_ventana(self):
        # TITULO
        self.label_titulo = Label(self, text="Actualizar usuarios", bg="white", font=("MS Reference Sans Serif", 15, 'bold'))
        self.label_titulo.pack(pady=10)
        #ID
        self.lbl_id = Label(self, text="Id: ", bg="white", font=("MS Reference Sans Serif", 10, "bold"))
        self.lbl_id.pack(anchor="w", padx=118)
        self.combo_id = ttk.Combobox(self, width=35, height=2, font=('MS Reference Sans Serif', 10), justify="left",background="white")
        self.combo_id.state(["readonly"])
        self.combo_id['values']=self.controlador.combo_id()
        self.combo_id.pack(anchor="w",padx=120,pady=5)
        
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
        self.lbl_numero.place(x=467,y=162)
        self.txt_numero = Entry(self, width=30, font=('MS Reference Sans Serif', 11), relief="groove", bg="#f7f9fc")
        self.txt_numero.place(x=470,y=188)
        # TRABAJO
        self.lbl_trabajos = Label(self, text="Trabajo a cargo:", bg="white", font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_trabajos.place(x=467,y=272)
        self.list_trabajo = ttk.Combobox(self, width=35, height=3,font=('MS Reference Sans Serif', 10))
        self.list_trabajo.state(["readonly"])
        self.list_trabajo.place(x=470,y=297)
        self.list_trabajo['values'] = self.controlador.combo_trabajo()
        # GENERO
        self.lbl_genero = Label(self, text="Genero:", bg='white', font=('MS Reference Sans Serif', 10, 'bold'))
        self.lbl_genero.place(x=467,y=217)
        self.list_genero = ttk.Combobox(self, width=35, height=2, font=('MS Reference Sans Serif', 10))
        self.list_genero.state(["readonly"])
        self.list_genero.place(x=470,y=242)
        self.list_genero['values'] = self.controlador.combo_genero()
        
        # BOTON
        self.btn_update = Button(self, text="Actualizar", font=("MS Reference Sans Serif", 10, "bold"), width=15, height=1, bg="#ea1608", fg="white", command=self.Actualizar_Datos )
        self.btn_update.pack(side="bottom", pady=15)
    
#CONEXION A BD
    def Actualizar_Datos(self):
        id = self.combo_id.get()
        nombre = self.txt_nombre.get()
        correo = self.txt_correo.get()
        numero = self.txt_numero.get()
        trabajo = self.list_trabajo.get()
        genero = self.list_genero.get()
      
        if len(id) !=0 and len(nombre) != 0 and len(correo) != 0 and len(numero) != 0 and len(trabajo)!=0 and len(genero) !=0:
            try:
                self.controlador.actualizar_empleado(nombre, correo, numero, trabajo, genero, id)
                messagebox.showinfo(title="Datos actualizados", message="Los datos fueron actualizados correctamente")
                self.destroy()
                
            except Exception as e:
                messagebox.showerror(title="Error!", message="No se pudieron actualizar los datos")
                print("El error esta en: ", e)
        else:
            messagebox.showerror(title="Error!", message="Los campos estan vacios")
    
    
