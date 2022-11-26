from tkinter import *

# FUNCIONES DE CONSULTAR 
def consultar():
    lblsaludar=Label(ventana,text="Bienvenido " + entradaNombre.get()
+ " \nSu cedula es: "
+ entradaCedula.get() + "\nUbicado en: " + entradaubicacion.get(),font=("Arial Black",10),bg="grey68").place(x=50,y=350)

def tipoVehiculo():
    s=selec.get() 
    l=entradaAlquiler.get() 
    horas=int(l)
    BOXER = horas*5000
    NS200  = horas*10000
    NKD125 = horas*9000
    DISCOVER125 =horas*8000 
    NMAX =horas*15000
    lblsaludar1=Label(ventana,text=" Escogiste la opción de la moto numero: "
+ str(s),font=("Arial Black",10),bg="grey68").place(x=50,y=420)
    

    if s==1:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la BOXER es de $5000"
+"\nEl total a pagar por su renta es de " + str(l)
+"Las horas de alquiler que desea la moto son:$"+str(BOXER),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=460)
    

    elif s==2:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NS200 es de $10000"
+"\nEl total a pagar por su renta es de " + str(l)
+"Las horas de alquiler que desea la moto son:$"+str(NS200),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=520)
        

    elif s==3:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NKD125 es de $9000"
+"\nEl total a pagar por su renta es de " + str(l)
+"Las horas de alquiler que desea la moto son:$"+str(NKD125),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=580)

    elif s==4:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la DISCOVER125 es de $8000"
+"\nEl total a pagar por su renta es de " + str(l)
+"Las horas de alquiler que desea la moto son:$"+str(DISCOVER125),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=640)

    else:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NMAX es de $15000"
+"\nEl total a pagar por su renta es de " + str(l)
+"Las horas de alquiler que desea la moto son:$"+str(NMAX),font=("Arial Black",10),bg="oliveDrab1").place(x=50,y=700)



#DIMENSIONES DE LA VENTANA
ventana=Tk() 
ventana.geometry("800x800")

# TITULO
ventana.title("AGUANCHA MOTOR ")

# ENTRADA DE DATOS DE LA PERSONA 
lblCedula=Label(text="Cedula:",font=("Adobe Gothic Std B",14),bg="oliveDrab1").place(x=10,y=10) 
entradaCedula=StringVar() 
txtCedula=Entry(ventana,textvariable=entradaCedula).place(x=115,y=15)

lblNombre=Label(text="Nombre:",font=("Adobe Gothic Std B",14),bg="oliveDrab1").place(x=10,y=40) 
entradaNombre=StringVar() 
txtNombre=Entry(ventana,textvariable=entradaNombre).place(x=115,y=50)
 
lblAlquiler=Label(text="¿Por cuantas horas va alquilar el vehiculo?:",font=("Adobe Gothic Std B",14),bg="oliveDrab1").place(x=10,y=100)
entradaAlquiler=IntVar() 
txtAlquiler=Entry(ventana,textvariable=entradaAlquiler).place(x=480,y=110)

lblUbicacion=Label(text="Ubicacion:",font=("Adobe Gothic Std B",14),bg="oliveDrab1").place(x=10,y=70) 
entradaubicacion=StringVar() 
txtUbicacion=Entry(ventana,textvariable=entradaubicacion).place(x=130,y=75)

# BOTONES DE LAS MOTOS 
selec=IntVar()

vehiculo1=Radiobutton(ventana,text="1. BOXER",value=1,
variable=selec,command=tipoVehiculo,font=("Adobe Gothic Std B",10)).place(x=100,y=140) 

vehiculo2=Radiobutton(ventana,text="2. NS200",value=2,
variable=selec,command=tipoVehiculo,font=("Adobe Gothic Std B",10)).place(x=100,y=160) 

vehiculo3=Radiobutton(ventana,text="3. NKD125",value=3,
variable=selec,command=tipoVehiculo,font=("Adobe Gothic Std B",10)).place(x=100,y=180) 

vehiculo4=Radiobutton(ventana,text="4. DISCOVER125",value=4,
variable=selec,command=tipoVehiculo,font=("Adobe Gothic Std B",10)).place(x=100,y=200) 

vehiculo5=Radiobutton(ventana,text="5. NMAX",value=5,
variable=selec,command=tipoVehiculo,font=("Adobe Gothic Std B",10)).place(x=100,y=220)

# IMAGENES DE LAS MOTOS 
#miImagen1 = PhotoImage(file="BOXER.png")
#Label(ventana,image=).place(x=720, y=10)
#tex1=Label(text="PRADO:", font=("Arial ",20)).place(x=610,y=100)

#miImagen2 = PhotoImage(file="NS200.png")
#Label(ventana,image=miImagen2).place(x=1400, y=10)
#tex2=Label(text="JEEP:",font=("Arial Black",20)).place(x=1200,y=100)

#miImagen3 = PhotoImage(file="NKD125.png")
#tex3=Label(text="LAND CRUISER:",font=("Arial Black",20)).place(x=530,y=500) 
#Label(ventana,image=miImagen3).place(x=720,y=320)


#miImagen4 = PhotoImage(file="DISCOVER125.png")
#tex4=Label(text="TOYOTA CRUISER:",font=("Arial Black",20)).place(x=1150,y=500) 
#Label(ventana,image=miImagen4).place(x=1400,y=400)

#miImagen5 = PhotoImage(file="NMAX.png") 
#Label(ventana,image=miImagen5).place(x=750,y=650) 
#tex5=Label(text="AUDI:",font=("Arial Black",20)).place(x=650,y=900)

# BOTON CONSULTAR
btnSaludar=Button(ventana,text="Consultar",command=consultar,font=("Arial Black",15),bg="oliveDrab1").place(x=95,y=270)

# FIN DEL PROGRAMA
ventana.mainloop()