import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

# ==========================
# FUNCIONES
# ==========================

def generar():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        n = int(entry_n.get())

        if b < a:
            messagebox.showerror("Error","b debe ser mayor o igual que a.")
            return

        if n <= 0:
            messagebox.showerror("Error","Cantidad inválida.")
            return

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1,n+1):

            ri = random.random()

            xi = a + math.floor((b-a+1)*ri)

            tabla.insert("", "end",
                         values=(i,
                                 f"{ri:.5f}",
                                 xi))

    except ValueError:
        messagebox.showerror("Error","Ingrese datos válidos.")

def limpiar():

    entry_a.delete(0,tk.END)
    entry_b.delete(0,tk.END)
    entry_n.delete(0,tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

# ==========================
# VENTANA
# ==========================

ventana=tk.Tk()
ventana.title("Distribución Uniforme Discreta")
ventana.geometry("700x500")
ventana.resizable(False,False)

tk.Label(
    ventana,
    text="Distribución Uniforme Discreta",
    font=("Arial",16,"bold")
).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="Valor mínimo (a):").grid(row=0,column=0,padx=10,pady=5)
entry_a=tk.Entry(frame,width=15)
entry_a.grid(row=0,column=1)

tk.Label(frame,text="Valor máximo (b):").grid(row=1,column=0,padx=10,pady=5)
entry_b=tk.Entry(frame,width=15)
entry_b.grid(row=1,column=1)

tk.Label(frame,text="Cantidad:").grid(row=2,column=0,padx=10,pady=5)
entry_n=tk.Entry(frame,width=15)
entry_n.grid(row=2,column=1)

botones=tk.Frame(ventana)
botones.pack(pady=10)

tk.Button(botones,text="Generar",width=15,bg="lightgreen",
command=generar).grid(row=0,column=0,padx=10)

tk.Button(botones,text="Limpiar",width=15,bg="tomato",
command=limpiar).grid(row=0,column=1,padx=10)

tabla=ttk.Treeview(
    ventana,
    columns=("i","ri","Xi"),
    show="headings",
    height=15
)

tabla.heading("i",text="i")
tabla.heading("ri",text="ri")
tabla.heading("Xi",text="Xi")

tabla.column("i",width=70,anchor="center")
tabla.column("ri",width=180,anchor="center")
tabla.column("Xi",width=180,anchor="center")

scroll=ttk.Scrollbar(ventana,orient="vertical",command=tabla.yview)
tabla.configure(yscroll=scroll.set)

tabla.pack(side="left",padx=10,pady=10)
scroll.pack(side="right",fill="y")

ventana.mainloop()
