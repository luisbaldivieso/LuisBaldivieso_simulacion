import tkinter as tk
from tkinter import ttk, messagebox
import random

def generar():
    try:
        p=float(entry_p.get())
        n=int(entry_n.get())

        if not (0<=p<=1):
            messagebox.showerror("Error","p debe estar entre 0 y 1.")
            return

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1,n+1):
            ri=random.random()
            xi=1 if ri<p else 0

            tabla.insert("",tk.END,
                         values=(i,
                                 f"{ri:.5f}",
                                 xi))

    except:
        messagebox.showerror("Error","Datos inválidos.")

def limpiar():
    entry_p.delete(0,tk.END)
    entry_n.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

ventana=tk.Tk()
ventana.title("Distribución Bernoulli")
ventana.geometry("700x500")

tk.Label(ventana,text="Distribución Bernoulli",
font=("Arial",16,"bold")).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Probabilidad p").grid(row=0,column=0,padx=5,pady=5)
entry_p=tk.Entry(frame)
entry_p.grid(row=0,column=1)

tk.Label(frame,text="Cantidad").grid(row=1,column=0,padx=5,pady=5)
entry_n=tk.Entry(frame)
entry_n.grid(row=1,column=1)

botones=tk.Frame(ventana)
botones.pack(pady=10)

tk.Button(botones,text="Generar",bg="lightgreen",
command=generar).grid(row=0,column=0,padx=10)

tk.Button(botones,text="Limpiar",bg="tomato",
command=limpiar).grid(row=0,column=1,padx=10)

tabla=ttk.Treeview(ventana,
columns=("i","ri","Xi"),
show="headings",height=15)

for c in ("i","ri","Xi"):
    tabla.heading(c,text=c)

tabla.pack(fill="both",expand=True,padx=10,pady=10)

ventana.mainloop()