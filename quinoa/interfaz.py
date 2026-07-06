"""
=========================================================
INTERFAZ GRÁFICA
Simulación de una Planta Procesadora de Quinua
=========================================================
"""

import matplotlib.pyplot as plt

from simulacion import resolver_modelo


def iniciar():

    # ==========================
    # Parámetros iniciales
    # ==========================

    alpha = 0.25
    beta = 0.08
    delta = 0.04
    gamma = 0.30

    stock_inicial = 10000
    procesamiento_inicial = 2000

    tiempo_final = 60

    # ==========================
    # Ejecutar simulación
    # ==========================

    tiempo, stock, procesamiento = resolver_modelo(
        alpha,
        beta,
        delta,
        gamma,
        stock_inicial,
        procesamiento_inicial,
        tiempo_final
    )

    # ==========================
    # Crear ventana
    # ==========================

    fig, axs = plt.subplots(1, 2, figsize=(15, 7))

    fig.suptitle(
        "Simulación de una Planta Procesadora de Quinua",
        fontsize=16,
        fontweight="bold"
    )

    # =====================================================
    # GRÁFICO 1
    # =====================================================

    axs[0].plot(
        tiempo,
        stock,
        color="green",
        linewidth=2,
        label="Stock de Quinua"
    )

    axs[0].plot(
        tiempo,
        procesamiento,
        color="orange",
        linewidth=2,
        label="Procesamiento"
    )

    axs[0].set_title("Evolución en el Tiempo")

    axs[0].set_xlabel("Tiempo")

    axs[0].set_ylabel("Cantidad")

    axs[0].grid(True)

    axs[0].legend()

    # =====================================================
    # GRÁFICO 2
    # =====================================================

    axs[1].plot(
        stock,
        procesamiento,
        color="blue",
        linewidth=2
    )

    axs[1].scatter(
        stock[0],
        procesamiento[0],
        color="red",
        s=80,
        label="Inicio"
    )

    axs[1].scatter(
        stock[-1],
        procesamiento[-1],
        color="black",
        s=80,
        label="Final"
    )

    axs[1].set_title("Espacio de Fase")

    axs[1].set_xlabel("Stock de Quinua")

    axs[1].set_ylabel("Procesamiento")

    axs[1].grid(True)

    axs[1].legend()

    # =====================================================
    # Texto informativo
    # =====================================================

    plt.figtext(
        0.5,
        0.02,
        (
            f"Stock Inicial: {stock_inicial:.0f} kg     "
            f"Procesamiento Inicial: {procesamiento_inicial:.0f} kg/día"
        ),
        ha="center",
        fontsize=11
    )

    plt.tight_layout()

    plt.show()