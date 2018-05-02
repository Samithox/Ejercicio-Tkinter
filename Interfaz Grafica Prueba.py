import tkinter
from tkinter import *

#Metodos:
def mostrar(ventana):
	ventana.deiconify()

def ocultar(ventana):
	ventana.withdraw()	

def ejecutar(f):
	vPrincipal.after(200,f)

def imprimir(texto):
	print (texto)	

def cambiar_stringvar(nuevotexto,stringvar):
 	stringvar.set(nuevotexto)

def limpiar():
	textoentradaRut.set("")
	textoentradaNombre.set("")
	textoentradaApellido.set("")

def limpiar2():
	textoRut.set("")
	textoNombre.set("")
	textoApellido.set("")

#Ventana principal:
vPrincipal = Tk()
vPrincipal.config(bg="white")
vPrincipal.config(bg="white")
vPrincipal.title("Mi primera App grafica")#Titulo de la pantalla
vPrincipal.geometry("500x500+400+100") #Las medidas de la ventana
vPrincipal.maxsize(750,600) #Setear el maximo tamaño que puede tener la ventana
vPrincipal.minsize(500,500) #Setear tamaño minimo de la ventana
vPrincipal.resizable(width=False, height=False)#Para bloquear si agrando o achico la pantalla

textoRut=StringVar()
textoNombre=StringVar()
textoApellido=StringVar()
textoentradaRut=StringVar()
textoentradaNombre=StringVar()
textoentradaApellido=StringVar()

cuaVer= Frame(vPrincipal,width = 4, height=300,bg="Black" ).place(x=248,y=0)
cuaHor= Frame(vPrincipal,width = 500, height=4,bg="Black" ).place(x=0,y=300)
#Botones Ventana Principal:
bAbr2=Button(vPrincipal,text="Abrir ven 2",command=lambda:ejecutar(mostrar(v2)) or ocultar(vPrincipal)).place(x=180,y=470)

bCerrvP=Button(vPrincipal,text="Salir",command=vPrincipal.destroy).place(x=250,y=470)

#Entrys Ventana Principal:


#Labels Ventana Principal:

	#Lebels Izquierda:
lrut=Label(vPrincipal,text="Rut:",bg="white").place(x=0,y=0)
lnombres=Label(vPrincipal,text="Nombres:",bg="white").place(x=0,y=20)
lapellidos=Label(vPrincipal,text="Apellidos:",bg="white").place(x=0,y=40)
	#Entrys entrada Izquierda:
EnRut=Entry(vPrincipal,textvar=textoentradaRut).place(x=60,y=0)
EnNombre=Entry(vPrincipal,textvar=textoentradaNombre).place(x=60,y=20)
EnApellido=Entry(vPrincipal,textvar=textoentradaApellido).place(x=60,y=40)

bGuardar=Button(vPrincipal,text="Guardar",command=lambda:cambiar_stringvar(textoentradaRut.get(),textoRut) or cambiar_stringvar(textoentradaNombre.get(),textoNombre) or cambiar_stringvar(textoentradaApellido.get(),textoApellido ))
bGuardar.place(x=70,y=250)
bLimpiar=Button(vPrincipal,text="Limpiar",command=limpiar)
bLimpiar.place(x=125,y=250)
	#Lebels Derecha:
lrut=Label(vPrincipal,text="Rut:",bg="white").place(x=258,y=0)
lnombres=Label(vPrincipal,text="Nombres:",bg="white").place(x=258,y=20)
lapellidos=Label(vPrincipal,text="Apellidos:",bg="white").place(x=258,y=40)
	#Labels receptores derecha:
labelRut=Label(vPrincipal,textvar=textoRut,bg="white",relief="groove",width = 10, height=1).place(x=320,y=0)
labelNombre=Label(vPrincipal,textvar=textoNombre,bg="white",relief="groove",width = 15, height=1).place(x=320,y=20)
labelApellido=Label(vPrincipal,textvar=textoApellido,bg="white",relief="groove",width = 15, height=1).place(x=320,y=40)

bLimpiar2=Button(vPrincipal,text="Limpiar",command=limpiar2)
bLimpiar2.place(x=325,y=250)

#Ventana Secundaria:
v2=Toplevel(vPrincipal)
v2.config(bg="white")
v2.title("Ventana Secundaria")
v2.geometry("500x500+400+100")

#Botones Ventana Secundaria:
bCerr2=Button(v2,text="Volver",command=lambda:ejecutar(ocultar(v2)) or mostrar(vPrincipal)).place(x=220,y=470)




v2.withdraw()
vPrincipal.mainloop()