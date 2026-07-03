import tkinter as tk
from tkinter import ttk, messagebox

from motor_ruleta import simular_giro
from estrategias import crear_estrategia
from estadisticas import Estadisticas
from graficos import mostrar_todos


# ==========================================
# VARIABLES GLOBALES
# ==========================================

estadisticas = Estadisticas()

numeros = []

rojos = 0
negros = 0
verdes = 0


# ==========================================
# FUNCIONES
# ==========================================

def simular():

    global numeros
    global rojos
    global negros
    global verdes

    tabla.delete(*tabla.get_children())

    try:

        capital = int(entry_capital.get())

        apuesta = int(entry_apuesta.get())

        giros = int(entry_giros.get())

    except:

        messagebox.showerror(

            "Error",

            "Ingrese valores numéricos."

        )

        return

    if capital <= 0:

        messagebox.showerror(

            "Error",

            "Capital incorrecto."

        )

        return

    if apuesta <= 0:

        messagebox.showerror(

            "Error",

            "Apuesta incorrecta."

        )

        return

    if giros <= 0:

        messagebox.showerror(

            "Error",

            "Cantidad de giros incorrecta."

        )

        return

    estrategia_obj = crear_estrategia(

        estrategia.get(),

        apuesta

    )

    estadisticas.reiniciar()

    estadisticas.iniciar(capital)

    numeros = []

    rojos = 0

    negros = 0

    verdes = 0

    for giro in range(giros):

        apuesta_actual = estrategia_obj.obtener_apuesta()

        datos = simular_giro(

            capital,

            apuesta_actual,

            tipo_apuesta.get()

        )

        capital = datos["capital"]

        if datos["gano"]:

            estrategia_obj.ganar()

        else:

            estrategia_obj.perder()

        estadisticas.registrar(

            capital,

            datos["gano"],

            apuesta_actual

        )

        numeros.append(

            datos["numero"]

        )

        if datos["color"] == "Rojo":

            rojos += 1

        elif datos["color"] == "Negro":

            negros += 1

        else:

            verdes += 1

        tabla.insert(

            "",

            "end",

            values=(

                giro + 1,

                datos["numero"],

                datos["color"],

                datos["resultado"],

                capital

            )

        )

    resumen = estadisticas.resumen()

    lbl_giros.config(

        text=f"Giros: {resumen['giros']}"

    )

    lbl_ganadas.config(

        text=f"Ganadas: {resumen['ganadas']}"

    )

    lbl_perdidas.config(

        text=f"Perdidas: {resumen['perdidas']}"

    )

    lbl_capital.config(

        text=f"Capital Final: {resumen['capital_final']}"

    )

    lbl_porcentaje.config(

        text=f"Aciertos: {resumen['porcentaje_aciertos']:.2f}%"

    )

    mostrar_todos(

        estadisticas.historial,

        estadisticas.ganadas,

        estadisticas.perdidas,

        rojos,

        negros,

        verdes,

        numeros

    )


def limpiar():

    entry_capital.delete(

        0,

        tk.END

    )

    entry_apuesta.delete(

        0,

        tk.END

    )

    entry_giros.delete(

        0,

        tk.END

    )

    entry_capital.insert(

        0,

        "1000"

    )

    entry_apuesta.insert(

        0,

        "10"

    )

    entry_giros.insert(

        0,

        "100"

    )

    tipo_apuesta.set(

        "Rojo"

    )

    estrategia.set(

        "Apuesta fija"

    )

    tabla.delete(

        *tabla.get_children()

    )

    lbl_giros.config(

        text="Giros:"

    )

    lbl_ganadas.config(

        text="Ganadas:"

    )

    lbl_perdidas.config(

        text="Perdidas:"

    )

    lbl_capital.config(

        text="Capital Final:"

    )

    lbl_porcentaje.config(

        text="Aciertos:"

    )


def salir():

    ventana.destroy()


# ==========================================
# VENTANA
# ==========================================

ventana = tk.Tk()

ventana.title("Ruleta Monte Carlo")

ventana.geometry("1200x850")

ventana.resizable(False, False)

titulo = tk.Label(

    ventana,

    text="RULETA MONTE CARLO",

    font=("Arial",20,"bold")

)

titulo.pack(pady=10)

frame = tk.Frame(

    ventana

)

frame.pack()
# ==========================================
# DATOS DE ENTRADA
# ==========================================

tk.Label(
    frame,
    text="Capital Inicial:"
).grid(row=0, column=0, padx=10, pady=5)

entry_capital = tk.Entry(frame, width=12)
entry_capital.insert(0, "1000")
entry_capital.grid(row=0, column=1)


tk.Label(
    frame,
    text="Apuesta Inicial:"
).grid(row=1, column=0, padx=10, pady=5)

entry_apuesta = tk.Entry(frame, width=12)
entry_apuesta.insert(0, "10")
entry_apuesta.grid(row=1, column=1)


tk.Label(
    frame,
    text="Número de Giros:"
).grid(row=2, column=0, padx=10, pady=5)

entry_giros = tk.Entry(frame, width=12)
entry_giros.insert(0, "100")
entry_giros.grid(row=2, column=1)


# ==========================================
# TIPO DE APUESTA
# ==========================================

tk.Label(
    frame,
    text="Tipo de Apuesta:"
).grid(row=0, column=2, padx=15)

tipo_apuesta = tk.StringVar()

combo_tipo = ttk.Combobox(
    frame,
    textvariable=tipo_apuesta,
    state="readonly",
    width=18
)

combo_tipo["values"] = (
    "Rojo",
    "Negro",
    "Verde"
)

combo_tipo.current(0)

combo_tipo.grid(row=0, column=3)


# ==========================================
# ESTRATEGIAS
# ==========================================

tk.Label(
    frame,
    text="Estrategia:"
).grid(row=1, column=2)

estrategia = tk.StringVar()

combo_estrategia = ttk.Combobox(
    frame,
    textvariable=estrategia,
    state="readonly",
    width=18
)

combo_estrategia["values"] = (
    "Apuesta fija",
    "Martingala",
    "D'Alembert",
    "Paroli"
)

combo_estrategia.current(0)

combo_estrategia.grid(row=1, column=3)


# ==========================================
# BOTONES
# ==========================================

frame_botones = tk.Frame(ventana)

frame_botones.pack(pady=15)

tk.Button(
    frame_botones,
    text="Simular",
    bg="green",
    fg="white",
    width=15,
    font=("Arial",10,"bold"),
    command=simular
).grid(row=0,column=0,padx=5)

tk.Button(
    frame_botones,
    text="Limpiar",
    bg="orange",
    fg="white",
    width=15,
    font=("Arial",10,"bold"),
    command=limpiar
).grid(row=0,column=1,padx=5)

tk.Button(
    frame_botones,
    text="Salir",
    bg="red",
    fg="white",
    width=15,
    font=("Arial",10,"bold"),
    command=salir
).grid(row=0,column=2,padx=5)


# ==========================================
# TABLA
# ==========================================

columnas = (

    "Giro",

    "Número",

    "Color",

    "Resultado",

    "Capital"

)

tabla = ttk.Treeview(

    ventana,

    columns=columnas,

    show="headings",

    height=15

)

for col in columnas:

    tabla.heading(col,text=col)

    tabla.column(col,width=180,anchor="center")

tabla.pack(pady=10)


# ==========================================
# ESTADISTICAS
# ==========================================

frame_est = tk.LabelFrame(

    ventana,

    text="Estadísticas",

    font=("Arial",11,"bold")

)

frame_est.pack(

    fill="x",

    padx=10,

    pady=10

)

lbl_giros = tk.Label(

    frame_est,

    text="Giros:",

    font=("Arial",11)

)

lbl_giros.grid(row=0,column=0,padx=20,pady=5)

lbl_ganadas = tk.Label(

    frame_est,

    text="Ganadas:",

    font=("Arial",11)

)

lbl_ganadas.grid(row=0,column=1,padx=20)

lbl_perdidas = tk.Label(

    frame_est,

    text="Perdidas:",

    font=("Arial",11)

)

lbl_perdidas.grid(row=0,column=2,padx=20)

lbl_capital = tk.Label(

    frame_est,

    text="Capital Final:",

    font=("Arial",11)

)

lbl_capital.grid(row=1,column=0,padx=20)

lbl_porcentaje = tk.Label(

    frame_est,

    text="Aciertos:",

    font=("Arial",11)

)

lbl_porcentaje.grid(row=1,column=1,padx=20)


# ==========================================
# MAIN
# ==========================================

ventana.mainloop()