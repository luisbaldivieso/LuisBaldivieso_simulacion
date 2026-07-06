# ==========================================
# motor_ruleta.py
# Ruleta Europea - Motor Monte Carlo
# ==========================================

import random

# Ruleta europea (0-36)
NUMEROS = list(range(37))

ROJOS = {
    0,1, 3, 5, 7, 9,
    12, 14, 16, 18,
    19, 21, 23, 25,
    27, 30, 32, 34, 36
}


def girar():
    """Simula un giro de ruleta."""
    return random.choice(NUMEROS)


def color(numero):
    """Devuelve color del número."""
    if numero == 0:
        return "verde"
    return "rojo" if numero in ROJOS else "negro"


def paridad(numero):
    if numero == 0:
        return "ninguno"
    return "par" if numero % 2 == 0 else "impar"


def mitad(numero):
    if 1 <= numero <= 18:
        return "1-18"
    if 19 <= numero <= 36:
        return "19-36"
    return "0"


def docena(numero):
    if 1 <= numero <= 12:
        return 1
    if 13 <= numero <= 24:
        return 2
    if 25 <= numero <= 36:
        return 3
    return 0


def columna(numero):
    if numero == 0:
        return 0
    return (numero - 1) % 3 + 1


def jugar(numero_apuesta, tipo, valor, monto):
    """
    Ejecuta una jugada de ruleta.
    Retorna resultado tipo Monte Carlo.
    """

    resultado = girar()

    gano = False

    if tipo == "numero":
        gano = (resultado == int(valor))

    elif tipo == "color":
        gano = (color(resultado) == valor.lower())

    elif tipo == "paridad":
        gano = (paridad(resultado) == valor.lower())

    elif tipo == "mitad":
        gano = (mitad(resultado) == valor)

    elif tipo == "docena":
        gano = (docena(resultado) == int(valor))

    elif tipo == "columna":
        gano = (columna(resultado) == int(valor))

    ganancia = monto * 35 if gano and tipo == "numero" else (monto * 2 if gano else -monto)

    return {
        "numero": resultado,
        "color": color(resultado),
        "gano": gano,
        "ganancia": ganancia,
        "monto": monto,
        "tipo": tipo,
        "valor": valor
    }


def simulacion(n=1000, tipo="color", valor="rojo", monto=10):
    """
    Monte Carlo: múltiples simulaciones.
    """

    resultados = {
        "ganadas": 0,
        "perdidas": 0,
        "capital": 0
    }

    for _ in range(n):
        r = jugar(0, tipo, valor, monto)

        if r["gano"]:
            resultados["ganadas"] += 1
        else:
            resultados["perdidas"] += 1

        resultados["capital"] += r["ganancia"]

    return resultados