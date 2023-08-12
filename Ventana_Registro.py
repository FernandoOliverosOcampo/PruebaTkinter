from tkinter import *
import tkinter as tk

class Ventana_registro():
    def __init__(self):
        self.root = tk.Tk()
        self.Configurar_Ventana()
        self.Decoracion_Ventana()
        self.Elementos_Ventana()
        self.root.mainloop()
        
    def Configurar_Ventana(self):
        #Tamaño de la pantalla
        htotal = self.root.winfo_screenheight()
        wtotal = self.root.winfo_screenwidth()
        #tamaño de la ventana
        hventana = 400
        wventana = 400
        #Calculo
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        #Geometria de la ventana
        self.root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    def Decoracion_Ventana(self):
        self.root.title("Registro usuarios")
        self.root.config(background="white")
        self.root.resizable(0,0)

    def Elementos_Ventana(self):
        #txt
        self.lblTitulo = Label(self.root, text="Registro de usuarios", font=('MS Reference Sans Serif', '15', 'bold'), bg="white").pack(pady=10)

        self.lbl_nombre = Label(self.root, text="Nombre: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold')).pack(anchor="w",padx=50)
        self.txt_nombre = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif',12)).pack(pady=10)

        self.lbl_usuario = Label(self.root, text="Usuario: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold')).pack(anchor="w",padx=50)
        self.txt_usuario = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif',12)).pack(pady=10)

        self.lbl_contraseña = Label(self.root, text="Contraseña: ", bg="white", font=('MS Reference Sans Serif', 10, 'bold')).pack(anchor="w",padx=50)
        self.txt_contraseña = Entry(self.root, relief="groove", bg="#f7f9fc", width=30, font=('MS Reference Sans Serif',12),show="*").pack(pady=10)
        #Botones
        self.btnFrame = Frame(self.root, background="white")  
        self.btnFrame.pack(pady=10)
        self.btn_registrar = Button(self.btnFrame, text="Registrate", width=10, height=1, background="blue",fg="white",font=('MS Reference Sans Serif', 11 )).pack(padx=10)

        self.btn_prueba = Button(self.root, text="preud", command=self.prueba_boton).pack()
        
    def prueba_boton(self):
        print("hollaaa")