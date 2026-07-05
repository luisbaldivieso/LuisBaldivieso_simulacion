"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: poblacion.py

Este módulo se encarga de crear la población inicial de la
simulación mediante una matriz bidimensional.

Cada posición representa una persona.

Estados disponibles:

0 = Vacío
1 = Sano
2 = Infectado
3 = Recuperado
4 = Fallecido
===========================================================
"""

import random
import copy

from colores import (
    VACIO,
    SANO,
    INFECTADO,
    RECUPERADO,
    FALLECIDO
)


class Poblacion:

    def __init__(self, filas=30, columnas=30):

        self.filas = filas
        self.columnas = columnas

        self.matriz = []

        self.crear_poblacion()


    # =====================================================
    # CREA TODA LA MATRIZ
    # =====================================================

    def crear_poblacion(self):

        self.matriz = []

        for i in range(self.filas):

            fila = []

            for j in range(self.columnas):

                fila.append(SANO)

            self.matriz.append(fila)


    # =====================================================
    # REINICIAR POBLACIÓN
    # =====================================================

    def reiniciar(self):

        self.crear_poblacion()


    # =====================================================
    # OBTENER MATRIZ
    # =====================================================

    def obtener_matriz(self):

        return self.matriz


    # =====================================================
    # DEVOLVER COPIA DE LA MATRIZ
    # =====================================================

    def copiar_matriz(self):

        return copy.deepcopy(self.matriz)


    # =====================================================
    # OBTENER ESTADO DE UNA CELDA
    # =====================================================

    def obtener_estado(self, fila, columna):

        if (
            fila < 0
            or fila >= self.filas
            or columna < 0
            or columna >= self.columnas
        ):

            return VACIO

        return self.matriz[fila][columna]


    # =====================================================
    # CAMBIAR ESTADO
    # =====================================================

    def cambiar_estado(self, fila, columna, estado):

        if (
            fila < 0
            or fila >= self.filas
            or columna < 0
            or columna >= self.columnas
        ):

            return

        self.matriz[fila][columna] = estado


    # =====================================================
    # LLENAR TODA LA MATRIZ CON UN ESTADO
    # =====================================================

    def llenar(self, estado=SANO):

        for i in range(self.filas):

            for j in range(self.columnas):

                self.matriz[i][j] = estado


    # =====================================================
    # VERIFICAR SI UNA POSICIÓN ES VÁLIDA
    # =====================================================

    def posicion_valida(self, fila, columna):

        return (
            0 <= fila < self.filas
            and
            0 <= columna < self.columnas
        )


    # =====================================================
    # OBTENER DIMENSIONES
    # =====================================================

    def dimensiones(self):

        return self.filas, self.columnas


    # =====================================================
    # CAMBIAR TAMAÑO DE LA MATRIZ
    # =====================================================

    def cambiar_tamano(self, filas, columnas):

        self.filas = filas
        self.columnas = columnas

        self.crear_poblacion()


    # =====================================================
    # VACIAR MATRIZ
    # =====================================================

    def vaciar(self):

        self.llenar(VACIO)


    # =====================================================
    # CONVERTIR TODOS EN SANOS
    # =====================================================

    def todos_sanos(self):

        self.llenar(SANO)


    # =====================================================
    # OBTENER UNA FILA
    # =====================================================

    def obtener_fila(self, fila):

        if fila < 0 or fila >= self.filas:

            return None

        return self.matriz[fila]


    # =====================================================
    # OBTENER UNA COLUMNA
    # =====================================================

    def obtener_columna(self, columna):

        if columna < 0 or columna >= self.columnas:

            return None

        datos = []

        for fila in range(self.filas):

            datos.append(self.matriz[fila][columna])

        return datos
        # =====================================================
    # COLOCAR INFECTADOS ALEATORIOS
    # =====================================================

    def colocar_infectados(self, cantidad):

        cantidad = min(cantidad, self.filas * self.columnas)

        colocados = 0

        while colocados < cantidad:

            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)

            if self.matriz[fila][columna] == SANO:

                self.matriz[fila][columna] = INFECTADO
                colocados += 1


    # =====================================================
    # COLOCAR RECUPERADOS ALEATORIOS
    # =====================================================

    def colocar_recuperados(self, cantidad):

        cantidad = min(cantidad, self.filas * self.columnas)

        colocados = 0

        while colocados < cantidad:

            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)

            if self.matriz[fila][columna] == SANO:

                self.matriz[fila][columna] = RECUPERADO
                colocados += 1


    # =====================================================
    # COLOCAR FALLECIDOS ALEATORIOS
    # =====================================================

    def colocar_fallecidos(self, cantidad):

        cantidad = min(cantidad, self.filas * self.columnas)

        colocados = 0

        while colocados < cantidad:

            fila = random.randint(0, self.filas - 1)
            columna = random.randint(0, self.columnas - 1)

            if self.matriz[fila][columna] == SANO:

                self.matriz[fila][columna] = FALLECIDO
                colocados += 1


    # =====================================================
    # CONTAR UN ESTADO
    # =====================================================

    def contar_estado(self, estado):

        contador = 0

        for fila in self.matriz:

            for celda in fila:

                if celda == estado:

                    contador += 1

        return contador


    # =====================================================
    # CONTAR TODOS LOS ESTADOS
    # =====================================================

    def estadisticas(self):

        return {

            "vacios": self.contar_estado(VACIO),

            "sanos": self.contar_estado(SANO),

            "infectados": self.contar_estado(INFECTADO),

            "recuperados": self.contar_estado(RECUPERADO),

            "fallecidos": self.contar_estado(FALLECIDO)

        }


    # =====================================================
    # MOSTRAR MATRIZ EN CONSOLA
    # =====================================================

    def mostrar(self):

        for fila in self.matriz:

            print(" ".join(str(x) for x in fila))

        print()


    # =====================================================
    # GENERAR POBLACIÓN NUEVA
    # =====================================================

    def generar(self,
                 infectados=5,
                 recuperados=0,
                 fallecidos=0):

        self.todos_sanos()

        self.colocar_infectados(infectados)

        if recuperados > 0:

            self.colocar_recuperados(recuperados)

        if fallecidos > 0:

            self.colocar_fallecidos(fallecidos)


    # =====================================================
    # OBTENER LISTA DE PERSONAS
    # =====================================================

    def personas(self):

        lista = []

        for i in range(self.filas):

            for j in range(self.columnas):

                lista.append(

                    (
                        i,
                        j,
                        self.matriz[i][j]
                    )

                )

        return lista


    # =====================================================
    # REEMPLAZAR MATRIZ
    # =====================================================

    def reemplazar(self, nueva_matriz):

        self.matriz = copy.deepcopy(nueva_matriz)


    # =====================================================
    # TAMAÑO TOTAL
    # =====================================================

    def total_personas(self):

        return self.filas * self.columnas


    # =====================================================
    # ELIMINAR TODA LA POBLACIÓN
    # =====================================================

    def limpiar(self):

        self.vaciar()


# ==========================================================
# PRUEBA DEL MÓDULO
# ==========================================================

if __name__ == "__main__":

    poblacion = Poblacion(15, 15)

    poblacion.generar(
        infectados=10,
        recuperados=3,
        fallecidos=2
    )

    poblacion.mostrar()

    print()

    print("Estadísticas")

    print("---------------------")

    datos = poblacion.estadisticas()

    for clave, valor in datos.items():

        print(f"{clave}: {valor}")