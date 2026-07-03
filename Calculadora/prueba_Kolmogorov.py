import tkinter as tk
from tkinter import ttk, messagebox
import math

from scipy.stats import kstwo

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ===================================
# VARIABLES
# ===================================

canvas = None


# ===================================
# FUNCIONES
# ===================================

def obtener_numeros():

    texto = txt_datos.get("1.0", tk.END)

    texto = texto.replace(",", " ")

    numeros = []

    for valor in texto.split():

        try:

            x = float(valor)

            if 0 <= x <= 1:

                numeros.append(x)

        except:

            pass

    return numeros


def generar():

    global canvas

    tabla.delete(*tabla.get_children())

    if canvas:

        canvas.get_tk_widget().destroy()

    numeros = obtener_numeros()

    if len(numeros) == 0:

        messagebox.showerror(

            "Error",

            "Ingrese números pseudoaleatorios."

        )

        return

    try:

        alpha = float(entry_alpha.get())

    except:

        alpha = 0.05

    numeros.sort()

    n = len(numeros)

    d_mas = []

    d_menos = []

    for i, ri in enumerate(numeros):

        i1 = i + 1

        d1 = (i1 / n) - ri

        d2 = ri - (i / n)

        d_mas.append(d1)

        d_menos.append(d2)

    dmas = max(d_mas)

    dmenos = max(d_menos)

    d = max(dmas, dmenos)

    d_critico = kstwo.ppf(

        1 - alpha,

        n

    )

    if d < d_critico:

        resultado = "SE ACEPTA H0"

        color = "green"

    else:

        resultado = "SE RECHAZA H0"

        color = "red"

    lbl_n.config(

        text=f"Cantidad: {n}"

    )

    lbl_dmas.config(

        text=f"D+: {dmas:.6f}"

    )

    lbl_dmenos.config(

        text=f"D-: {dmenos:.6f}"

    )

    lbl_d.config(

        text=f"D Máximo: {d:.6f}"

    )

    lbl_critico.config(

        text=f"D Crítico: {d_critico:.6f}"

    )

    lbl_resultado.config(

        text=resultado,

        fg=color

    )

    for i, ri in enumerate(numeros):

        tabla.insert(

            "",

            "end",

            values=(

                i + 1,

                f"{ri:.6f}",

                f"{d_mas[i]:.6f}",

                f"{d_menos[i]:.6f}"

            )

        )

    figura = plt.Figure(

        figsize=(6,3),

        dpi=100

    )

    ax = figura.add_subplot(111)

    ax.step(

        numeros,

        [(i+1)/n for i in range(n)],

        where="post"

    )

    ax.set_title(

        "Distribución Acumulada"

    )

    ax.set_xlabel("Ri")

    ax.set_ylabel("F(Ri)")

    canvas = FigureCanvasTkAgg(

        figura,

        master=frame_grafico

    )

    canvas.draw()

    canvas.get_tk_widget().pack()


def limpiar():

    global canvas

    txt_datos.delete(

        "1.0",

        tk.END

    )

    entry_alpha.delete(

        0,

        tk.END

    )

    entry_alpha.insert(

        0,

        "0.05"

    )

    tabla.delete(

        *tabla.get_children()

    )

    if canvas:

        canvas.get_tk_widget().destroy()

        canvas = None

    lbl_n.config(

        text="Cantidad:"

    )

    lbl_dmas.config(

        text="D+:"

    )

    lbl_dmenos.config(

        text="D-:"

    )

    lbl_d.config(

        text="D Máximo:"

    )

    lbl_critico.config(

        text="D Crítico:"

    )

    lbl_resultado.config(

        text="Resultado:",

        fg="black"

    )


def salir():

    ventana.destroy()


# ===================================
# VENTANA
# ===================================

ventana = tk.Tk()

ventana.title(

    "Prueba Kolmogorov-Smirnov"

)

ventana.geometry(

    "1200x850"

)

ventana.resizable(

    False,

    False

)

tk.Label(

    ventana,

    text="PRUEBA KOLMOGOROV-SMIRNOV",

    font=("Arial",18,"bold")

).pack(

    pady=10

)

frame_superior = tk.Frame(

    ventana

)

frame_superior.pack()

tk.Label(

    frame_superior,

    text="Nivel de significancia α"

).grid(

    row=0,

    column=0,

    padx=10

)

entry_alpha = tk.Entry(

    frame_superior,

    width=10

)

entry_alpha.insert(

    0,

    "0.05"

)

entry_alpha.grid(

    row=0,

    column=1

)

tk.Label(

    frame_superior,

    text="Pegue los Ri"

).grid(

    row=1,

    column=0,

    columnspan=2,

    pady=10

)

txt_datos = tk.Text(

    frame_superior,

    width=60,

    height=8

)

txt_datos.grid(

    row=2,

    column=0,

    columnspan=3

)

tk.Button(

    frame_superior,

    text="Generar",

    bg="green",

    fg="white",

    command=generar

).grid(

    row=3,

    column=0,

    pady=10

)

tk.Button(

    frame_superior,

    text="Limpiar",

    bg="orange",

    fg="white",

    command=limpiar

).grid(

    row=3,

    column=1

)
tk.Button(

    frame_superior,

    text="Salir",

    bg="red",

    fg="white",

    command=salir

).grid(

    row=3,

    column=2

)


# ===================================
# RESULTADOS
# ===================================

frame_resultados = tk.Frame(

    ventana

)

frame_resultados.pack(

    pady=10

)

lbl_n = tk.Label(

    frame_resultados,

    text="Cantidad:",

    font=("Arial",11)

)

lbl_n.pack(anchor="w")

lbl_dmas = tk.Label(

    frame_resultados,

    text="D+:",

    font=("Arial",11)

)

lbl_dmas.pack(anchor="w")

lbl_dmenos = tk.Label(

    frame_resultados,

    text="D-:",

    font=("Arial",11)

)

lbl_dmenos.pack(anchor="w")

lbl_d = tk.Label(

    frame_resultados,

    text="D Máximo:",

    font=("Arial",11)

)

lbl_d.pack(anchor="w")

lbl_critico = tk.Label(

    frame_resultados,

    text="D Crítico:",

    font=("Arial",11)

)

lbl_critico.pack(anchor="w")

lbl_resultado = tk.Label(

    frame_resultados,

    text="Resultado:",

    font=("Arial",13,"bold")

)

lbl_resultado.pack(

    pady=5

)


# ===================================
# TABLA
# ===================================

columnas = (

    "i",

    "Ri",

    "D+",

    "D-"

)

tabla = ttk.Treeview(

    ventana,

    columns=columnas,

    show="headings",

    height=12

)

for col in columnas:

    tabla.heading(

        col,

        text=col

    )

    tabla.column(

        col,

        width=150,

        anchor="center"

    )

tabla.pack(

    pady=10

)


# ===================================
# GRAFICO
# ===================================

frame_grafico = tk.Frame(

    ventana

)

frame_grafico.pack(

    fill="both",

    expand=True

)


# ===================================
# MAIN
# ===================================

ventana.mainloop()