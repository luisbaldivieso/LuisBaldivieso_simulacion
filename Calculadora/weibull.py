import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

# ==========================
# FUNCIONES
# ==========================

def generar():

    try:
        gamma = float(entry_gamma.get())
        alpha = float(entry_alpha.get())
        beta = float(entry_beta.get())
        cantidad = int(entry_n.get())

        if alpha <= 0 or beta <= 0 or cantidad <= 0:
            raise ValueError

        for fila in tabla.get_children():
            tabla.delete(fila)

        for i in range(1, cantidad + 1):

            ri = random.random()

            xi = gamma + beta * ((-math.log(1 - ri)) ** (1 / alpha))

            tabla.insert(
                "",
                tk.END,
                values=(
                    i,
                    f"{ri:.5f}",
                    f"{xi:.5f}"
                )
            )

    except:
        messagebox.showerror(
            "Error",
            "Verifique los datos ingresados."
        )


def limpiar():

    entry_gamma.delete(0, tk.END)
    entry_alpha.delete(0, tk.END)
    entry_beta.delete(0, tk.END)
    entry_n.delete(0, tk.END)

    for fila in tabla.get_children():
        tabla.delete(fila)

# ==========================
# VENTANA
# ==========================

ventana = tk.Tk()
ventana.title("Distribución Weibull")
ventana.geometry("720x520")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="Distribución Weibull",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

frame = tk.Frame(ventana)
frame.pack()

tk.Label(frame, text="Gamma (γ):").grid(row=0, column=0, padx=10, pady=5)
entry_gamma = tk.Entry(frame, width=15)
entry_gamma.grid(row=0, column=1)

tk.Label(frame, text="Alpha (α):").grid(row=1, column=0, padx=10, pady=5)
entry_alpha = tk.Entry(frame, width=15)
entry_alpha.grid(row=1, column=1)

tk.Label(frame, text="Beta (β):").grid(row=2, column=0, padx=10, pady=5)
entry_beta = tk.Entry(frame, width=15)
entry_beta.grid(row=2, column=1)

tk.Label(frame, text="Cantidad:").grid(row=3, column=0, padx=10, pady=5)
entry_n = tk.Entry(frame, width=15)
entry_n.grid(row=3, column=1)

botones = tk.Frame(ventana)
botones.pack(pady=10)

tk.Button(
    botones,
    text="Generar",
    width=15,
    bg="lightgreen",
    command=generar
).grid(row=0, column=0, padx=10)

tk.Button(
    botones,
    text="Limpiar",
    width=15,
    bg="tomato",
    command=limpiar
).grid(row=0, column=1, padx=10)

# ==========================
# TABLA
# ==========================

tabla = ttk.Treeview(
    ventana,
    columns=("i", "ri", "Xi"),
    show="headings",
    height=16
)

tabla.heading("i", text="i")
tabla.heading("ri", text="ri")
tabla.heading("Xi", text="Xi")

tabla.column("i", width=60, anchor="center")
tabla.column("ri", width=180, anchor="center")
tabla.column("Xi", width=220, anchor="center")

scroll = ttk.Scrollbar(
    ventana,
    orient="vertical",
    command=tabla.yview
)

tabla.configure(yscroll=scroll.set)

tabla.pack(side="left", padx=10, pady=10)
scroll.pack(side="right", fill="y")

ventana.mainloop()