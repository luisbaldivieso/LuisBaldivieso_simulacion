import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

# ==========================
# FUNCIONES
# ==========================

def generar():
    try:
        lam = float(entry_lambda.get())
        n = int(entry_n.get())

        if lam <= 0:
            messagebox.showerror("Error", "λ debe ser mayor que cero.")
            return

        if n <= 0:
            messagebox.showerror("Error", "La cantidad debe ser mayor que cero.")
            return

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1, n + 1):
            ri = random.random()
            xi = -(1 / lam) * math.log(1 - ri)

            tabla.insert("", "end",
                         values=(i,
                                 f"{ri:.5f}",
                                 f"{xi:.5f}"))

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores válidos.")

def limpiar():
    entry_lambda.delete(0, tk.END)
    entry_n.delete(0, tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

# ==========================
# VENTANA
# ==========================

ventana = tk.Tk()
ventana.title("Distribución Exponencial")
ventana.geometry("700x500")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="Distribución Exponencial",
    font=("Arial",16,"bold")
).pack(pady=10)

frame=tk.Frame(ventana)
frame.pack()

tk.Label(frame,text="λ:").grid(row=0,column=0,padx=10,pady=5)
entry_lambda=tk.Entry(frame,width=15)
entry_lambda.grid(row=0,column=1)

tk.Label(frame,text="Cantidad:").grid(row=1,column=0,padx=10,pady=5)
entry_n=tk.Entry(frame,width=15)
entry_n.grid(row=1,column=1)

botones=tk.Frame(ventana)
botones.pack(pady=10)

tk.Button(botones,text="Generar",bg="lightgreen",width=15,
command=generar).grid(row=0,column=0,padx=10)

tk.Button(botones,text="Limpiar",bg="tomato",width=15,
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