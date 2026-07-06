import tkinter as tk
from tkinter import ttk,messagebox
import random

def generar():

    try:
        ensayos=int(entry_ensayos.get())
        p=float(entry_p.get())
        cantidad=int(entry_cantidad.get())

        if ensayos<=0:
            raise ValueError

        if not (0<=p<=1):
            raise ValueError

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1,cantidad+1):

            exitos=0

            for j in range(ensayos):
                ri=random.random()

                if ri<p:
                    exitos+=1

            tabla.insert("",tk.END,
                         values=(i,exitos))

    except:
        messagebox.showerror("Error","Datos incorrectos.")

def limpiar():

    entry_ensayos.delete(0,tk.END)
    entry_p.delete(0,tk.END)
    entry_cantidad.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

ventana=tk.Tk()
ventana.title("Distribución Binomial")
ventana.geometry("650x500")

tk.Label(ventana,
text="Distribución Binomial",
font=("Arial",16,"bold")).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Ensayos (n)").grid(row=0,column=0,pady=5)
entry_ensayos=tk.Entry(frame)
entry_ensayos.grid(row=0,column=1)

tk.Label(frame,text="Probabilidad (p)").grid(row=1,column=0,pady=5)
entry_p=tk.Entry(frame)
entry_p.grid(row=1,column=1)

tk.Label(frame,text="Cantidad").grid(row=2,column=0,pady=5)
entry_cantidad=tk.Entry(frame)
entry_cantidad.grid(row=2,column=1)

tk.Button(frame,text="Generar",bg="lightgreen",
command=generar).grid(row=3,column=0,pady=10)

tk.Button(frame,text="Limpiar",bg="tomato",
command=limpiar).grid(row=3,column=1)

tabla=ttk.Treeview(ventana,
columns=("i","Xi"),
show="headings",
height=15)

tabla.heading("i",text="i")
tabla.heading("Xi",text="Xi")

tabla.pack(fill="both",expand=True,padx=10,pady=10)

ventana.mainloop()