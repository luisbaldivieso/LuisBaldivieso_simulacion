"""
utilidades.py
Funciones auxiliares del proyecto.
"""

from tkinter import messagebox


def validar_numero(valor):

    try:
        float(valor)
        return True

    except ValueError:
        return False


def mostrar_error(mensaje):

    messagebox.showerror(
        "Error",
        mensaje
    )


def mostrar_info(mensaje):

    messagebox.showinfo(
        "Información",
        mensaje
    )


def redondear(numero):

    return round(numero,2)