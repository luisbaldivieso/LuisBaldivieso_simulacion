import tkinter as tk
from tkinter import ttk,messagebox
import random

def generar():

    try:
        mu=float(entry_mu.get())
        sigma=float(entry_sigma.get())
        cantidad=int(entry_n.get())

        if sigma<=0:
            raise ValueError

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1,cantidad+1):

            suma=0

            for j in range(12):
                suma+=random.random()

            xi=(suma-6)*sigma+mu

            tabla.insert("",tk.END,
                         values=(i,
                                 f"{xi:.5f}"))

    except:
        messagebox.showerror("Error","Datos incorrectos.")

def limpiar():

    entry_mu.delete(0,tk.END)
    entry_sigma.delete(0,tk.END)
    entry_n.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

ventana=tk.Tk()
ventana.title("Distribución Normal")
ventana.geometry("650x500")

tk.Label(ventana,
text="Distribución Normal",
font=("Arial",16,"bold")).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Media (μ)").grid(row=0,column=0,pady=5)
entry_mu=tk.Entry(frame)
entry_mu.grid(row=0,column=1)

tk.Label(frame,text="Desviación (σ)").grid(row=1,column=0,pady=5)
entry_sigma=tk.Entry(frame)
entry_sigma.grid(row=1,column=1)

tk.Label(frame,text="Cantidad").grid(row=2,column=0,pady=5)
entry_n=tk.Entry(frame)
entry_n.grid(row=2,column=1)

tk.Button(frame,text="Generar",
bg="lightgreen",
command=generar).grid(row=3,column=0,pady=10)

tk.Button(frame,text="Limpiar",
bg="tomato",
command=limpiar).grid(row=3,column=1)

tabla=ttk.Treeview(
ventana,
columns=("i","Xi"),
show="headings",
height=15)

tabla.heading("i",text="i")
tabla.heading("Xi",text="Xi")

tabla.pack(fill="both",expand=True,padx=10,pady=10)

ventana.mainloop()