# - - - - - - - - Importar Libreria Tkinter - - - - - - - - - - 
from tkinter import *
from tkinter import messagebox
import prueba
import os

 # Identificador de la app frente a windows
try:
    from ctypes import windll

    myappid="fronteraenergy.ca"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

#Variable para rutas relativas para iconos e imagenes
basedir=os.path.dirname(__file__) #obtiene la ruta de este archivo

# ----------------------------- Configuración de la raiz -----------------------------
raiz=Tk()
raiz.title("Interfaz cuestionario descuento tributario") #Titulo
raiz.resizable(True,True) #Redimencionable alto y ancho
raiz.iconbitmap( os.path.join(basedir, "IconoFE.ico") ) #icono
#raiz.geometry("650x350") #se le da tamaño al frame, ya que la raiz se adapta
raiz.config(width=500, height=400, bg="#833177") #Color de fondo
raiz.config(bd=5)
#raiz.config(relief="groove")

# --------------- Funcion frame principal ------------------
def Frame_principal():
    #bandera bandF_principal=+1
    #Creacion del frame
    miFrame=Frame() 
    miFrame.grid(row=3)

    miFrame.config(bg="white") #Color de frame
    miFrame.config(width="650", height="350") #Tamaño de frame
    miFrame.config(bd=8) #Grosor de borde
    miFrame.config(relief="groove") #Tipo de borde
    #miFrame.config(cursor="pirate") #mouse diferente
    #print(str(bandF_principal))
    #return(1)

# ------- funcion volver --------
def volver():
    raiz.iconify()
    raiz.deiconify()

def hola1():
    print("Hola 1")
    return(1)

def hola2():
    print("Hola 2")
    return(2)

# ---------------- Funcion Frame G&A -----------------------
def FrameGyA():
    FrameGyA=Tk()
    FrameGyA.title("Costo G&A")
    FrameGyA.iconbitmap(os.path.join(basedir, "IconoFE.ico"))

    barraMenu=Menu(FrameGyA) #creacion objeto menu
    FrameGyA.config(menu=barraMenu)

     #Creacion pestañas
    archivoVolver=Menu(barraMenu, tearoff=0)
    archivoVolver.add_command(label="Mostrar Menu", command=volver)
    
     #mostrar pestañas
    barraMenu.add_cascade(label="Volver", menu=archivoVolver)

    frame=Frame(FrameGyA)
    frame.grid(row=2)
    #Label(frame, text="Hola", width=50, height=50).grid(row=0)

    Pregunta=Label(frame, text="Elije el tipo de transacción", width=20, height=10).grid(row=0, column=2)
    
    #checkbutton
    compra=IntVar()
    servicio=IntVar()
    def o():
        valC=compra.get()
        valS=servicio.get()
        print("valC ", valC, "  -  valS ", valS)

    def opc_transaccion():
        opc_escojida="valor: "
        if(compra.get()==1):
            opc_escojida+=" compra"
            print(opc_escojida)
        
        if(servicio.get()==1):
            opc_escojida+=" servicio"
            print(opc_escojida)

        textFinal.config(text=opc_escojida)

    Checkbutton(frame, text="Compra", variable=compra, onvalue=1, offvalue=0, command=opc_transaccion).grid(row=1, column=0)
    Checkbutton(frame, text="Servicio", variable=servicio, onvalue=1, offvalue=0, command=opc_transaccion).grid(row=1, column=3)
    #BCompra=Button(frame, text="Compra", command=hola1, padx=0.5, pady=0.5).grid(row=1, column=0)
    #Bservicio=Button(frame, text="Servicio", command=hola2, padx=0.5, pady=0.5).grid(row=1, column=3)
    B_transaccion=Button(frame, text="Enviar", command=o).grid(row=2)
    
    textFinal=Label(frame)
    textFinal.grid(row=4)
    
     #condicional esconder raiz
    if(FrameGyA):
        raiz.withdraw()

    FrameGyA.mainloop()

# ---------------- Funcion Frame OPEX -----------------------
def FrameOPEX():
    FrameOPEX=Tk()
    FrameOPEX.title("Costo OPEX")
    FrameOPEX.mainloop()

# ---------------- Funcion Frame CAPEX -----------------------
def FrameCAPEX():
    FrameCAPEX=Tk()
    FrameCAPEX.title("Costo CAPEX")
    FrameCAPEX.mainloop()

# -------- funcion Salir App -------
def Salir():
    Respuesta=messagebox.askquestion("salir", "¿Deseas salir de la aplicación?")
    if Respuesta=="yes":
        #FrameGyA.destroy()
        raiz.destroy()

# ---------------- Mensaje Informacion --------------------
def informacion():
    messagebox.showinfo("Area Impuestos 2023", "Software Descuento Tributario")

# ---------------- Mensaje Reporte Error -----------------
def R_error():
    messagebox.showinfo("Area Impuestos 2023", "Enviar un correo a: javendano@fronteraenergy.ca")

#------------------------------- Menú -------------------------------
barraMenu=Menu(raiz) #creacion objeto menu
raiz.config(menu=barraMenu)

    #Creacion pestañas
archivoTcosto=Menu(barraMenu, tearoff=0)
archivoTcosto.add_command(label="G&A", command=FrameGyA)
archivoTcosto.add_command(label="OPEX", command=FrameOPEX)
archivoTcosto.add_command(label="CAPEX", command=FrameCAPEX)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_cascade(label="Empresa")
archivoAyuda.add_cascade(label="Licencia", command=informacion)
archivoAyuda.add_separator() #Separador estetico
archivoAyuda.add_cascade(label="Reportar error", command=R_error)

archivosalida=Menu(barraMenu, tearoff=0)
archivosalida.add_command(label="Salir", command=Salir)

 #Mostrar pestañas
barraMenu.add_cascade(label="Tipo Costo", menu=archivoTcosto)
barraMenu.add_cascade(label="Acerca de...", menu=archivoAyuda)
barraMenu.add_cascade(label="Salir", menu=archivosalida)

# ------------------------- Fin Menu -------------------------------

# ------------------------- Diseño raiz ---------------------------

img_bienvenida=PhotoImage(file=os.path.join(basedir, "Frontera_Bienvenida.PNG") )
imgzoom=img_bienvenida.subsample(8)
Label(raiz, image=imgzoom, padx=0.5, pady=0.5).grid(row=0, column=0) #pack()
D_trib = Label(raiz, text="", bg="#833177")
D_trib.grid(row=1, column=0)
# Botones raiz
#nombreboton=button("padre", text="texto de boton", command=funcion).grid("posiciones en grilla")
B_Frame_principal = Button(raiz, text="Mostrar Frame_principal", command=Frame_principal).grid(row=2, column=0, sticky=SE)  #place(relx=0 , rely=0.5)
B_Frame2 = Button(raiz, text="Mostrar Frame #2", command=FrameGyA).grid(row=2, column=0, sticky=SW) #place(relx=0.5 , rely=0.5)

prueba.pru()

#Bucle de la ventana
raiz.mainloop()
