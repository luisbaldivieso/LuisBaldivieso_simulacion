import tkinter as tk
from tkinter import ttk, messagebox


# ===========================
# FUNCIONES
# ===========================

def generar():

    tabla.delete(*tabla.get_children())

    try:

        semilla1 = entrada_semilla1.get()
        semilla2 = entrada_semilla2.get()

        if len(semilla1) != 4 or not semilla1.isdigit():
            messagebox.showerror("Error", "La Semilla 1 debe tener 4 dígitos.")
            return

        if len(semilla2) != 4 or not semilla2.isdigit():
            messagebox.showerror("Error", "La Semilla 2 debe tener 4 dígitos.")
            return

        cantidad = int(entrada_cantidad.get())

    except:
        messagebox.showerror("Error", "Datos incorrectos.")
        return

    x0 = int(semilla1)
    x1 = int(semilla2)

    lista_ri = []

    for i in range(cantidad):

        producto = str(x0 * x1).zfill(8)

        centro = producto[2:6]

        xi = int(centro)

        ri = xi / 10000

        lista_ri.append(ri)

        tabla.insert(
            "",
            "end",
            values=(
                i + 1,
                x0,
                x1,
                producto,
                centro,
                xi,
                f"{ri:.4f}"
            )
        )

        x0 = x1
        x1 = xi

    promedio.config(text=f"Promedio: {sum(lista_ri)/len(lista_ri):.4f}")
    minimo.config(text=f"Mínimo: {min(lista_ri):.4f}")
    maximo.config(text=f"Máximo: {max(lista_ri):.4f}")


def limpiar():

    entrada_semilla1.delete(0, tk.END)
    entrada_semilla2.delete(0, tk.END)
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

ventana.title("Productos Medios")

ventana.geometry("1100x650")

ventana.resizable(False, False)


# ===========================
# TITULO
# ===========================

tk.Label(

    ventana,

    text="MÉTODO DE PRODUCTOS MEDIOS",

    font=("Arial",18,"bold")

).pack(pady=10)


# ===========================
# DATOS
# ===========================

frame = tk.Frame(ventana)

frame.pack(pady=10)

tk.Label(frame,text="Semilla 1:",font=("Arial",12)).grid(row=0,column=0,padx=10,pady=5)

entrada_semilla1 = tk.Entry(frame,font=("Arial",12),width=10)

entrada_semilla1.grid(row=0,column=1)

tk.Label(frame,text="Semilla 2:",font=("Arial",12)).grid(row=1,column=0,padx=10,pady=5)

entrada_semilla2 = tk.Entry(frame,font=("Arial",12),width=10)

entrada_semilla2.grid(row=1,column=1)

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

columnas=("Iteración","X0","X1","Producto","Centro","Xi","Ri")

tabla = ttk.Treeview(

    ventana,

    columns=columnas,

    show="headings",

    height=18

)

for c in columnas:

    tabla.heading(c,text=c)

    tabla.column(c,width=130,anchor="center")

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