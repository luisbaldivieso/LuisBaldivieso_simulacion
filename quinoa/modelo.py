"""
=========================================================
MODELO MATEMÁTICO - PLANTA PROCESADORA DE QUINUA
Modelo Lotka-Volterra adaptado al procesamiento industrial
=========================================================

Variables:

x = Stock de quinua (kg)
y = Nivel de procesamiento (kg/día)

Parámetros:

alpha = Tasa de llegada de quinua
beta = Tasa de consumo de quinua por procesamiento
delta = Incremento del procesamiento por disponibilidad de stock
gamma = Reducción del procesamiento por mantenimiento o fallas
"""


def modelo_quinua(variables, t, alpha, beta, delta, gamma):
    """
    Modelo dinámico de la planta procesadora de quinua.

    Parámetros
    ----------
    variables : list
        [stock_quinua, procesamiento]

    t : float
        Tiempo (requerido por odeint).

    alpha : float
        Llegada de quinua.

    beta : float
        Consumo de quinua.

    delta : float
        Incremento del procesamiento.

    gamma : float
        Reducción del procesamiento.

    Retorna
    -------
    list
        [dStock/dt, dProcesamiento/dt]
    """

    stock = variables[0]
    procesamiento = variables[1]

    # Variación del stock de quinua
    dstock_dt = alpha * stock - beta * stock * procesamiento

    # Variación del nivel de procesamiento
    dprocesamiento_dt = (
        delta * stock * procesamiento
        - gamma * procesamiento
    )

    return [dstock_dt, dprocesamiento_dt]