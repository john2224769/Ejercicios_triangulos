from tkinter import *
from tkinter import messagebox

def comprobar():
    messagebox.showinfo("Comprobar", "Comprobacion completa...")
    if int(a.get())>0 and int(b.get())>0 and int(c.get())>0:
        if int(a.get())+int(b.get())>int(c.get()) and int(a.get())+int(c.get())>int(b.get()) and int(b.get())+int(c.get())>int(a.get()):
            if int(a.get())==int(b.get()) and int(a.get())==int(c.get()) and int(b.get())==int(c.get()):
                r="Los lados forman un triangulo equilatero"
            elif int(a.get())==int(b.get()) or int(a.get())==int(c.get()) or int(c.get())==int(b.get()):
                r="Los lados forman un triangulo isosceles"
            elif int(a.get())!=int(b.get()) and int(b.get())!=int(c.get()) and int(a.get())!=int(c.get()):
                r="Los lados forman un triangulo escaleno"
        else:
            r="Los valores ingresados NO pueden formar un triangulo"
    else:
        r="Los valores ingresados NO pueden formar un triangulo, uno de ellos es menor o igual a cero"
    t_resultados.insert(INSERT, r+"\n")

def borrar():
    messagebox.showinfo("Borrar", "Se borraran los campos llenos... ")
    a.set("")
    b.set("")
    c.set("")
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Salir: ", "La app se cerrara... ")
    ventana.destroy()

ventana= Tk()

a=StringVar()
b=StringVar()
c=StringVar()

ventana.title("Clasificacion de triangulos 1.0")
ventana.geometry("500x600")
ventana.resizable(0,0)
ventana.config(bg="black")

#Frame de entrada
frame_entrada= Frame(ventana)
frame_entrada.config(bg="white", width=480, height=260)
frame_entrada.place(x=10, y=10)

titulo = Label(frame_entrada, text= "Tipo de triangulo \n Ingrese los tres lados del triangulo" )
titulo.config(bg="white", fg="green", font=("Arial",16))
titulo.place(x=70, y=10)

#Lado a
lb_a = Label(frame_entrada, text="Lado a = " )
lb_a.config(bg="white", fg="green", font=("Arial",16))
lb_a.place(x=50, y=100, width=100, height=30)

entry_a= Entry(frame_entrada, textvariable=a) 
entry_a.config(font=("Arial, 16"), justify=LEFT, fg="green")
entry_a.focus_set()
entry_a.place(x=150, y=100, width=100, height=30)

#Lado b
lb_b = Label(frame_entrada, text="Lado b = " )
lb_b.config(bg="white", fg="green", font=("Arial",16))
lb_b.place(x=50, y=150, width=100, height=30)

entry_b= Entry(frame_entrada, textvariable=b) 
entry_b.config(font=("Arial, 16"), justify=LEFT, fg="green")
entry_b.place(x=150, y=150, width=100, height=30)

#Lado c
lb_c = Label(frame_entrada, text="Lado c = " )
lb_c.config(bg="white", fg="green", font=("Arial",16))
lb_c.place(x=50, y=200, width=100, height=30)

entry_c= Entry(frame_entrada, textvariable=c) 
entry_c.config(font=("Arial, 16"), justify=LEFT, fg="green")
entry_c.place(x=150, y=200, width=100, height=30)

#Frame de opciones
frame_opciones= Frame(ventana)
frame_opciones.config(bg="white", width=480, height=120)
frame_opciones.place(x=10, y=280)


#Botones
#Boton comprobar
bt_comprobar= Button(frame_opciones, text="Comprobar", command=comprobar)
bt_comprobar.place(x=40, y=45, width=100, height=30)

#Boton borrar
bt_borrar = Button(frame_opciones, text="Borrar", command=borrar)
bt_borrar.place(x=190 , y=45 , width=100, height=30)

#Boton salir
bt_salir = Button(frame_opciones, text="Salir", command=salir)
bt_salir.place(x=335 , y=45 , width=100, height=30)

#Frame de resultados
frame_resultados= Frame(ventana)
frame_resultados.config(bg="white", width=480, height=150)
frame_resultados.place(x=10, y=410)

t_resultados= Text(frame_resultados)
t_resultados.config(bg="green", width=57, height=8)
t_resultados.place(x=10, y=10 )

ventana.mainloop()