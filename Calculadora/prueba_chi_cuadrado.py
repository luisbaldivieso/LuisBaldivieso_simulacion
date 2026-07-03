import tkinter as tk
from tkinter import ttk, messagebox
import math

from scipy.stats import chi2

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
            "Ingrese números."
        )

        return

    try:

        alpha = float(entry_alpha.get())

    except:

        alpha = 0.05

    n = len(numeros)

    m = round(math.sqrt(n))

    ei = n / m

    observadas = [0] * m

    ancho = 1 / m

    for numero in numeros:

        indice = int(numero / ancho)

        if indice >= m:

            indice = m - 1

        observadas[indice] += 1

    chi_calculado = 0

    for fo in observadas:

        chi_calculado += ((ei - fo) ** 2) / ei

    gl = m - 1

    chi_critico = chi2.ppf(

        1 - alpha,

        gl

    )

    if chi_calculado < chi_critico:

        resultado = "SE ACEPTA H0"

        color = "green"

    else:

        resultado = "SE RECHAZA H0"

        color = "red"

    lbl_n.config(

        text=f"Cantidad: {n}"

    )

    lbl_intervalos.config(

        text=f"Intervalos: {m}"

    )

    lbl_chi.config(

        text=f"Chi Calculado: {chi_calculado:.6f}"

    )

    lbl_critico.config(

        text=f"Chi Crítico: {chi_critico:.6f}"

    )

    lbl_resultado.config(

        text=resultado,

        fg=color

    )

    for i in range(m):

        li = i * ancho

        ls = (i + 1) * ancho

        tabla.insert(

            "",

            "end",

            values=(

                f"{li:.2f} - {ls:.2f}",

                observadas[i],

                f"{ei:.2f}",

                f"{((ei-observadas[i])**2)/ei:.4f}"

            )

        )

    figura = plt.Figure(

        figsize=(6,3),

        dpi=100

    )

    ax = figura.add_subplot(111)

    ax.hist(

        numeros,

        bins=m,

        edgecolor="black"

    )

    ax.set_title(

        "Distribución de Frecuencias"

    )

    ax.set_xlabel("Ri")

    ax.set_ylabel("Frecuencia")

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

    lbl_intervalos.config(

        text="Intervalos:"
    )

    lbl_chi.config(

        text="Chi Calculado:"
    )

    lbl_critico.config(

        text="Chi Crítico:"
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

    "Prueba Chi-Cuadrado"

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

    text="PRUEBA CHI-CUADRADO",

    font=("Arial",18,"bold")

).pack(pady=10)

frame_superior = tk.Frame(

    ventana

)

frame_superior.pack()

tk.Label(

    frame_superior,

    text="Nivel de significancia α"

).grid(row=0,column=0,padx=10)

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

lbl_intervalos = tk.Label(

    frame_resultados,

    text="Intervalos:",

    font=("Arial",11)

)

lbl_intervalos.pack(anchor="w")

lbl_chi = tk.Label(

    frame_resultados,

    text="Chi Calculado:",

    font=("Arial",11)

)

lbl_chi.pack(anchor="w")

lbl_critico = tk.Label(

    frame_resultados,

    text="Chi Crítico:",

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

    "Intervalo",

    "FO",

    "FE",

    "(FE-FO)²/FE"

)

tabla = ttk.Treeview(

    ventana,

    columns=columnas,

    show="headings",

    height=10

)

for col in columnas:

    tabla.heading(

        col,

        text=col

    )

    tabla.column(

        col,

        width=180,

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