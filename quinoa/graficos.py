"""
graficos.py
---------------------------------------
Funciones para generar los gráficos
del simulador de la planta procesadora
de quinua.
"""

from matplotlib.figure import Figure


class Graficos:

    def __init__(self):
        """
        Crea la figura con tres gráficos.
        """

        self.figura = Figure(
            figsize=(10, 7),
            dpi=100,
            facecolor="white"
        )

        self.ax_stock = self.figura.add_subplot(311)
        self.ax_procesamiento = self.figura.add_subplot(312)
        self.ax_comparacion = self.figura.add_subplot(313)

        self.figura.tight_layout(pad=3)

    def actualizar(self, tiempo, stock, procesamiento):
        """
        Actualiza los tres gráficos.
        """

        # Limpiar gráficos anteriores

        self.ax_stock.clear()
        self.ax_procesamiento.clear()
        self.ax_comparacion.clear()

        # -----------------------------
        # Gráfico 1
        # -----------------------------

        self.ax_stock.plot(
            tiempo,
            stock,
            color="green",
            linewidth=2
        )

        self.ax_stock.set_title("🌾 Evolución del Stock de Quinua")
        self.ax_stock.set_ylabel("Kilogramos")
        self.ax_stock.grid(True, alpha=0.3)

        # -----------------------------
        # Gráfico 2
        # -----------------------------

        self.ax_procesamiento.plot(
            tiempo,
            procesamiento,
            color="orange",
            linewidth=2
        )

        self.ax_procesamiento.set_title("🏭 Nivel de Procesamiento")
        self.ax_procesamiento.set_ylabel("kg/día")
        self.ax_procesamiento.grid(True, alpha=0.3)

        # -----------------------------
        # Gráfico 3
        # -----------------------------

        self.ax_comparacion.plot(
            tiempo,
            stock,
            label="Stock",
            linewidth=2
        )

        self.ax_comparacion.plot(
            tiempo,
            procesamiento,
            label="Procesamiento",
            linewidth=2
        )

        self.ax_comparacion.set_title("📈 Comparación General")
        self.ax_comparacion.set_xlabel("Tiempo (días)")
        self.ax_comparacion.grid(True, alpha=0.3)
        self.ax_comparacion.legend()

    def obtener_figura(self):
        """
        Devuelve la figura completa para
        mostrarla en Tkinter.
        """

        return self.figura

    def guardar(self, ruta):
        """
        Guarda la figura como imagen.
        """

        self.figura.savefig(
            ruta,
            dpi=300,
            bbox_inches="tight"
        )