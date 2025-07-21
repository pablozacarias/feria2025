from tkinter import *

ventana = Tk()
ventana.title("Operaciones Básicas")
ventana.geometry("500x300")

def fnSuma():
    a=a1.get()
    b=txt2.get()
    c=txt3.get()
    r = float(a) + float(b) + float(c)
    txt4.insert(0,r)

etiqueta1 = Label(ventana, text="Primer número", bg="cyan")
etiqueta1.place(x=10, y=10, width=100, height=30)

lbl2 = Label(ventana, text="Segundo número", bg="cyan")
lbl2.place(x=10, y=50, width=100, height=30)

lbl3 = Label(ventana, text="Tercer número", bg="cyan")
lbl3.place(x=10, y=90, width=100, height=30)

a1 = Entry(ventana, bg="white")
a1.place(x=120, y=10, width=100, height=30)

txt2 = Entry(ventana, bg="white")
txt2.place(x=120, y=50, width=100, height=30)

txt3 = Entry(ventana, bg="white")
txt3.place(x=120, y=90, width=100, height=30)

txt4 = Entry(ventana, bg="white")
txt4.place(x=300, y=50, width=100, height=30)

btn = Button(ventana,text="Sumar", command=fnSuma)
btn.place(x=230, y=50, width=50, height=30)

ventana.mainloop()