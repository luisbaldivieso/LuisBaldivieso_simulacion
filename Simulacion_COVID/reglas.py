"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: reglas.py

Este módulo implementa las reglas del autómata celular
para la propagación del COVID.

Cada persona solamente observa a sus 8 vecinos
(Vecindad de Moore).

Las decisiones se toman únicamente usando información
local.
===========================================================
"""

import random

from colores import (
    VACIO,
    SANO,
    INFECTADO,
    RECUPERADO,
    FALLECIDO
)


class ReglasCovid:

    def __init__(
            self,
            probabilidad_contagio=0.40,
            dias_recuperacion=10,
            probabilidad_muerte=0.03):

        self.probabilidad_contagio = probabilidad_contagio
        self.dias_recuperacion = dias_recuperacion
        self.probabilidad_muerte = probabilidad_muerte

        # Guarda cuántos días lleva infectada cada persona
        self.dias_infectado = {}


    # =====================================================
    # CAMBIAR PARÁMETROS
    # =====================================================

    def configurar(
            self,
            probabilidad_contagio=None,
            dias_recuperacion=None,
            probabilidad_muerte=None):

        if probabilidad_contagio is not None:
            self.probabilidad_contagio = probabilidad_contagio

        if dias_recuperacion is not None:
            self.dias_recuperacion = dias_recuperacion

        if probabilidad_muerte is not None:
            self.probabilidad_muerte = probabilidad_muerte


    # =====================================================
    # OBTENER LOS 8 VECINOS (MOORE)
    # =====================================================

    def obtener_vecinos(self, matriz, fila, columna):

        vecinos = []

        filas = len(matriz)
        columnas = len(matriz[0])

        for df in (-1, 0, 1):

            for dc in (-1, 0, 1):

                if df == 0 and dc == 0:
                    continue

                nf = fila + df
                nc = columna + dc

                if 0 <= nf < filas and 0 <= nc < columnas:

                    vecinos.append(matriz[nf][nc])

                else:

                    # Fuera de la matriz = VACIO
                    vecinos.append(VACIO)

        return vecinos


    # =====================================================
    # CONTAR VECINOS INFECTADOS
    # =====================================================

    def contar_infectados(self, matriz, fila, columna):

        vecinos = self.obtener_vecinos(
            matriz,
            fila,
            columna
        )

        contador = 0

        for vecino in vecinos:

            if vecino == INFECTADO:

                contador += 1

        return contador


    # =====================================================
    # CONTAR VECINOS SANOS
    # =====================================================

    def contar_sanos(self, matriz, fila, columna):

        vecinos = self.obtener_vecinos(
            matriz,
            fila,
            columna
        )

        contador = 0

        for vecino in vecinos:

            if vecino == SANO:

                contador += 1

        return contador


    # =====================================================
    # CONTAR VECINOS RECUPERADOS
    # =====================================================

    def contar_recuperados(self, matriz, fila, columna):

        vecinos = self.obtener_vecinos(
            matriz,
            fila,
            columna
        )

        contador = 0

        for vecino in vecinos:

            if vecino == RECUPERADO:

                contador += 1

        return contador


    # =====================================================
    # CONTAR VECINOS FALLECIDOS
    # =====================================================

    def contar_fallecidos(self, matriz, fila, columna):

        vecinos = self.obtener_vecinos(
            matriz,
            fila,
            columna
        )

        contador = 0

        for vecino in vecinos:

            if vecino == FALLECIDO:

                contador += 1

        return contador


    # =====================================================
    # TOTAL DE VECINOS OCUPADOS
    # =====================================================

    def vecinos_ocupados(self, matriz, fila, columna):

        vecinos = self.obtener_vecinos(
            matriz,
            fila,
            columna
        )

        contador = 0

        for vecino in vecinos:

            if vecino != VACIO:

                contador += 1

        return contador


    # =====================================================
    # VERIFICAR SI EXISTE ALGÚN INFECTADO CERCA
    # =====================================================

    def hay_infectado(self, matriz, fila, columna):

        return self.contar_infectados(
            matriz,
            fila,
            columna
        ) > 0


    # =====================================================
    # OBTENER EL ESTADO ACTUAL
    # =====================================================

    def estado_actual(self, matriz, fila, columna):

        return matriz[fila][columna]


    # =====================================================
    # OBTENER CLAVE ÚNICA DE UNA PERSONA
    # =====================================================

    def clave(self, fila, columna):

        return (fila, columna)
        # =====================================================
    # CALCULAR PROBABILIDAD SEGÚN LOS VECINOS
    # =====================================================

    def calcular_probabilidad_contagio(self, vecinos_infectados):

        if vecinos_infectados <= 0:
            return 0.0

        if vecinos_infectados == 1:
            return self.probabilidad_contagio

        if vecinos_infectados == 2:
            return min(0.60, self.probabilidad_contagio + 0.20)

        if vecinos_infectados == 3:
            return min(0.80, self.probabilidad_contagio + 0.40)

        return 1.0


    # =====================================================
    # REGLA DE CONTAGIO
    # =====================================================

    def evaluar_contagio(self, matriz, fila, columna):

        estado = self.estado_actual(
            matriz,
            fila,
            columna
        )

        if estado != SANO:
            return estado

        vecinos = self.contar_infectados(
            matriz,
            fila,
            columna
        )

        if vecinos == 0:
            return SANO

        probabilidad = self.calcular_probabilidad_contagio(
            vecinos
        )

        if random.random() <= probabilidad:

            self.dias_infectado[
                self.clave(fila, columna)
            ] = 0

            return INFECTADO

        return SANO


    # =====================================================
    # AUMENTAR DÍAS DE INFECCIÓN
    # =====================================================

    def incrementar_dias(self, fila, columna):

        clave = self.clave(fila, columna)

        if clave not in self.dias_infectado:

            self.dias_infectado[clave] = 0

        self.dias_infectado[clave] += 1


    # =====================================================
    # OBTENER DÍAS INFECTADO
    # =====================================================

    def obtener_dias(self, fila, columna):

        return self.dias_infectado.get(

            self.clave(fila, columna),

            0

        )


    # =====================================================
    # REGLA DE FALLECIMIENTO
    # =====================================================

    def evaluar_fallecimiento(self, fila, columna):

        if random.random() <= self.probabilidad_muerte:

            clave = self.clave(fila, columna)

            if clave in self.dias_infectado:

                del self.dias_infectado[clave]

            return FALLECIDO

        return INFECTADO


    # =====================================================
    # REGLA DE RECUPERACIÓN
    # =====================================================

    def evaluar_recuperacion(self, fila, columna):

        dias = self.obtener_dias(
            fila,
            columna
        )

        if dias >= self.dias_recuperacion:

            clave = self.clave(fila, columna)

            if clave in self.dias_infectado:

                del self.dias_infectado[clave]

            return RECUPERADO

        return INFECTADO


    # =====================================================
    # EVALUAR PERSONA INFECTADA
    # =====================================================

    def evaluar_infectado(self, fila, columna):

        self.incrementar_dias(
            fila,
            columna
        )

        estado = self.evaluar_fallecimiento(
            fila,
            columna
        )

        if estado == FALLECIDO:

            return FALLECIDO

        return self.evaluar_recuperacion(
            fila,
            columna
        )


    # =====================================================
    # APLICAR LA REGLA COMPLETA
    # =====================================================

    def aplicar_regla(self, matriz, fila, columna):

        estado = self.estado_actual(
            matriz,
            fila,
            columna
        )

        if estado == VACIO:

            return VACIO

        if estado == SANO:

            return self.evaluar_contagio(
                matriz,
                fila,
                columna
            )

        if estado == INFECTADO:

            return self.evaluar_infectado(
                fila,
                columna
            )

        if estado == RECUPERADO:

            return RECUPERADO

        if estado == FALLECIDO:

            return FALLECIDO

        return estado
        # =====================================================
    # ELIMINAR REGISTRO DE UNA PERSONA
    # =====================================================

    def eliminar_registro(self, fila, columna):

        clave = self.clave(fila, columna)

        if clave in self.dias_infectado:

            del self.dias_infectado[clave]


    # =====================================================
    # REINICIAR TODOS LOS CONTADORES
    # =====================================================

    def reiniciar(self):

        self.dias_infectado.clear()


    # =====================================================
    # OBTENER CONFIGURACIÓN ACTUAL
    # =====================================================

    def obtener_configuracion(self):

        return {

            "probabilidad_contagio": self.probabilidad_contagio,

            "dias_recuperacion": self.dias_recuperacion,

            "probabilidad_muerte": self.probabilidad_muerte

        }


    # =====================================================
    # CAMBIAR SOLO LA PROBABILIDAD DE CONTAGIO
    # =====================================================

    def cambiar_probabilidad_contagio(self, valor):

        self.probabilidad_contagio = valor


    # =====================================================
    # CAMBIAR DÍAS DE RECUPERACIÓN
    # =====================================================

    def cambiar_dias_recuperacion(self, dias):

        self.dias_recuperacion = dias


    # =====================================================
    # CAMBIAR PROBABILIDAD DE MUERTE
    # =====================================================

    def cambiar_probabilidad_muerte(self, valor):

        self.probabilidad_muerte = valor


    # =====================================================
    # SABER SI UNA PERSONA ESTÁ REGISTRADA
    # =====================================================

    def esta_registrado(self, fila, columna):

        return self.clave(fila, columna) in self.dias_infectado


    # =====================================================
    # TOTAL DE INFECTADOS EN SEGUIMIENTO
    # =====================================================

    def total_en_seguimiento(self):

        return len(self.dias_infectado)


    # =====================================================
    # DEVOLVER TODOS LOS CONTADORES
    # =====================================================

    def obtener_contadores(self):

        return dict(self.dias_infectado)


    # =====================================================
    # CARGAR CONTADORES
    # =====================================================

    def cargar_contadores(self, datos):

        self.dias_infectado = dict(datos)


    # =====================================================
    # MOSTRAR CONTADORES
    # =====================================================

    def mostrar_contadores(self):

        print()

        print("PERSONAS INFECTADAS")

        print("---------------------------")

        if not self.dias_infectado:

            print("No existen registros.")

            return

        for posicion, dias in self.dias_infectado.items():

            print(

                f"Posición {posicion} -> {dias} días"

            )


# ==========================================================
# PRUEBA DEL MÓDULO
# ==========================================================

if __name__ == "__main__":

    from poblacion import Poblacion

    poblacion = Poblacion(10, 10)

    poblacion.generar(

        infectados=8

    )

    reglas = ReglasCovid(

        probabilidad_contagio=0.40,

        dias_recuperacion=8,

        probabilidad_muerte=0.05

    )

    print()

    print("Configuración")

    print("--------------------")

    print(

        reglas.obtener_configuracion()

    )

    print()

    print("Matriz inicial")

    print("--------------------")

    poblacion.mostrar()

    print()

    print("Ejemplo de vecinos")

    print("--------------------")

    vecinos = reglas.contar_infectados(

        poblacion.obtener_matriz(),

        5,

        5

    )

    print(

        "Vecinos infectados:",

        vecinos

    )

    print()

    print("Archivo reglas.py cargado correctamente.")