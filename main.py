import tkinter as tk
from tkinter import messagebox

# ===============================
# FUNCIONES
# ===============================

def abrir_calculadora():
    messagebox.showinfo("Calculadora", "Próximamente estará disponible.")

def abrir_ruleta():
    messagebox.showinfo("Monte Carlo", "Próximamente estará disponible.")

def abrir_covid():
    messagebox.showinfo("COVID", "Próximamente estará disponible.")

def salir():
    ventana.destroy()


# ===============================
# VENTANA PRINCIPAL
# ===============================

ventana = tk.Tk()
ventana.title("SALVANDO LA MATERIA")
ventana.geometry("900x600")
ventana.resizable(False, False)
ventana.configure(bg="#0F172A")


# ===============================
# TITULO
# ===============================

titulo = tk.Label(
    ventana,
    text="SIMULADOR DE SIMULACIÓN",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#0F172A"
)
titulo.pack(pady=20)

subtitulo = tk.Label(
    ventana,
    text="Proyecto Final - Salvando la Materia",
    font=("Arial", 14),
    fg="white",
    bg="#0F172A"
)
subtitulo.pack()


# ===============================
# MARCO CENTRAL
# ===============================

frame = tk.Frame(
    ventana,
    bg="#1E293B",
    bd=3,
    relief="ridge"
)
frame.pack(pady=50)


# ===============================
# BOTONES
# ===============================

btn1 = tk.Button(
    frame,
    text="📊 CALCULADORA DE SIMULACIÓN",
    font=("Arial",16,"bold"),
    width=35,
    height=2,
    bg="#2563EB",
    fg="white",
    command=abrir_calculadora
)

btn1.pack(pady=15)


btn2 = tk.Button(
    frame,
    text="🎲 RULETA MONTE CARLO",
    font=("Arial",16,"bold"),
    width=35,
    height=2,
    bg="#16A34A",
    fg="white",
    command=abrir_ruleta
)

btn2.pack(pady=15)


btn3 = tk.Button(
    frame,
    text="🦠 SIMULACIÓN COVID",
    font=("Arial",16,"bold"),
    width=35,
    height=2,
    bg="#DC2626",
    fg="white",
    command=abrir_covid
)

btn3.pack(pady=15)


btn4 = tk.Button(
    ventana,
    text="❌ SALIR",
    font=("Arial",14,"bold"),
    width=20,
    bg="#111827",
    fg="white",
    command=salir
)

btn4.pack(pady=20)


# ===============================
# PIE
# ===============================

pie = tk.Label(
    ventana,
    text="Versión 1.0 | Proyecto de Simulación",
    font=("Arial",10),
    fg="white",
    bg="#0F172A"
)

pie.pack(side="bottom", pady=10)


ventana.mainloop()