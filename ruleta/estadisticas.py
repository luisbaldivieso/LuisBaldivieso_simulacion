# ===========================================
# ESTADISTICAS DE LA RULETA
# ===========================================

class Estadisticas:

    def __init__(self):

        self.reiniciar()

    # =======================================

    def reiniciar(self):

        self.giros = 0

        self.ganadas = 0

        self.perdidas = 0

        self.capital_inicial = 0

        self.capital_final = 0

        self.capital_maximo = 0

        self.capital_minimo = 0

        self.ganancia_maxima = 0

        self.perdida_maxima = 0

        self.historial = []

    # =======================================

    def iniciar(self, capital):

        self.capital_inicial = capital

        self.capital_final = capital

        self.capital_maximo = capital

        self.capital_minimo = capital

        self.historial = [capital]

    # =======================================

    def registrar(self, capital, gano, apuesta):

        self.giros += 1

        self.capital_final = capital

        self.historial.append(capital)

        if gano:

            self.ganadas += 1

            if apuesta > self.ganancia_maxima:

                self.ganancia_maxima = apuesta

        else:

            self.perdidas += 1

            if apuesta > self.perdida_maxima:

                self.perdida_maxima = apuesta

        if capital > self.capital_maximo:

            self.capital_maximo = capital

        if capital < self.capital_minimo:

            self.capital_minimo = capital

    # =======================================

    def porcentaje_aciertos(self):

        if self.giros == 0:

            return 0

        return (self.ganadas / self.giros) * 100

    # =======================================

    def porcentaje_fallos(self):

        if self.giros == 0:

            return 0

        return (self.perdidas / self.giros) * 100

    # =======================================

    def ganancia_total(self):

        return self.capital_final - self.capital_inicial

    # =======================================

    def promedio_por_giro(self):

        if self.giros == 0:

            return 0

        return self.ganancia_total() / self.giros

    # =======================================

    def resumen(self):

        return {

            "giros": self.giros,

            "ganadas": self.ganadas,

            "perdidas": self.perdidas,

            "capital_inicial": self.capital_inicial,

            "capital_final": self.capital_final,

            "capital_maximo": self.capital_maximo,

            "capital_minimo": self.capital_minimo,

            "ganancia_total": self.ganancia_total(),

            "ganancia_maxima": self.ganancia_maxima,

            "perdida_maxima": self.perdida_maxima,

            "porcentaje_aciertos": self.porcentaje_aciertos(),

            "porcentaje_fallos": self.porcentaje_fallos(),

            "promedio_por_giro": self.promedio_por_giro()

        }


# ===========================================
# PRUEBA
# ===========================================

if __name__ == "__main__":

    est = Estadisticas()

    est.iniciar(1000)

    est.registrar(1010, True, 10)

    est.registrar(990, False, 20)

    est.registrar(1010, True, 20)

    est.registrar(1030, True, 20)

    datos = est.resumen()

    print("\n========== ESTADÍSTICAS ==========\n")

    for clave, valor in datos.items():

        print(f"{clave}: {valor}")

    print("\n==================================")