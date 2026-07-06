import tkinter as tk
import subprocess
import os

# =====================================
# FUNCIÓN GENERAL PARA ABRIR MÓDULOS
# =====================================

def abrir_script(ruta):
    try:
        subprocess.Popen(["python", ruta])
    except Exception as e:
        print(f"Error al abrir {ruta}: {e}")


# =====================================
# RUTAS DEL PROYECTO
# =====================================

BASE_PATH = r"C:\Users\LENOVO\Desktop\Simulacion\proyecto_final"


def abrir_calculadora():
    abrir_script(os.path.join(BASE_PATH, "Calculadora", "calculadora.py"))


def abrir_ruleta():
    abrir_script(os.path.join(BASE_PATH, "ruleta", "ruleta.py"))


def abrir_covid():
    abrir_script(os.path.join(BASE_PATH, "Simulacion_COVID", "covid.py"))


def abrir_quinoa():
    abrir_script(os.path.join(BASE_PATH, "quinoa", "quinoa.py"))


def salir():
    ventana.destroy()


# =====================================
# VENTANA PRINCIPAL
# =====================================

ventana = tk.Tk()
ventana.title("Sistema de Simulación")
ventana.geometry("900x600")
ventana.resizable(False, False)
ventana.configure(bg="#0F172A")


# =====================================
# ENCABEZADO
# =====================================

tk.Label(
    ventana,
    text="SISTEMA INTEGRADO DE SIMULACIÓN",
    font=("Arial", 24, "bold"),
    fg="#FFFFFF",
    bg="#0F172A"
).pack(pady=(20,5))

tk.Label(
    ventana,
    text="Proyecto Final de Simulación",
    font=("Arial", 15),
    fg="#CBD5E1",
    bg="#0F172A"
).pack()

tk.Label(
    ventana,
    text="Aplicación desarrollada para la ejecución de diferentes modelos de simulación.",
    font=("Arial", 11),
    fg="#94A3B8",
    bg="#0F172A"
).pack(pady=(5,25))


# =====================================
# PANEL PRINCIPAL
# =====================================

frame = tk.Frame(
    ventana,
    bg="#1E293B",
    bd=4,
    relief="groove"
)
frame.pack(pady=10, ipadx=20, ipady=20)


tk.Label(
    frame,
    text="MENÚ PRINCIPAL",
    font=("Arial",18,"bold"),
    bg="#1E293B",
    fg="white"
).pack(pady=(0,20))


# =====================================
# BOTONES
# =====================================

tk.Button(
    frame,
    text="📊  Calculadora de Simulación",
    font=("Arial",16,"bold"),
    width=32,
    height=2,
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    cursor="hand2",
    command=abrir_calculadora
).pack(pady=8)


tk.Button(
    frame,
    text="🎲  Ruleta Monte Carlo",
    font=("Arial",16,"bold"),
    width=32,
    height=2,
    bg="#16A34A",
    fg="white",
    activebackground="#15803D",
    cursor="hand2",
    command=abrir_ruleta
).pack(pady=8)


tk.Button(
    frame,
    text="🦠  Simulación COVID-19",
    font=("Arial",16,"bold"),
    width=32,
    height=2,
    bg="#DC2626",
    fg="white",
    activebackground="#B91C1C",
    cursor="hand2",
    command=abrir_covid
).pack(pady=8)


tk.Button(
    frame,
    text="🌾  Simulación de Producción de Quinoa",
    font=("Arial",16,"bold"),
    width=32,
    height=2,
    bg="#D97706",
    fg="white",
    activebackground="#B45309",
    cursor="hand2",
    command=abrir_quinoa
).pack(pady=8)


# =====================================
# BOTÓN SALIR
# =====================================

tk.Button(
    ventana,
    text="Cerrar Aplicación",
    font=("Arial",13,"bold"),
    width=22,
    height=2,
    bg="#111827",
    fg="white",
    activebackground="#374151",
    cursor="hand2",
    command=salir
).pack(pady=25)


# =====================================
# PIE DE PÁGINA
# =====================================

tk.Label(
    ventana,
    text="Desarrollado por Luis Baldivieso",
    font=("Arial",11,"bold"),
    fg="#E2E8F0",
    bg="#0F172A"
).pack()

tk.Label(
    ventana,
    text="Proyecto Final • Ingeniería de Sistemas • Versión 1.0",
    font=("Arial",10),
    fg="#94A3B8",
    bg="#0F172A"
).pack(pady=(2,10))


ventana.mainloop()