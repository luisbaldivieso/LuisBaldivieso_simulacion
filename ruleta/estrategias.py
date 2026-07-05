# ==========================================
# estrategias.py
# Estrategias de Apuesta
# ==========================================


class Martingala:
    """
    Duplica la apuesta cuando pierde.
    Reinicia al ganar.
    """

    def __init__(self, apuesta_inicial):
        self.apuesta_inicial = apuesta_inicial
        self.apuesta_actual = apuesta_inicial

    def actualizar(self, gano):

        if gano:
            self.apuesta_actual = self.apuesta_inicial
        else:
            self.apuesta_actual *= 2

        return self.apuesta_actual

    def reiniciar(self):
        self.apuesta_actual = self.apuesta_inicial


class Fibonacci:
    """
    Estrategia Fibonacci.
    """

    def __init__(self, apuesta_inicial):

        self.apuesta_inicial = apuesta_inicial
        self.secuencia = [1, 1]
        self.posicion = 0

    def apuesta(self):

        while self.posicion >= len(self.secuencia):
            self.secuencia.append(
                self.secuencia[-1] + self.secuencia[-2]
            )

        return self.secuencia[self.posicion] * self.apuesta_inicial

    def actualizar(self, gano):

        if gano:
            self.posicion = max(0, self.posicion - 2)
        else:
            self.posicion += 1

        return self.apuesta()

    def reiniciar(self):
        self.posicion = 0


class DAlembert:
    """
    Estrategia D'Alembert.
    """

    def __init__(self, apuesta_inicial):

        self.apuesta_inicial = apuesta_inicial
        self.apuesta_actual = apuesta_inicial

    def actualizar(self, gano):

        if gano:
            self.apuesta_actual = max(
                self.apuesta_inicial,
                self.apuesta_actual - self.apuesta_inicial
            )
        else:
            self.apuesta_actual += self.apuesta_inicial

        return self.apuesta_actual

    def reiniciar(self):
        self.apuesta_actual = self.apuesta_inicial


class EstrategiaFija:
    """
    Siempre apuesta el mismo monto.
    """

    def __init__(self, apuesta):

        self.apuesta = apuesta

    def actualizar(self, gano):
        return self.apuesta

    def reiniciar(self):
        pass


# ==========================================
# FÁBRICA DE ESTRATEGIAS
# ==========================================

def crear_estrategia(nombre, apuesta_inicial):

    nombre = nombre.lower()

    if nombre == "martingala":
        return Martingala(apuesta_inicial)

    elif nombre == "fibonacci":
        return Fibonacci(apuesta_inicial)

    elif nombre == "dalembert":
        return DAlembert(apuesta_inicial)

    else:
        return EstrategiaFija(apuesta_inicial)


# ==========================================
# PRUEBAS
# ==========================================

if __name__ == "__main__":

    estrategia = crear_estrategia("Martingala", 10)

    print("Apuesta inicial:", estrategia.apuesta_actual)

    for resultado in [False, False, True, False, True]:

        apuesta = estrategia.actualizar(resultado)

        print(
            "Ganó:", resultado,
            "-> Nueva apuesta:", apuesta
        )