"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: graficos.py

Este módulo genera las gráficas de la simulación utilizando
Matplotlib.

Representa la evolución de:
- Sanos
- Infectados
- Recuperados
- Fallecidos
===========================================================
"""

import matplotlib.pyplot as plt


class GraficosCovid:

    def __init__(self):

        self.generaciones = []

        self.sanos = []

        self.infectados = []

        self.recuperados = []

        self.fallecidos = []


    # =====================================================
    # LIMPIAR DATOS
    # =====================================================

    def limpiar(self):

        self.generaciones.clear()

        self.sanos.clear()

        self.infectados.clear()

        self.recuperados.clear()

        self.fallecidos.clear()


    # =====================================================
    # AGREGAR GENERACIÓN
    # =====================================================

    def agregar(self, datos):

        self.generaciones.append(

            datos["generacion"]

        )

        self.sanos.append(

            datos["sanos"]

        )

        self.infectados.append(

            datos["infectados"]

        )

        self.recuperados.append(

            datos["recuperados"]

        )

        self.fallecidos.append(

            datos["fallecidos"]

        )


    # =====================================================
    # CARGAR HISTORIAL COMPLETO
    # =====================================================

    def cargar_historial(self, historial):

        self.limpiar()

        for datos in historial:

            self.agregar(datos)


    # =====================================================
    # TOTAL DE GENERACIONES
    # =====================================================

    def total_generaciones(self):

        return len(self.generaciones)


    # =====================================================
    # EXISTEN DATOS
    # =====================================================

    def tiene_datos(self):

        return len(self.generaciones) > 0


    # =====================================================
    # DEVOLVER DATOS
    # =====================================================

    def obtener_datos(self):

        return {

            "generaciones": self.generaciones,

            "sanos": self.sanos,

            "infectados": self.infectados,

            "recuperados": self.recuperados,

            "fallecidos": self.fallecidos

        }


    # =====================================================
    # GRÁFICA PRINCIPAL
    # =====================================================

    def mostrar(self):

        if not self.tiene_datos():

            print("No existen datos para graficar.")

            return

        plt.figure(figsize=(10,6))

        plt.plot(

            self.generaciones,

            self.sanos,

            label="Sanos"

        )

        plt.plot(

            self.generaciones,

            self.infectados,

            label="Infectados"

        )

        plt.plot(

            self.generaciones,

            self.recuperados,

            label="Recuperados"

        )

        plt.plot(

            self.generaciones,

            self.fallecidos,

            label="Fallecidos"

        )

        plt.title(

            "Evolución de la Simulación COVID"

        )

        plt.xlabel(

            "Generaciones"

        )

        plt.ylabel(

            "Cantidad de Personas"

        )

        plt.grid(True)

        plt.legend()
        plt.tight_layout()

        plt.show()


    # =====================================================
    # GRAFICAR SOLO INFECTADOS
    # =====================================================

    def mostrar_infectados(self):

        if not self.tiene_datos():

            print("No existen datos.")

            return

        plt.figure(figsize=(10, 6))

        plt.plot(

            self.generaciones,

            self.infectados,

            color="red",

            linewidth=2,

            label="Infectados"

        )

        plt.title("Evolución de Infectados")

        plt.xlabel("Generaciones")

        plt.ylabel("Cantidad")

        plt.grid(True)

        plt.legend()

        plt.tight_layout()

        plt.show()


    # =====================================================
    # GUARDAR GRÁFICA
    # =====================================================

    def guardar(self, nombre="grafico_covid.png"):

        if not self.tiene_datos():

            return

        plt.figure(figsize=(10,6))

        plt.plot(

            self.generaciones,

            self.sanos,

            label="Sanos"

        )

        plt.plot(

            self.generaciones,

            self.infectados,

            label="Infectados"

        )

        plt.plot(

            self.generaciones,

            self.recuperados,

            label="Recuperados"

        )

        plt.plot(

            self.generaciones,

            self.fallecidos,

            label="Fallecidos"

        )

        plt.title(

            "Simulación COVID"

        )

        plt.xlabel(

            "Generaciones"

        )

        plt.ylabel(

            "Personas"

        )

        plt.legend()

        plt.grid(True)

        plt.tight_layout()

        plt.savefig(

            nombre,

            dpi=300

        )

        plt.close()


    # =====================================================
    # MOSTRAR RESUMEN
    # =====================================================

    def resumen(self):

        if not self.tiene_datos():

            return

        print()

        print("=" * 40)

        print("RESUMEN DE LA SIMULACIÓN")

        print("=" * 40)

        print()

        print("Generaciones:", self.generaciones[-1])

        print("Sanos:", self.sanos[-1])

        print("Infectados:", self.infectados[-1])

        print("Recuperados:", self.recuperados[-1])

        print("Fallecidos:", self.fallecidos[-1])


# ==========================================================
# PRUEBA DEL MÓDULO
# ==========================================================

if __name__ == "__main__":

    grafico = GraficosCovid()

    for i in range(20):

        grafico.agregar({

            "generacion": i,

            "sanos": 400 - (i * 8),

            "infectados": i * 6,

            "recuperados": i * 2,

            "fallecidos": i

        })

    grafico.resumen()

    grafico.mostrar()

    grafico.mostrar_infectados()

    grafico.guardar()

    print()

    print("Gráfico guardado correctamente.")