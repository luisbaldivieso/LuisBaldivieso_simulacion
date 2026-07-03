import tkinter as tk
from tkinter import messagebox

# ======================================
# FUNCIONES (por ahora)
# ======================================
import subprocess
import os
def cuadrados_medios():
   subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\cuadrados_medios.py"
    ])
def productos_medios():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\productos_medios.py"
    ])

def multiplicador_constante():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\multiplicador_constante.py"
    ])
def congruencial_lineal():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\congruencial_lineal.py"
    ])

def congruencial_multiplicativo():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\congruencial_multiplicativo.py"
    ])

def congruencial_aditivo():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\congruencial_aditivo.py"
    ])

def congruencial_no_lineal():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\congruencial_no_lineal.py"
    ])

def prueba_media():
    subprocess.Popen([
        "python",
        r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\prueba_media.py"
    ])

def prueba_varianza():
    messagebox.showinfo("Prueba Varianza", "Módulo en construcción")

def chi_cuadrado():
    messagebox.showinfo("Chi Cuadrado", "Módulo en construcción")

def kolmogorov():
    messagebox.showinfo("Kolmogorov", "Módulo en construcción")

def independencia():
    messagebox.showinfo("Independencia", "Módulo en construcción")

def uniforme():
    messagebox.showinfo("Distribución Uniforme", "Módulo en construcción")

def exponencial():
    messagebox.showinfo("Distribución Exponencial", "Módulo en construcción")

def normal():
    messagebox.showinfo("Distribución Normal", "Módulo en construcción")

def poisson():
    messagebox.showinfo("Distribución Poisson", "Módulo en construcción")

def binomial():
    messagebox.showinfo("Distribución Binomial", "Módulo en construcción")

def montecarlo():
    messagebox.showinfo("Monte Carlo", "Módulo en construcción")

def volver():
    ventana.destroy()


# ======================================
# VENTANA
# ======================================

ventana = tk.Tk()
ventana.title("Calculadora de Simulación")
ventana.geometry("1300x750")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)

# ======================================
# TITULO
# ======================================

titulo = tk.Label(
    ventana,
    text="CALCULADORA DE SIMULACIÓN",
    font=("Arial",24,"bold"),
    fg="white",
    bg="#0F172A"
)

titulo.pack(pady=10)

# ======================================
# CONTENEDOR PRINCIPAL
# ======================================

contenedor = tk.Frame(
    ventana,
    bg="#0F172A"
)

contenedor.pack(fill="both", expand=True)

# ======================================
# MENU IZQUIERDO
# ======================================

menu = tk.Frame(
    contenedor,
    width=340,
    bg="#1E293B"
)

menu.pack(side="left", fill="y")
menu.pack_propagate(False)

# ======================================
# PANEL DERECHO
# ======================================

panel = tk.Frame(
    contenedor,
    bg="white"
)

panel.pack(side="right", fill="both", expand=True)

mensaje = tk.Label(
    panel,
    text="""

Bienvenido a la Calculadora de Simulación

Seleccione un método del menú izquierdo.

Aquí aparecerán todos los ejercicios del PDF.


""",
    font=("Arial",18),
    bg="white"
)

mensaje.pack(expand=True)

# ======================================
# BOTONES
# ======================================

def crear_boton(texto, comando):

    tk.Button(
        menu,
        text=texto,
        command=comando,
        width=33,
        height=2,
        bg="#2563EB",
        fg="white",
        font=("Arial",11,"bold")
    ).pack(pady=3)


tk.Label(
    menu,
    text="GENERADORES",
    bg="#1E293B",
    fg="white",
    font=("Arial",14,"bold")
).pack(pady=8)

crear_boton("Cuadrados Medios", cuadrados_medios)
crear_boton("Productos Medios", productos_medios)
crear_boton("Multiplicador Constante", multiplicador_constante)
crear_boton("Congruencial Lineal", congruencial_lineal)
crear_boton("Congruencial Multiplicativo", congruencial_multiplicativo)
crear_boton("Congruencial Aditivo", congruencial_aditivo)
crear_boton("Congruencial No Lineal", congruencial_no_lineal)

tk.Label(
    menu,
    text="PRUEBAS",
    bg="#1E293B",
    fg="white",
    font=("Arial",14,"bold")
).pack(pady=8)

crear_boton("Prueba Media", prueba_media)
crear_boton("Prueba Varianza", prueba_varianza)
crear_boton("Chi Cuadrado", chi_cuadrado)
crear_boton("Kolmogorov", kolmogorov)
crear_boton("Independencia", independencia)

tk.Label(
    menu,
    text="DISTRIBUCIONES",
    bg="#1E293B",
    fg="white",
    font=("Arial",14,"bold")
).pack(pady=8)

crear_boton("Uniforme", uniforme)
crear_boton("Exponencial", exponencial)
crear_boton("Normal", normal)
crear_boton("Poisson", poisson)
crear_boton("Binomial", binomial)

tk.Label(
    menu,
    text="SIMULACIÓN",
    bg="#1E293B",
    fg="white",
    font=("Arial",14,"bold")
).pack(pady=8)

crear_boton("Monte Carlo", montecarlo)

tk.Button(
    menu,
    text="← Volver",
    command=volver,
    width=33,
    height=2,
    bg="#DC2626",
    fg="white",
    font=("Arial",11,"bold")
).pack(pady=15)

ventana.mainloop()