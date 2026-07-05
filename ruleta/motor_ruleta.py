# ==========================================
# motor_ruleta.py
# Motor de la Ruleta Europea
# ==========================================

import random

# Números rojos de la ruleta europea
ROJOS = {
    1, 3, 5, 7, 9,
    12, 14, 16, 18,
    19, 21, 23, 25,
    27, 30, 32, 34, 36
}


def girar_ruleta():
    """
    Genera un número aleatorio entre 0 y 36.
    """
    return random.randint(0, 36)


def obtener_color(numero):
    """
    Devuelve el color del número.
    """
    if numero == 0:
        return "Verde"

    if numero in ROJOS:
        return "Rojo"

    return "Negro"


def es_par(numero):
    """
    Devuelve True si el número es par.
    """
    if numero == 0:
        return False

    return numero % 2 == 0


def es_impar(numero):
    """
    Devuelve True si el número es impar.
    """
    if numero == 0:
        return False

    return numero % 2 != 0


def primera_mitad(numero):
    """
    1 - 18
    """
    return 1 <= numero <= 18


def segunda_mitad(numero):
    """
    19 - 36
    """
    return 19 <= numero <= 36


def obtener_docena(numero):
    """
    Devuelve la docena.
    """
    if 1 <= numero <= 12:
        return 1

    if 13 <= numero <= 24:
        return 2

    if 25 <= numero <= 36:
        return 3

    return 0


def obtener_columna(numero):
    """
    Devuelve la columna.
    """
    if numero == 0:
        return 0

    if numero % 3 == 1:
        return 1

    if numero % 3 == 2:
        return 2

    return 3


def normalizar_valor(tipo, valor):
    """Convierte los valores del formulario a un formato útil para la evaluación."""

    if tipo == "mitad":
        if isinstance(valor, str):
            valor = valor.strip().lower()
            if valor in {"1", "1-18", "primera", "primera mitad"}:
                return 1
            return 2
        return valor

    if isinstance(valor, str):
        valor = valor.strip()

    if tipo in {"numero", "docena", "columna"}:
        try:
            return int(valor)
        except (TypeError, ValueError):
            return valor

    return valor


def evaluar_apuesta(tipo, valor, numero):
    """
    Evalúa si una apuesta gana o pierde.

    tipo:
        numero
        color
        paridad
        mitad
        docena
        columna
    """

    valor = normalizar_valor(tipo, valor)

    if tipo == "numero":
        return numero == valor

    if tipo == "color":
        return obtener_color(numero).lower() == str(valor).lower()

    if tipo == "paridad":
        if str(valor).lower() == "par":
            return es_par(numero)

        return es_impar(numero)

    if tipo == "mitad":
        if valor == 1:
            return primera_mitad(numero)

        return segunda_mitad(numero)

    if tipo == "docena":
        return obtener_docena(numero) == valor

    if tipo == "columna":
        return obtener_columna(numero) == valor

    return False


def pago_apuesta(tipo):
    """
    Multiplicador de ganancia.
    """

    pagos = {
        "numero": 35,
        "color": 1,
        "paridad": 1,
        "mitad": 1,
        "docena": 2,
        "columna": 2
    }

    return pagos.get(tipo, 1)


def jugar(tipo, valor, monto):
    """
    Ejecuta una jugada completa.

    Retorna un diccionario con toda la información.
    """

    numero = girar_ruleta()

    gano = evaluar_apuesta(tipo, valor, numero)

    if gano:
        ganancia = monto * pago_apuesta(tipo)
    else:
        ganancia = -monto

    return {
        "numero": numero,
        "color": obtener_color(numero),
        "gano": gano,
        "ganancia": ganancia,
        "monto": monto,
        "tipo": tipo,
        "valor": valor
    }