import tkinter as tk
from tkinter import ttk, messagebox
import math
from statistics import NormalDist

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# ===================================
# FUNCIONES
# ===================================

canvas = None


def obtener_numeros():

    texto = txt_datos.get("1.0", tk.END)

    texto = texto.replace(",", " ")

    lista = []

    for valor in texto.split():

        try:

            numero = float(valor)

            if 0 <= numero <= 1:

                lista.append(numero)

        except:

            pass

    return lista


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

    n = len(numeros)

    promedio = sum(numeros) / n

    z0 = (promedio - 0.5) / math.sqrt(1 / (12 * n))

    z_critico = NormalDist().inv_cdf(1 - alpha / 2)

    if abs(z0) < z_critico:

        resultado = "SE ACEPTA H0"

        color = "green"

    else:

        resultado = "SE RECHAZA H0"

        color = "red"

    lbl_n.config(text=f"Cantidad de datos: {n}")

    lbl_promedio.config(text=f"Promedio: {promedio:.6f}")

    lbl_z0.config(text=f"Z calculado: {z0:.6f}")

    lbl_zc.config(text=f"Z crítico: ±{z_critico:.6f}")

    lbl_resultado.config(

        text=resultado,

        fg=color

    )

    for i, valor in enumerate(numeros):

        tabla.insert(

            "",

            "end",

            values=(

                i + 1,

                f"{valor:.6f}"

            )

        )

    figura = plt.Figure(figsize=(6,3), dpi=100)

    grafico = figura.add_subplot(111)

    grafico.hist(

        numeros,

        bins=10,

        edgecolor="black"

    )

    grafico.set_title("Histograma")

    grafico.set_xlabel("Ri")

    grafico.set_ylabel("Frecuencia")

    canvas = FigureCanvasTkAgg(

        figura,

        master=frame_grafico

    )

    canvas.draw()

    canvas.get_tk_widget().pack()


def limpiar():

    global canvas

    txt_datos.delete("1.0", tk.END)

    entry_alpha.delete(0, tk.END)

    entry_alpha.insert(0, "0.05")

    tabla.delete(*tabla.get_children())

    if canvas:

        canvas.get_tk_widget().destroy()

        canvas = None

    lbl_n.config(text="Cantidad de datos:")

    lbl_promedio.config(text="Promedio:")

    lbl_z0.config(text="Z calculado:")

    lbl_zc.config(text="Z crítico:")

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

ventana.title("Prueba de la Media")

ventana.geometry("1100x800")

ventana.resizable(False, False)

titulo = tk.Label(

    ventana,

    text="PRUEBA DE LA MEDIA",

    font=("Arial",18,"bold")

)

titulo.pack(pady=10)

frame_superior = tk.Frame(ventana)

frame_superior.pack()

tk.Label(

    frame_superior,

    text="Nivel de significancia α"

).grid(row=0,column=0,padx=10)

entry_alpha = tk.Entry(

    frame_superior,

    width=10

)

entry_alpha.insert(0,"0.05")

entry_alpha.grid(row=0,column=1)

tk.Label(

    frame_superior,

    text="Pegue los Ri (espacios, comas o saltos de línea)"

).grid(row=1,column=0,columnspan=2,pady=10)

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

).grid(row=3,column=0,pady=10)

tk.Button(

    frame_superior,

    text="Limpiar",

    bg="orange",

    fg="white",

    command=limpiar

).grid(row=3,column=1)
tk.Button(

    frame_superior,

    text="Salir",

    bg="red",

    fg="white",

    command=salir

).grid(row=3,column=2)


# ===================================
# RESULTADOS
# ===================================

frame_resultados = tk.Frame(ventana)

frame_resultados.pack(pady=10)

lbl_n = tk.Label(

    frame_resultados,

    text="Cantidad de datos:",

    font=("Arial",11)

)

lbl_n.pack(anchor="w")

lbl_promedio = tk.Label(

    frame_resultados,

    text="Promedio:",

    font=("Arial",11)

)

lbl_promedio.pack(anchor="w")

lbl_z0 = tk.Label(

    frame_resultados,

    text="Z calculado:",

    font=("Arial",11)

)

lbl_z0.pack(anchor="w")

lbl_zc = tk.Label(

    frame_resultados,

    text="Z crítico:",

    font=("Arial",11)

)

lbl_zc.pack(anchor="w")

lbl_resultado = tk.Label(

    frame_resultados,

    text="Resultado:",

    font=("Arial",13,"bold")

)

lbl_resultado.pack(pady=5)


# ===================================
# TABLA
# ===================================

columnas = (

    "N",

    "Ri"

)

tabla = ttk.Treeview(

    ventana,

    columns=columnas,

    show="headings",

    height=10

)

for col in columnas:

    tabla.heading(col,text=col)

    tabla.column(

        col,

        width=120,

        anchor="center"

    )

tabla.pack(pady=10)


# ===================================
# GRAFICO
# ===================================

frame_grafico = tk.Frame(ventana)

frame_grafico.pack(fill="both", expand=True)


# ===================================
# MAIN
# ===================================

ventana.mainloop()