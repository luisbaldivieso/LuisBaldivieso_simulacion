"""
interfaz.py
Interfaz gráfica del simulador de la planta procesadora de quinua.
"""

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from simulador import rk4
from graficos import Graficos
from reportes import exportar_csv, exportar_imagen
from utilidades import validar_numero, mostrar_error


class Ventana(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title("Simulador Planta Procesadora de Quinua")
        self.geometry("1200x800")

        self.tiempo = None
        self.stock = None
        self.procesamiento = None

        self.graficos = Graficos()

        self.crear_widgets()

    def crear_widgets(self):

        panel = ttk.Frame(self)
        panel.pack(side="left", fill="y", padx=10, pady=10)

        datos = [

            ("Stock inicial", "10000"),
            ("Procesamiento inicial", "2000"),
            ("Alpha", "0.05"),
            ("Beta", "0.00001"),
            ("Delta", "0.00002"),
            ("Gamma", "0.03"),
            ("Tiempo total", "120"),
            ("Paso dt", "0.5")

        ]

        self.entradas = {}

        for texto, valor in datos:

            ttk.Label(panel, text=texto).pack(anchor="w")

            e = ttk.Entry(panel, width=20)

            e.insert(0, valor)

            e.pack(pady=3)

            self.entradas[texto] = e

        ttk.Button(

            panel,
            text="Ejecutar simulación",
            command=self.simular

        ).pack(fill="x", pady=10)

        ttk.Button(

            panel,
            text="Exportar CSV",
            command=self.exportar_csv

        ).pack(fill="x", pady=5)

        ttk.Button(

            panel,
            text="Guardar gráfico",
            command=self.exportar_imagen

        ).pack(fill="x", pady=5)

        self.canvas = FigureCanvasTkAgg(

            self.graficos.obtener_figura(),
            master=self

        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(

            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10

        )

    def simular(self):

        valores = []

        for entrada in self.entradas.values():

            texto = entrada.get()

            if not validar_numero(texto):

                mostrar_error("Todos los valores deben ser numéricos.")

                return

            valores.append(float(texto))

        (
            x0,
            y0,
            alpha,
            beta,
            delta,
            gamma,
            tiempo_total,
            dt

        ) = valores

        self.tiempo, self.stock, self.procesamiento = rk4(

            x0,
            y0,
            alpha,
            beta,
            delta,
            gamma,
            tiempo_total,
            dt

        )

        self.graficos.actualizar(

            self.tiempo,
            self.stock,
            self.procesamiento

        )

        self.canvas.draw()

    def exportar_csv(self):

        exportar_csv(

            self.tiempo,
            self.stock,
            self.procesamiento

        )

    def exportar_imagen(self):

        exportar_imagen(

            self.graficos.obtener_figura()

        )