"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: estadisticas.py

Este módulo administra todas las estadísticas de la
simulación.

No modifica la simulación.

Únicamente analiza los resultados de cada generación.
===========================================================
"""

from colores import (
    VACIO,
    SANO,
    INFECTADO,
    RECUPERADO,
    FALLECIDO
)


class EstadisticasCovid:

    def __init__(self):

        self.historial = []


    # =====================================================
    # LIMPIAR HISTORIAL
    # =====================================================

    def limpiar(self):

        self.historial.clear()


    # =====================================================
    # CONTAR UN ESTADO
    # =====================================================

    def contar_estado(self, matriz, estado):

        contador = 0

        for fila in matriz:

            for celda in fila:

                if celda == estado:

                    contador += 1

        return contador


    # =====================================================
    # TOTAL DE PERSONAS
    # =====================================================

    def total_personas(self, matriz):

        total = 0

        for fila in matriz:

            total += len(fila)

        return total


    # =====================================================
    # PERSONAS SANAS
    # =====================================================

    def sanos(self, matriz):

        return self.contar_estado(

            matriz,

            SANO

        )


    # =====================================================
    # PERSONAS INFECTADAS
    # =====================================================

    def infectados(self, matriz):

        return self.contar_estado(

            matriz,

            INFECTADO

        )


    # =====================================================
    # PERSONAS RECUPERADAS
    # =====================================================

    def recuperados(self, matriz):

        return self.contar_estado(

            matriz,

            RECUPERADO

        )


    # =====================================================
    # PERSONAS FALLECIDAS
    # =====================================================

    def fallecidos(self, matriz):

        return self.contar_estado(

            matriz,

            FALLECIDO

        )


    # =====================================================
    # ESPACIOS VACÍOS
    # =====================================================

    def vacios(self, matriz):

        return self.contar_estado(

            matriz,

            VACIO

        )


    # =====================================================
    # CALCULAR PORCENTAJE
    # =====================================================

    def porcentaje(self, cantidad, total):

        if total == 0:

            return 0

        return round(

            (cantidad / total) * 100,

            2

        )
            # =====================================================
    # GENERAR ESTADÍSTICAS COMPLETAS
    # =====================================================

    def generar(self, matriz, generacion=0):

        total = self.total_personas(matriz)

        datos = {

            "generacion": generacion,

            "total": total,

            "vacios": self.vacios(matriz),

            "sanos": self.sanos(matriz),

            "infectados": self.infectados(matriz),

            "recuperados": self.recuperados(matriz),

            "fallecidos": self.fallecidos(matriz)

        }

        datos["porcentaje_sanos"] = self.porcentaje(
            datos["sanos"],
            total
        )

        datos["porcentaje_infectados"] = self.porcentaje(
            datos["infectados"],
            total
        )

        datos["porcentaje_recuperados"] = self.porcentaje(
            datos["recuperados"],
            total
        )

        datos["porcentaje_fallecidos"] = self.porcentaje(
            datos["fallecidos"],
            total
        )

        datos["porcentaje_vacios"] = self.porcentaje(
            datos["vacios"],
            total
        )

        return datos


    # =====================================================
    # GUARDAR HISTORIAL
    # =====================================================

    def guardar(self, matriz, generacion):

        datos = self.generar(
            matriz,
            generacion
        )

        self.historial.append(datos)


    # =====================================================
    # OBTENER HISTORIAL
    # =====================================================

    def obtener_historial(self):

        return self.historial


    # =====================================================
    # ÚLTIMO REGISTRO
    # =====================================================

    def ultimo(self):

        if len(self.historial) == 0:

            return None

        return self.historial[-1]


    # =====================================================
    # TOTAL DE GENERACIONES
    # =====================================================

    def total_generaciones(self):

        return len(self.historial)


    # =====================================================
    # OBTENER UNA GENERACIÓN
    # =====================================================

    def obtener_generacion(self, indice):

        if indice < 0:

            return None

        if indice >= len(self.historial):

            return None

        return self.historial[indice]


    # =====================================================
    # EXISTE HISTORIAL
    # =====================================================

    def tiene_historial(self):

        return len(self.historial) > 0


    # =====================================================
    # ELIMINAR ÚLTIMO REGISTRO
    # =====================================================

    def eliminar_ultimo(self):

        if self.tiene_historial():

            self.historial.pop()


    # =====================================================
    # REEMPLAZAR HISTORIAL
    # =====================================================

    def cargar_historial(self, historial):

        self.historial = historial.copy()


    # =====================================================
    # EXPORTAR HISTORIAL
    # =====================================================

    def exportar(self):

        return self.historial.copy()