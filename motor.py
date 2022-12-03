from tkinter import Label, Entry,StringVar, messagebox, Tk, Spinbox,IntVar,OptionMenu, Radiobutton,Button, Menu


# FUNCIONES 
def consultar():
    LICENCIA = var_licencia.get()
    SEXO = var_sexo.get()
    licenca = var_licencia1.get()
    lblsaludar=Label(ventana,text="Nombres: " + entryNombre.get()+ "\nApellidos: " + entryApellidos.get() + " \nNúmero de CC: "+ "\nNúmero teléfonico:" + entrynumero.get() + entryCedula.get() + "\nSexo: " + SEXO + "\nEdad: " + edad_entry.get() +"\nUbicado en: " + entryubicacion.get() + "\nPosee licencia: " + licenca + "\nTipo de licencia: "+ LICENCIA ,font=("aTimes New Roman",10),bg="#19CCAE").place(x=220,y=300)

def tipo_de_moto():
    moto=selec.get() 
    renta=entryAlquiler.get() 
    horas=int(renta)
    BOXER=horas*5000
    NS200=horas*10000
    NKD125=horas*9000
    DISCOVER125=horas*8000 
    NMAX=horas*15000
    
    lblsaludar1=Label(ventana,text=" Escogiste la opción de la moto numero: "
+ str(moto),font=("Times New Roman",11),bg="grey68").place(x=50,y=460)

    if moto==1:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la BOXER es de $5000"
+"\nEl total a pagar por su renta es de " + str(renta)
+"Las horas de alquiler que desea la moto son:$"+str(BOXER),font=("aTimes New Roman",11),bg="#19CCAE").place(x=50,y=485)
    
    elif moto==2:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NS200 es de $10000"
+"\nEl total a pagar por su renta es de " + str(renta)
+"Las horas de alquiler que desea la moto son:$"+str(NS200),font=("aTimes New Roman",11),bg="#19CCAE").place(x=50,y=485)

    elif moto==3:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NKD125 es de $9000"
+"\nEl total a pagar por su renta es de " + str(renta)
+"Las horas de alquiler que desea la moto son:$"+str(NKD125),font=("aTimes New Roman",11),bg="#19CCAE").place(x=50,y=485)

    elif moto==4:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la DISCOVER125 es de $8000"
+"\nEl total a pagar por su renta es de " + str(renta)
+"Las horas de alquiler que desea la moto son:$"+str(DISCOVER125),font=("aTimes New Roman",11),bg="#19CCAE").place(x=50,y=485)

    else:
        lblconsultar2=Label(ventana,text="*El costo de la hora de alquiler de la NMAX es de $15000"
+"\nEl total a pagar por su renta es de " + str(renta)
+"Las horas de alquiler que desea la moto son:$"+str(NMAX),font=("aTimes New Roman",11),bg="#19CCAE").place(x=50,y=485)

def borrar():
    txtUbicacion.delete(0, "end")
    txtApellidos.delete(0, "end")
    txtCedula.delete(0, "end")
    txtdireccion.delete(0, "end")
    txtAlquiler.delete(0, "end")
    txtNombre.delete(0, "end")
    edad_entry.delete(0, "end")
    
def cancelar():
    ventana.destroy()
    
def salir():
    ventana.destroy()
    
def manual_usuario():
    messagebox.showinfo("Manual de usuario", "En construcción...")

def acerca_de():
    messagebox.showinfo("Acerca de...", "Versión 1.0")
  
#DIMENSIONES DE LA VENTANA
ventana=Tk() 
ventana.geometry("700x600")
ventana.title("AGUANCHA MOTOR ")
barra_menus = Menu()
ventana.config(menu=barra_menus)
menu_edicion = Menu(tearoff=0)

# TEXTOS 
lblaguancha_motor=Label(text="AGUANCHA MOTOR",font=("Times New Roman",16),bg="#19CCAE").place(x=250,y=10) 
lblDatos_personales =Label(text="DATOS PERSONALES ",font=("Times New Roman",14)).place(x=20,y=50) 
lbVehiculos_disponibles =Label(text="Vehículos disponibles: ",font=("Times New Roman",16)).place(x=20,y=290) 

# ENTRADA DE DATOS DE LA PERSONA 
# NOMBRE DEL CLIENTE 
lblNombres=Label(text="Nombres:",font=("Times New Roman",16))
lblNombres.place(x=20,y=80) 
entryNombre=StringVar() 
txtNombre = Entry(ventana,textvariable=entryNombre,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtNombre.place(x=110,y=80)

# APELLIDOS DEL CLIENTE 
lblApellidos=Label(text="Apellidos:",font=("Times New Roman",16))
lblApellidos.place(x=275,y=75) 
entryApellidos=StringVar() 
txtApellidos = Entry(ventana,textvariable=entryApellidos,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtApellidos.place(x=368,y=80)

# EDAD DEL CLIENTE 
edad_minima = 18
edad_maxima = 65
edad_label = Label(text="Edad:")
edad_entry = Spinbox(from_=edad_minima, to=edad_maxima, width=3, bd=3, highlightcolor="#0C4881", highlightthickness=2)
selecciones_label = Label(text="", padx=10, justify="left")
lbledad=Label(text="Edad:",font=("Times New Roman",16)).place(x=275,y=110)
edad_entry.grid(padx=330,pady=110)

# CEDULA DEL CLIENTE 
lblCedula=Label(text="Cédula:",font=("Times New Roman",16))
lblCedula.place(x=20,y=110) 
entryCedula=StringVar() 
txtCedula=Entry(ventana,textvariable=entryCedula,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtCedula.place(x=95,y=111)

# NUMERO DE TELEFONO DEL CLIENTE 
lblnumero=Label(text="Numero teléfonico:",font=("Times New Roman",16))
lblnumero.place(x=380,y=110) 
entrynumero=StringVar() 
txtnumero=Entry(ventana,textvariable=entrynumero,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtnumero.place(x=550,y=112)

# DIRECCIÓN DEL CLIENTE 
lbldireccion=Label(text="Dirección:",font=("Times New Roman",16))
lbldireccion.place(x=275,y=140) 
entrydireccion=StringVar() 
txtdireccion=Entry(ventana,textvariable=entrydireccion,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtdireccion.place(x=370,y=142)

# UBICACION DEL CLIENTE 
lblUbicacion=Label(text="Ubicación:",font=("Times New Roman",16))
lblUbicacion.place(x=20,y=140) 
entryubicacion=StringVar() 
txtUbicacion=Entry(ventana,textvariable=entryubicacion,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtUbicacion.place(x=120,y=141)

# LICENCIA DEL CLIENTE 
var_licencia1 = StringVar()
lbllicencia1=Label(text="¿Tiene licencia de conducción?",font=("Times New Roman",16)).place(x=20,y=170) 
licencia1_menu = OptionMenu(ventana, var_licencia1, "SI", "NO")
var_licencia1.set("Pulse para ver")
licencia1_menu.place(x=40,y=200)
 
# HORAS DE RENTA DEL CLIENTE 
lblAlquiler=Label(text="¿Horas que desea rentar el vehículo?",font=("Times New Roman",16))
lblAlquiler.place(x=20,y=230)
entryAlquiler=IntVar() 
txtAlquiler=Entry(ventana,textvariable=entryAlquiler,bd=3,highlightcolor="#0C4881", highlightthickness=2)
txtAlquiler.place(x=40,y=260)

# SEXO DEL CLIENTE 
var_sexo = StringVar()
lblsexo=Label(text="Sexo:",font=("Times New Roman",16)).place(x=510,y=75)
sexo_menu = OptionMenu(ventana, var_sexo, "MASCULINO", "FEMENINO","INDEFINIDO",)
var_sexo.set("Pulse para ver")
sexo_menu.place(x=560,y=75)

# TIPO DE LICENDIA 
var_licencia = StringVar()
lbllicencia=Label(text="¿Tipo de licencia? ",font=("Times New Roman",16)).place(x=400,y=230)
licencia_menu = OptionMenu(ventana, var_licencia, "A1", "A2", "B1", "B2", "B3")
var_licencia.set("Pulse para ver")
licencia_menu.place(x=410,y=260)

# BOTONES DE LAS MOTOS 
selec=IntVar()

moto1=Radiobutton(ventana,text="1. BOXER",value=1,
variable=selec,command=tipo_de_moto,font=("Times New Roman",11)).place(x=30,y=315) 

moto2=Radiobutton(ventana,text="2. NS200",value=2,
variable=selec,command=tipo_de_moto,font=("Times New Roman",11)).place(x=30,y=335) 

moto3=Radiobutton(ventana,text="3. NKD125",value=3,
variable=selec,command=tipo_de_moto,font=("Times New Roman",11)).place(x=30,y=355) 

moto4=Radiobutton(ventana,text="4. DISCOVER125",value=4,
variable=selec,command=tipo_de_moto,font=("Times New Roman",11)).place(x=30,y=375) 

moto5=Radiobutton(ventana,text="5. NMAX",value=5,
variable=selec,command=tipo_de_moto,font=("Times New Roman",11)).place(x=30,y=395)

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
btnconsultar=Button(ventana,text="Consultar",command=consultar,font=("Arial Black",15),bg="#19CCAE").place(x=100,y=530)
btnborrar=Button(ventana,text="Borrar",command=borrar,font=("Arial Black",15),bg="#19CCAE").place(x=310,y=530)
btncancelar=Button(ventana,text="Cancelar",command=cancelar,font=("Arial Black",15),bg="#19CCAE").place(x=480,y=530)

# BARRA DE MENU 
menu_archivo = Menu(tearoff=0)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", compound="left", command=salir)
barra_menus.add_cascade(label="Archivo", menu=menu_archivo)
menu_edicion.add_command(label="En proceso ", command=manual_usuario)
barra_menus.add_cascade(label="Edición", menu=menu_edicion)
menu_ayuda = Menu(tearoff=0)
menu_ayuda.add_command(label="Términos y Condiciones", command=manual_usuario)
menu_ayuda.add_command(label="Versión del programa", command=acerca_de)
barra_menus.add_cascade(label="Ayuda", menu=menu_ayuda)

# FIN DEL PROGRAMA
ventana.mainloop()
