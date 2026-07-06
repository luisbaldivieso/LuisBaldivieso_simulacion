import tkinter as tk
from tkinter import ttk,messagebox
import random
import math

def generar():

    try:
        alpha=int(entry_alpha.get())
        beta=float(entry_beta.get())
        cantidad=int(entry_n.get())

        if alpha<=0 or beta<=0:
            raise ValueError

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(cantidad):

            producto=1

            for j in range(alpha):
                producto*=1-random.random()

            xi=-(beta/alpha)*math.log(producto)

            tabla.insert("",tk.END,
                         values=(i+1,
                                 f"{xi:.5f}"))

    except:
        messagebox.showerror("Error","Datos incorrectos.")

def limpiar():

    entry_alpha.delete(0,tk.END)
    entry_beta.delete(0,tk.END)
    entry_n.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

ventana=tk.Tk()
ventana.title("Distribución Gamma")
ventana.geometry("650x500")

tk.Label(ventana,
text="Distribución Gamma",
font=("Arial",16,"bold")).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Alpha").grid(row=0,column=0)
entry_alpha=tk.Entry(frame)
entry_alpha.grid(row=0,column=1)

tk.Label(frame,text="Beta").grid(row=1,column=0)
entry_beta=tk.Entry(frame)
entry_beta.grid(row=1,column=1)

tk.Label(frame,text="Cantidad").grid(row=2,column=0)
entry_n=tk.Entry(frame)
entry_n.grid(row=2,column=1)

tk.Button(frame,text="Generar",
command=generar,bg="lightgreen").grid(row=3,column=0,pady=10)

tk.Button(frame,text="Limpiar",
command=limpiar,bg="tomato").grid(row=3,column=1)

tabla=ttk.Treeview(
ventana,
columns=("i","Xi"),
show="headings",
height=15)

tabla.heading("i",text="i")
tabla.heading("Xi",text="Xi")

tabla.pack(fill="both",expand=True,padx=10,pady=10)

ventana.mainloop()