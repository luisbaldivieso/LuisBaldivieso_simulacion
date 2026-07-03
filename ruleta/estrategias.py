# ===========================================
# ESTRATEGIAS DE APUESTA
# ===========================================

class EstrategiaBase:

    def __init__(self, apuesta_inicial):

        self.apuesta_inicial = apuesta_inicial
        self.apuesta_actual = apuesta_inicial

    def ganar(self):
        pass

    def perder(self):
        pass

    def obtener_apuesta(self):
        return self.apuesta_actual

    def reiniciar(self):
        self.apuesta_actual = self.apuesta_inicial


# ===========================================
# APUESTA FIJA
# ===========================================

class ApuestaFija(EstrategiaBase):

    def ganar(self):
        self.apuesta_actual = self.apuesta_inicial

    def perder(self):
        self.apuesta_actual = self.apuesta_inicial


# ===========================================
# MARTINGALA
# Duplica la apuesta cuando pierde.
# Reinicia al ganar.
# ===========================================

class Martingala(EstrategiaBase):

    def ganar(self):
        self.apuesta_actual = self.apuesta_inicial

    def perder(self):
        self.apuesta_actual *= 2


# ===========================================
# D'ALEMBERT
# +1 unidad al perder
# -1 unidad al ganar
# ===========================================

class DAlembert(EstrategiaBase):

    def ganar(self):

        if self.apuesta_actual > self.apuesta_inicial:

            self.apuesta_actual -= self.apuesta_inicial

    def perder(self):

        self.apuesta_actual += self.apuesta_inicial


# ===========================================
# PAROLI
# Duplica al ganar.
# Reinicia al perder.
# Máximo 3 victorias consecutivas.
# ===========================================

class Paroli(EstrategiaBase):

    def __init__(self, apuesta_inicial):

        super().__init__(apuesta_inicial)

        self.racha = 0

    def ganar(self):

        self.racha += 1

        if self.racha >= 3:

            self.apuesta_actual = self.apuesta_inicial
            self.racha = 0

        else:

            self.apuesta_actual *= 2

    def perder(self):

        self.apuesta_actual = self.apuesta_inicial

        self.racha = 0


# ===========================================
# FABRICA DE ESTRATEGIAS
# ===========================================

def crear_estrategia(nombre, apuesta_inicial):

    nombre = nombre.lower()

    if nombre == "martingala":
        return Martingala(apuesta_inicial)

    elif nombre == "d'alembert":
        return DAlembert(apuesta_inicial)

    elif nombre == "paroli":
        return Paroli(apuesta_inicial)

    else:
        return ApuestaFija(apuesta_inicial)


# ===========================================
# PRUEBA
# ===========================================

if __name__ == "__main__":

    estrategia = crear_estrategia("Martingala", 10)

    print("Apuesta inicial:", estrategia.obtener_apuesta())

    estrategia.perder()
    print("Pierde ->", estrategia.obtener_apuesta())

    estrategia.perder()
    print("Pierde ->", estrategia.obtener_apuesta())

    estrategia.ganar()
    print("Gana ->", estrategia.obtener_apuesta())