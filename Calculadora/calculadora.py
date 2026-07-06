import tkinter as tk
import subprocess

# ======================================
# FUNCION GENERAL
# ======================================

def abrir(path):
    try:
        subprocess.Popen(["python", path])
    except Exception as e:
        print("Error:", e)


# ======================================
# RUTAS BASE (IMPORTANTE PARA EVITAR ERRORES)
# ======================================

BASE = r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final\Calculadora\\"

# ======================================
# 20 MÉTODOS
# ======================================

# GENERADORES
def cuadrados_medios():
    abrir(BASE + "cuadrados_medios.py")

def productos_medios():
    abrir(BASE + "productos_medios.py")

def multiplicador_constante():
    abrir(BASE + "multiplicador_constante.py")

def congruencial_lineal():
    abrir(BASE + "congruencial_lineal.py")

def congruencial_multiplicativo():
    abrir(BASE + "congruencial_multiplicativo.py")

def congruencial_aditivo():
    abrir(BASE + "congruencial_aditivo.py")


# PRUEBAS
def prueba_media():
    abrir(BASE + "prueba_media.py")

def prueba_varianza():
    abrir(BASE + "prueba_varianza.py")

def chi_cuadrado():
    abrir(BASE + "chi_cuadrado.py")

def kolmogorov():
    abrir(BASE + "kolmogorov.py")


# DISTRIBUCIONES (PDF)
def uniforme():
    abrir(BASE + "uniforme.py")

def exponencial():
    abrir(BASE + "exponencial.py")

def gamma():
    abrir(BASE + "gamma.py")

def erlang():
    abrir(BASE + "erlang.py")

def normal():
    abrir(BASE + "normal.py")

def weibull():
    abrir(BASE + "weibull.py")

def bernoulli():
    abrir(BASE + "bernoulli.py")

def binomial():
    abrir(BASE + "binomial.py")   # 🔥 ESTE ERA EL PROBLEMA

def poisson():
    abrir(BASE + "poisson.py")

def montecarlo():
    abrir(BASE + "montecarlo.py")


# ======================================
# VENTANA
# ======================================

ventana = tk.Tk()
ventana.title("Simulación - 20 Métodos")
ventana.geometry("1000x650")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)

# ======================================
# TITULO
# ======================================

tk.Label(
    ventana,
    text="CALCULADORA DE SIMULACIÓN (20 MÉTODOS)",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#0F172A"
).pack(pady=10)

# ======================================
# FRAME PRINCIPAL
# ======================================

contenedor = tk.Frame(ventana, bg="#0F172A")
contenedor.pack(expand=True)

panel = tk.Frame(contenedor, bg="#1E293B", padx=20, pady=20)
panel.pack()

# ======================================
# BOTÓN
# ======================================

def boton(texto, comando):
    return tk.Button(
        panel,
        text=texto,
        command=comando,
        width=30,
        bg="#2563EB",
        fg="white",
        font=("Arial", 10, "bold")
    )

# ======================================
# GRID 2 COLUMNAS (MITAD / MITAD)
# ======================================

# TITULOS
tk.Label(panel, text="GENERADORES", bg="#1E293B", fg="white",
         font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

boton("Cuadrados Medios", cuadrados_medios).grid(row=1, column=0, pady=3)
boton("Productos Medios", productos_medios).grid(row=1, column=1, pady=3)

boton("Multiplicador Constante", multiplicador_constante).grid(row=2, column=0, pady=3)
boton("Congruencial Lineal", congruencial_lineal).grid(row=2, column=1, pady=3)

boton("Congruencial Multiplicativo", congruencial_multiplicativo).grid(row=3, column=0, pady=3)
boton("Congruencial Aditivo", congruencial_aditivo).grid(row=3, column=1, pady=3)


tk.Label(panel, text="PRUEBAS", bg="#1E293B", fg="white",
         font=("Arial", 12, "bold")).grid(row=4, column=0, columnspan=2, pady=8)

boton("Prueba Media", prueba_media).grid(row=5, column=0, pady=3)
boton("Prueba Varianza", prueba_varianza).grid(row=5, column=1, pady=3)

boton("Chi Cuadrado", chi_cuadrado).grid(row=6, column=0, pady=3)
boton("Kolmogorov", kolmogorov).grid(row=6, column=1, pady=3)


tk.Label(panel, text="DISTRIBUCIONES", bg="#1E293B", fg="white",
         font=("Arial", 12, "bold")).grid(row=7, column=0, columnspan=2, pady=8)

boton("Uniforme", uniforme).grid(row=8, column=0, pady=3)
boton("Exponencial", exponencial).grid(row=8, column=1, pady=3)

boton("Gamma", gamma).grid(row=9, column=0, pady=3)
boton("Erlang", erlang).grid(row=9, column=1, pady=3)

boton("Normal", normal).grid(row=10, column=0, pady=3)
boton("Weibull", weibull).grid(row=10, column=1, pady=3)

boton("Bernoulli", bernoulli).grid(row=11, column=0, pady=3)
boton("Binomial", binomial).grid(row=11, column=1, pady=3)

boton("Poisson", poisson).grid(row=12, column=0, pady=3)
boton("Monte Carlo", montecarlo).grid(row=12, column=1, pady=3)


ventana.mainloop()