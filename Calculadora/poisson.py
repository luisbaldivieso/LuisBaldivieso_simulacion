import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

def generar():

    try:
        lam=float(entry_lambda.get())
        cantidad=int(entry_n.get())

        if lam<=0:
            raise ValueError

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1,cantidad+1):

            L=math.exp(-lam)
            k=0
            p=1

            while p>L:
                k+=1
                p*=random.random()

            xi=k-1

            tabla.insert("",tk.END,
                         values=(i,xi))

    except:
        messagebox.showerror("Error","Datos incorrectos.")

def limpiar():

    entry_lambda.delete(0,tk.END)
    entry_n.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

ventana=tk.Tk()
ventana.title("Distribución Poisson")
ventana.geometry("650x500")

tk.Label(ventana,
text="Distribución Poisson",
font=("Arial",16,"bold")).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Lambda (λ)").grid(row=0,column=0,pady=5)
entry_lambda=tk.Entry(frame)
entry_lambda.grid(row=0,column=1)

tk.Label(frame,text="Cantidad").grid(row=1,column=0,pady=5)
entry_n=tk.Entry(frame)
entry_n.grid(row=1,column=1)

tk.Button(frame,text="Generar",
command=generar,bg="lightgreen").grid(row=2,column=0,pady=10)

tk.Button(frame,text="Limpiar",
command=limpiar,bg="tomato").grid(row=2,column=1)

tabla=ttk.Treeview(ventana,
columns=("i","Xi"),
show="headings",
height=15)

tabla.heading("i",text="i")
tabla.heading("Xi",text="Xi")

tabla.pack(fill="both",expand=True,padx=10,pady=10)

ventana.mainloop()