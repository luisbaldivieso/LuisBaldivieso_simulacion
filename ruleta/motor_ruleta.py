import random

# ===========================================
# NUMEROS ROJOS Y NEGROS (RULETA EUROPEA)
# ===========================================

ROJOS = {
    1, 3, 5, 7, 9,
    12, 14, 16, 18,
    19, 21, 23, 25,
    27, 30, 32, 34, 36
}

NEGROS = {
    2, 4, 6, 8, 10,
    11, 13, 15, 17,
    20, 22, 24, 26,
    28, 29, 31, 33, 35
}


# ===========================================
# OBTENER COLOR
# ===========================================

def obtener_color(numero):

    if numero == 0:
        return "Verde"

    if numero in ROJOS:
        return "Rojo"

    return "Negro"


# ===========================================
# GIRAR RULETA
# ===========================================

def girar_ruleta():

    numero = random.randint(0, 36)

    color = obtener_color(numero)

    return numero, color


# ===========================================
# EVALUAR APUESTA
# ===========================================

def evaluar_apuesta(tipo_apuesta, valor_apuesta, numero, color):

    tipo_apuesta = tipo_apuesta.lower()

    if tipo_apuesta == "rojo":

        if color == "Rojo":
            return True, 1

        return False, -1

    elif tipo_apuesta == "negro":

        if color == "Negro":
            return True, 1

        return False, -1

    elif tipo_apuesta == "verde":

        if color == "Verde":
            return True, 35

        return False, -1

    elif tipo_apuesta == "numero":

        if int(valor_apuesta) == numero:
            return True, 35

        return False, -1

    return False, -1


# ===========================================
# SIMULAR UN GIRO
# ===========================================

def simular_giro(capital, apuesta, tipo_apuesta, valor_apuesta=None):

    numero, color = girar_ruleta()

    gano, multiplicador = evaluar_apuesta(

        tipo_apuesta,

        valor_apuesta if valor_apuesta is not None else -1,

        numero,

        color

    )

    if gano:

        capital += apuesta * multiplicador

        resultado = "GANÓ"

    else:

        capital -= apuesta

        resultado = "PERDIÓ"

    return {

        "numero": numero,

        "color": color,

        "resultado": resultado,

        "capital": capital,

        "gano": gano

    }


# ===========================================
# PRUEBA DEL ARCHIVO
# ===========================================

if __name__ == "__main__":

    capital = 1000

    apuesta = 10

    for giro in range(10):

        datos = simular_giro(

            capital,

            apuesta,

            "Rojo"

        )

        capital = datos["capital"]

        print(

            f"Giro {giro+1:02d} | "

            f"Número: {datos['numero']:2d} | "

            f"{datos['color']:6s} | "

            f"{datos['resultado']:7s} | "

            f"Capital: {capital}"

        )