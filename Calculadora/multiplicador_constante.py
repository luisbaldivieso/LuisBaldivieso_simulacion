import tkinter as tk
from tkinter import ttk, messagebox


# ===========================
# FUNCIONES
# ===========================

def generar():

    tabla.delete(*tabla.get_children())

    try:

        semilla = entrada_semilla.get()
        constante = entrada_constante.get()

        if len(semilla) != 4 or not semilla.isdigit():
            messagebox.showerror("Error", "La semilla debe tener 4 dígitos.")
            return

        if len(constante) != 4 or not constante.isdigit():
            messagebox.showerror("Error", "La constante debe tener 4 dígitos.")
            return

        cantidad = int(entrada_cantidad.get())

    except:
        messagebox.showerror("Error", "Datos incorrectos.")
        return

    x = int(semilla)
    c = int(constante)

    lista_ri = []

    for i in range(cantidad):

        producto = str(x * c).zfill(8)

        centro = producto[2:6]

        x = int(centro)

        ri = x / 10000

        lista_ri.append(ri)

        tabla.insert(
            "",
            "end",
            values=(
                i + 1,
                producto,
                centro,
                x,
                f"{ri:.4f}"
            )
        )

    promedio.config(text=f"Promedio: {sum(lista_ri)/len(lista_ri):.4f}")
    minimo.config(text=f"Mínimo: {min(lista_ri):.4f}")
    maximo.config(text=f"Máximo: {max(lista_ri):.4f}")


def limpiar():

    entrada_semilla.delete(0, tk.END)
    entrada_constante.delete(0, tk.END)
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

ventana.title("Multiplicador Constante")

ventana.geometry("950x620")

ventana.resizable(False, False)


# ===========================
# TITULO
# ===========================

tk.Label(
    ventana,
    text="MÉTODO DEL MULTIPLICADOR CONSTANTE",
    font=("Arial",18,"bold")
).pack(pady=10)


# ===========================
# DATOS
# ===========================

frame = tk.Frame(ventana)

frame.pack(pady=10)

tk.Label(frame,text="Semilla:",font=("Arial",12)).grid(row=0,column=0,padx=10,pady=5)

entrada_semilla = tk.Entry(frame,font=("Arial",12),width=10)

entrada_semilla.grid(row=0,column=1)

tk.Label(frame,text="Constante:",font=("Arial",12)).grid(row=1,column=0,padx=10,pady=5)

entrada_constante = tk.Entry(frame,font=("Arial",12),width=10)

entrada_constante.grid(row=1,column=1)

tk.Label(frame,text="Cantidad:",font=("Arial",12)).grid(row=2,column=0,padx=10,pady=5)

entrada_cantidad = tk.Entry(frame,font=("Arial",12),width=10)

entrada_cantidad.grid(row=2,column=1)


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
).grid(row=1,column=2,padx=15)


tk.Button(
    frame,
    text="Salir",
    bg="red",
    fg="white",
    font=("Arial",11,"bold"),
    command=salir
).grid(row=2,column=2,padx=15)


# ===========================
# TABLA
# ===========================

columnas=("Iteración","Producto","Centro","Xi","Ri")

tabla = ttk.Treeview(
    ventana,
    columns=columnas,
    show="headings",
    height=18
)

for c in columnas:
    tabla.heading(c,text=c)
    tabla.column(c,width=170,anchor="center")

tabla.pack()


# ===========================
# ESTADISTICAS
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