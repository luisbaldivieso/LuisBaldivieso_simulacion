"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: motor_covid.py

Motor principal del autómata celular.

Este módulo es responsable de evolucionar la población
de una generación a otra utilizando las reglas definidas
en reglas.py.

G0 -> G1 -> G2 -> G3 -> ...
===========================================================
"""

import copy

from poblacion import Poblacion
from reglas import ReglasCovid


class MotorCovid:

    def __init__(
            self,
            filas=30,
            columnas=30,
            infectados_iniciales=5,
            probabilidad_contagio=0.40,
            dias_recuperacion=10,
            probabilidad_muerte=0.03):

        # ==========================================
        # CREAR POBLACIÓN
        # ==========================================

        self.poblacion = Poblacion(
            filas,
            columnas
        )

        self.poblacion.generar(
            infectados=infectados_iniciales
        )

        # ==========================================
        # REGLAS
        # ==========================================

        self.reglas = ReglasCovid(
            probabilidad_contagio,
            dias_recuperacion,
            probabilidad_muerte
        )

        # ==========================================
        # CONTADOR DE GENERACIONES
        # ==========================================

        self.generacion = 0

        # ==========================================
        # HISTORIAL
        # ==========================================

        self.historial = []

        self.guardar_estadisticas()


    # =====================================================
    # OBTENER MATRIZ ACTUAL
    # =====================================================

    def obtener_matriz(self):

        return self.poblacion.obtener_matriz()


    # =====================================================
    # COPIA DE MATRIZ
    # =====================================================

    def copiar_matriz(self):

        return copy.deepcopy(

            self.obtener_matriz()

        )


    # =====================================================
    # CREAR MATRIZ VACÍA
    # =====================================================

    def nueva_matriz(self):

        filas = self.poblacion.filas
        columnas = self.poblacion.columnas

        matriz = []

        for i in range(filas):

            fila = []

            for j in range(columnas):

                fila.append(

                    self.obtener_matriz()[i][j]

                )

            matriz.append(fila)

        return matriz


    # =====================================================
    # GUARDAR ESTADÍSTICAS
    # =====================================================

    def guardar_estadisticas(self):

        datos = self.poblacion.estadisticas()

        datos["generacion"] = self.generacion

        self.historial.append(

            datos

        )


    # =====================================================
    # OBTENER HISTORIAL
    # =====================================================

    def obtener_historial(self):

        return self.historial


    # =====================================================
    # GENERACIÓN ACTUAL
    # =====================================================

    def obtener_generacion(self):

        return self.generacion


    # =====================================================
    # REINICIAR SIMULACIÓN
    # =====================================================

    def reiniciar(self):

        filas = self.poblacion.filas
        columnas = self.poblacion.columnas

        infectados = self.poblacion.contar_estado(2)

        self.poblacion = Poblacion(

            filas,

            columnas

        )

        self.poblacion.generar(

            infectados=infectados

        )

        self.reglas.reiniciar()

        self.generacion = 0

        self.historial.clear()

        self.guardar_estadisticas()


    # =====================================================
    # MATRIZ SIGUIENTE
    # =====================================================

    def calcular_siguiente_generacion(self):

        matriz_actual = self.obtener_matriz()

        nueva = self.nueva_matriz()

        filas = self.poblacion.filas
        columnas = self.poblacion.columnas

        for fila in range(filas):

            for columna in range(columnas):

                nuevo_estado = self.reglas.aplicar_regla(

                    matriz_actual,

                    fila,

                    columna

                )

                nueva[fila][columna] = nuevo_estado

        return nueva
        # =====================================================
    # APLICAR NUEVA GENERACIÓN
    # =====================================================

    def avanzar(self):

        nueva = self.calcular_siguiente_generacion()

        self.poblacion.reemplazar(

            nueva

        )

        self.generacion += 1

        self.guardar_estadisticas()


    # =====================================================
    # AVANZAR VARIAS GENERACIONES
    # =====================================================

    def avanzar_varias(self, generaciones):

        for _ in range(generaciones):

            self.avanzar()


    # =====================================================
    # EXISTEN INFECTADOS
    # =====================================================

    def existen_infectados(self):

        return (

            self.poblacion.contar_estado(2) > 0

        )


    # =====================================================
    # SIMULACIÓN TERMINADA
    # =====================================================

    def simulacion_terminada(self):

        return not self.existen_infectados()


    # =====================================================
    # ESTADÍSTICAS ACTUALES
    # =====================================================

    def estadisticas(self):

        datos = self.poblacion.estadisticas()

        datos["generacion"] = self.generacion

        return datos


    # =====================================================
    # TOTAL DE PERSONAS
    # =====================================================

    def total_personas(self):

        return self.poblacion.total_personas()


    # =====================================================
    # MATRIZ ACTUAL
    # =====================================================

    def matriz(self):

        return self.obtener_matriz()


    # =====================================================
    # CAMBIAR PARÁMETROS
    # =====================================================

    def configurar(

        self,

        probabilidad_contagio=None,

        dias_recuperacion=None,

        probabilidad_muerte=None

    ):

        self.reglas.configurar(

            probabilidad_contagio,

            dias_recuperacion,

            probabilidad_muerte

        )


    # =====================================================
    # GENERACIÓN SIGUIENTE
    # =====================================================

    def siguiente(self):

        self.avanzar()

        return self.obtener_matriz()


    # =====================================================
    # EJECUTAR HASTA TERMINAR
    # =====================================================

    def ejecutar(

        self,

        max_generaciones=500

    ):

        while (

            not self.simulacion_terminada()

            and

            self.generacion < max_generaciones

        ):

            self.avanzar()


    # =====================================================
    # PERSONAS SANAS
    # =====================================================

    def sanos(self):

        return self.poblacion.contar_estado(1)


    # =====================================================
    # PERSONAS INFECTADAS
    # =====================================================

    def infectados(self):

        return self.poblacion.contar_estado(2)


    # =====================================================
    # PERSONAS RECUPERADAS
    # =====================================================

    def recuperados(self):

        return self.poblacion.contar_estado(3)


    # =====================================================
    # PERSONAS FALLECIDAS
    # =====================================================

    def fallecidos(self):

        return self.poblacion.contar_estado(4)


    # =====================================================
    # PERSONAS VACÍAS
    # =====================================================

    def vacios(self):

        return self.poblacion.contar_estado(0)


    # =====================================================
    # IMPRIMIR MATRIZ
    # =====================================================

    def mostrar(self):

        self.poblacion.mostrar()


    # =====================================================
    # IMPRIMIR ESTADÍSTICAS
    # =====================================================

    def mostrar_estadisticas(self):

        datos = self.estadisticas()

        print()

        print("Generación:", datos["generacion"])

        print("-----------------------------")

        print("Sanos:", datos["sanos"])

        print("Infectados:", datos["infectados"])

        print("Recuperados:", datos["recuperados"])

        print("Fallecidos:", datos["fallecidos"])

        print("Vacíos:", datos["vacios"])
            # =====================================================
    # OBTENER UNA CELDA
    # =====================================================

    def obtener_celda(self, fila, columna):

        return self.obtener_matriz()[fila][columna]


    # =====================================================
    # CAMBIAR UNA CELDA
    # =====================================================

    def cambiar_celda(self, fila, columna, estado):

        self.poblacion.cambiar_estado(

            fila,

            columna,

            estado

        )


    # =====================================================
    # REEMPLAZAR MATRIZ COMPLETA
    # =====================================================

    def reemplazar_matriz(self, matriz):

        self.poblacion.reemplazar(

            matriz

        )


    # =====================================================
    # LIMPIAR HISTORIAL
    # =====================================================

    def limpiar_historial(self):

        self.historial.clear()


    # =====================================================
    # ÚLTIMO REGISTRO
    # =====================================================

    def ultimo_registro(self):

        if len(self.historial) == 0:

            return None

        return self.historial[-1]


    # =====================================================
    # CANTIDAD DE GENERACIONES GUARDADAS
    # =====================================================

    def total_generaciones(self):

        return len(self.historial)


    # =====================================================
    # RESTAURAR SIMULACIÓN
    # =====================================================

    def restaurar(

        self,

        historial

    ):

        self.historial = historial.copy()


    # =====================================================
    # EXPORTAR DATOS
    # =====================================================

    def exportar(self):

        return {

            "generacion": self.generacion,

            "historial": self.historial,

            "estadisticas": self.estadisticas()

        }


    # =====================================================
    # INFORMACIÓN GENERAL
    # =====================================================

    def informacion(self):

        return {

            "filas": self.poblacion.filas,

            "columnas": self.poblacion.columnas,

            "personas": self.total_personas(),

            "generacion": self.generacion

        }


    # =====================================================
    # REINICIAR SOLO LA GENERACIÓN
    # =====================================================

    def reiniciar_generacion(self):

        self.generacion = 0


    # =====================================================
    # REINICIAR HISTORIAL Y CONTADORES
    # =====================================================

    def reinicio_total(self):

        self.reglas.reiniciar()

        self.generacion = 0

        self.historial.clear()

        self.guardar_estadisticas()


# ==========================================================
# PRUEBA DEL MOTOR
# ==========================================================

if __name__ == "__main__":

    motor = MotorCovid(

        filas=20,

        columnas=20,

        infectados_iniciales=8,

        probabilidad_contagio=0.40,

        dias_recuperacion=10,

        probabilidad_muerte=0.03

    )

    print()

    print("======================================")

    print(" SIMULACIÓN COVID ")

    print("======================================")

    print()

    motor.mostrar()

    print()

    for i in range(15):

        print()

        print("=" * 40)

        print(f"GENERACIÓN {motor.obtener_generacion()}")

        print("=" * 40)

        motor.mostrar_estadisticas()

        motor.avanzar()

    print()

    print("=" * 40)

    print("SIMULACIÓN FINALIZADA")

    print("=" * 40)

    print()

    print(

        "Generaciones simuladas:",

        motor.obtener_generacion()

    )

    print()

    print(

        "Información del sistema"

    )

    print(

        motor.informacion()

    )