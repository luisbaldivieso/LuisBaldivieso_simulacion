import tkinter as tk
from tkinter import ttk, messagebox


# ===========================
# FUNCIONES
# ===========================

def generar():

    tabla.delete(*tabla.get_children())

    try:

        semilla = int(entrada_semilla.get())
        a = int(entrada_a.get())
        c = int(entrada_c.get())
        m = int(entrada_m.get())
        cantidad = int(entrada_cantidad.get())

    except:
        messagebox.showerror("Error", "Ingrese solamente números.")
        return

    if m <= 0:
        messagebox.showerror("Error", "El módulo debe ser mayor que cero.")
        return

    x = semilla
    lista_ri = []

    for i in range(cantidad):

        xn = (a * x + c) % m

        ri = xn / m

        lista_ri.append(ri)

        tabla.insert(
            "",
            "end",
            values=(
                i + 1,
                x,
                a,
                c,
                m,
                xn,
                f"{ri:.6f}"
            )
        )

        x = xn

    promedio.config(text=f"Promedio: {sum(lista_ri)/len(lista_ri):.6f}")
    minimo.config(text=f"Mínimo: {min(lista_ri):.6f}")
    maximo.config(text=f"Máximo: {max(lista_ri):.6f}")


def limpiar():

    entrada_semilla.delete(0, tk.END)
    entrada_a.delete(0, tk.END)
    entrada_c.delete(0, tk.END)
    entrada_m.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)

    tabla.delete(*tabla.get_children())

    promedio.config(text="Promedio:")
    minimo.config(text="Mínimo:")
    maximo.config(text="Máximo:")


def salir():
    ventana.destroy()


# ===========================
# VENTANA
# ===========================

ventana = tk.Tk()

ventana.title("Congruencial Lineal")

ventana.geometry("1200x650")

ventana.resizable(False, False)


# ===========================
# TITULO
# ===========================

tk.Label(
    ventana,
    text="MÉTODO CONGRUENCIAL LINEAL",
    font=("Arial",18,"bold")
).pack(pady=10)


# ===========================
# ENTRADAS
# ===========================

frame = tk.Frame(ventana)
frame.pack(pady=10)

tk.Label(frame,text="Semilla (X0):",font=("Arial",12)).grid(row=0,column=0,padx=10,pady=5)
entrada_semilla = tk.Entry(frame,font=("Arial",12),width=10)
entrada_semilla.grid(row=0,column=1)

tk.Label(frame,text="Multiplicador (a):",font=("Arial",12)).grid(row=1,column=0,padx=10,pady=5)
entrada_a = tk.Entry(frame,font=("Arial",12),width=10)
entrada_a.grid(row=1,column=1)

tk.Label(frame,text="Incremento (c):",font=("Arial",12)).grid(row=2,column=0,padx=10,pady=5)
entrada_c = tk.Entry(frame,font=("Arial",12),width=10)
entrada_c.grid(row=2,column=1)

tk.Label(frame,text="Módulo (m):",font=("Arial",12)).grid(row=3,column=0,padx=10,pady=5)
entrada_m = tk.Entry(frame,font=("Arial",12),width=10)
entrada_m.grid(row=3,column=1)

tk.Label(frame,text="Cantidad:",font=("Arial",12)).grid(row=4,column=0,padx=10,pady=5)
entrada_cantidad = tk.Entry(frame,font=("Arial",12),width=10)
entrada_cantidad.grid(row=4,column=1)


tk.Button(
    frame,
    text="Generar",
    bg="green",
    fg="white",
    font=("Arial",11,"bold"),
    command=generar
).grid(row=0,column=2,padx=15)

tk.Button(
    frame,
    text="Limpiar",
    bg="orange",
    fg="white",
    font=("Arial",11,"bold"),
    command=limpiar
).grid(row=2,column=2,padx=15)

tk.Button(
    frame,
    text="Salir",
    bg="red",
    fg="white",
    font=("Arial",11,"bold"),
    command=salir
).grid(row=4,column=2,padx=15)


# ===========================
# TABLA
# ===========================

columnas = (
    "Iteración",
    "Xi",
    "a",
    "c",
    "m",
    "Xi+1",
    "Ri"
)

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=16
)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=150, anchor="center")

tabla.pack()


# ===========================
# ESTADÍSTICAS
# ===========================

frame2 = tk.Frame(ventana)
frame2.pack(pady=10)

promedio = tk.Label(frame2,text="Promedio:",font=("Arial",12))
promedio.pack()

minimo = tk.Label(frame2,text="Mínimo:",font=("Arial",12))
minimo.pack()

maximo = tk.Label(frame2,text="Máximo:",font=("Arial",12))
maximo.pack()


ventana.mainloop()