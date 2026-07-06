"""
simulador.py
---------------------------------------
Modelo Lotka-Volterra aplicado a una
planta procesadora de quinua.

Autor: Tu Nombre
"""

import numpy as np


def modelo(x, y, alpha, beta, delta, gamma):
    """
    Calcula las derivadas del sistema.

    Parámetros:
        x : Stock de quinua
        y : Nivel de procesamiento
        alpha : Tasa de crecimiento
        beta : Tasa de consumo
        delta : Tasa de conversión
        gamma : Tasa de reducción

    Retorna:
        dx, dy
    """

    dx = alpha * x - beta * x * y
    dy = delta * x * y - gamma * y

    return dx, dy


def rk4(x0, y0, alpha, beta, delta, gamma, tiempo_total, dt):
    """
    Resuelve el sistema mediante Runge-Kutta de cuarto orden.

    Retorna:
        tiempo
        stock
        procesamiento
    """

    pasos = int(tiempo_total / dt) + 1

    tiempo = np.zeros(pasos)
    stock = np.zeros(pasos)
    procesamiento = np.zeros(pasos)

    tiempo[0] = 0
    stock[0] = x0
    procesamiento[0] = y0

    for i in range(pasos - 1):

        tiempo[i + 1] = tiempo[i] + dt

        x = stock[i]
        y = procesamiento[i]

        k1x, k1y = modelo(x, y, alpha, beta, delta, gamma)

        k2x, k2y = modelo(
            x + 0.5 * dt * k1x,
            y + 0.5 * dt * k1y,
            alpha, beta, delta, gamma
        )

        k3x, k3y = modelo(
            x + 0.5 * dt * k2x,
            y + 0.5 * dt * k2y,
            alpha, beta, delta, gamma
        )

        k4x, k4y = modelo(
            x + dt * k3x,
            y + dt * k3y,
            alpha, beta, delta, gamma
        )

        stock[i + 1] = x + (dt / 6) * (
            k1x + 2 * k2x + 2 * k3x + k4x
        )

        procesamiento[i + 1] = y + (dt / 6) * (
            k1y + 2 * k2y + 2 * k3y + k4y
        )

        # Evitar valores negativos

        if stock[i + 1] < 0:
            stock[i + 1] = 0

        if procesamiento[i + 1] < 0:
            procesamiento[i + 1] = 0

    return tiempo, stock, procesamiento


# Prueba rápida del módulo
if __name__ == "__main__":

    t, x, y = rk4(
        x0=10000,
        y0=2000,
        alpha=0.05,
        beta=0.00001,
        delta=0.00002,
        gamma=0.03,
        tiempo_total=120,
        dt=0.5
    )

    print("Simulación completada correctamente.")
    print(f"Datos generados: {len(t)}")
    print(f"Stock final: {x[-1]:.2f} kg")
    print(f"Procesamiento final: {y[-1]:.2f} kg/día")