import matplotlib.pyplot as plt


# ===========================================
# GRAFICO DEL CAPITAL
# ===========================================

def grafico_capital(historial):

    plt.figure(figsize=(8, 5))

    plt.plot(
        range(len(historial)),
        historial,
        marker="o"
    )

    plt.title("Evolución del Capital")

    plt.xlabel("Giros")

    plt.ylabel("Capital")

    plt.grid(True)

    plt.tight_layout()

    plt.show()


# ===========================================
# GRAFICO DE GANADAS Y PERDIDAS
# ===========================================

def grafico_resultados(ganadas, perdidas):

    plt.figure(figsize=(6, 6))

    etiquetas = ["Ganadas", "Perdidas"]

    valores = [ganadas, perdidas]

    colores = ["green", "red"]

    plt.pie(
        valores,
        labels=etiquetas,
        colors=colores,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Ganadas vs Perdidas")

    plt.axis("equal")

    plt.show()


# ===========================================
# GRAFICO DE COLORES
# ===========================================

def grafico_colores(rojos, negros, verdes):

    plt.figure(figsize=(6, 5))

    nombres = ["Rojo", "Negro", "Verde"]

    cantidades = [rojos, negros, verdes]

    colores = ["red", "black", "green"]

    plt.bar(
        nombres,
        cantidades,
        color=colores
    )

    plt.title("Frecuencia por Color")

    plt.ylabel("Cantidad")

    plt.tight_layout()

    plt.show()


# ===========================================
# GRAFICO DE NUMEROS
# ===========================================

def grafico_numeros(numeros):

    plt.figure(figsize=(12, 5))

    plt.hist(
        numeros,
        bins=37,
        edgecolor="black"
    )

    plt.title("Frecuencia de Números")

    plt.xlabel("Número")

    plt.ylabel("Frecuencia")

    plt.xticks(range(37))

    plt.tight_layout()

    plt.show()


# ===========================================
# GRAFICO COMPLETO
# ===========================================

def mostrar_todos(

    historial,

    ganadas,

    perdidas,

    rojos,

    negros,

    verdes,

    numeros

):

    grafico_capital(historial)

    grafico_resultados(

        ganadas,

        perdidas

    )

    grafico_colores(

        rojos,

        negros,

        verdes

    )

    grafico_numeros(

        numeros

    )


# ===========================================
# PRUEBA
# ===========================================

if __name__ == "__main__":

    historial = [

        1000,

        1010,

        990,

        1030,

        1040,

        1020,

        1050

    ]

    numeros = [

        5,18,7,12,0,

        35,20,14,1,

        33,25,8,10

    ]

    grafico_capital(historial)

    grafico_resultados(8,5)

    grafico_colores(6,6,1)

    grafico_numeros(numeros)