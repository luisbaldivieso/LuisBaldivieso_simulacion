"""
=========================================================
SIMULACIÓN DE LA PLANTA PROCESADORA DE QUINUA
=========================================================

Este módulo resuelve el sistema de ecuaciones
utilizando odeint.
"""

import numpy as np
from scipy.integrate import odeint

from modelo import modelo_quinua


def resolver_modelo(
    alpha,
    beta,
    delta,
    gamma,
    stock_inicial,
    procesamiento_inicial,
    tiempo_final,
    puntos=1000
):
    """
    Ejecuta la simulación del modelo.

    Parámetros
    ----------
    alpha : float
        Tasa de llegada de quinua.

    beta : float
        Tasa de consumo.

    delta : float
        Incremento del procesamiento.

    gamma : float
        Reducción del procesamiento.

    stock_inicial : float
        Stock inicial de quinua.

    procesamiento_inicial : float
        Procesamiento inicial.

    tiempo_final : float
        Tiempo total de simulación.

    puntos : int
        Cantidad de puntos de cálculo.

    Retorna
    -------
    tiempo
    stock
    procesamiento
    """

    # Vector de tiempo
    tiempo = np.linspace(0, tiempo_final, puntos)

    # Condiciones iniciales
    condiciones = [
        stock_inicial,
        procesamiento_inicial
    ]

    # Resolver ecuaciones
    solucion = odeint(
        modelo_quinua,
        condiciones,
        tiempo,
        args=(alpha, beta, delta, gamma)
    )

    stock = solucion[:, 0]
    procesamiento = solucion[:, 1]

    return tiempo, stock, procesamiento


# =========================================================
# Prueba rápida (solo si se ejecuta este archivo)
# =========================================================
if __name__ == "__main__":

    tiempo, stock, procesamiento = resolver_modelo(
        alpha=0.25,
        beta=0.08,
        delta=0.04,
        gamma=0.30,
        stock_inicial=10000,
        procesamiento_inicial=2000,
        tiempo_final=60
    )

    print("Simulación ejecutada correctamente.")
    print(f"Tiempo: {len(tiempo)} puntos")
    print(f"Stock inicial: {stock[0]:.2f}")
    print(f"Stock final: {stock[-1]:.2f}")
    print(f"Procesamiento inicial: {procesamiento[0]:.2f}")
    print(f"Procesamiento final: {procesamiento[-1]:.2f}")