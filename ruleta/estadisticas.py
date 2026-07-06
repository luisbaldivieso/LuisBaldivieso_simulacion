# ==========================================
# estadisticas.py
# Control de estadísticas - Monte Carlo
# ==========================================

class Estadisticas:

    def __init__(self, capital_inicial):

        self.capital_inicial = capital_inicial
        self.capital = capital_inicial

        self.jugadas = 0
        self.ganadas = 0
        self.perdidas = 0

        self.historial = []

        self.racha_ganadora = 0
        self.racha_perdedora = 0

        self.max_racha_ganadora = 0
        self.max_racha_perdedora = 0

    def registrar(self, resultado):
        """
        Registra una jugada individual.
        """

        self.jugadas += 1

        gano = resultado["gano"]
        ganancia = resultado["ganancia"]
        numero = resultado["numero"]

        # actualizar capital
        self.capital += ganancia

        # historial
        self.historial.append(numero)

        if len(self.historial) > 30:
            self.historial.pop(0)

        # ganadas / perdidas
        if gano:
            self.ganadas += 1

            self.racha_ganadora += 1
            self.racha_perdedora = 0

            self.max_racha_ganadora = max(
                self.max_racha_ganadora,
                self.racha_ganadora
            )

        else:
            self.perdidas += 1

            self.racha_perdedora += 1
            self.racha_ganadora = 0

            self.max_racha_perdedora = max(
                self.max_racha_perdedora,
                self.racha_perdedora
            )

    def porcentaje_aciertos(self):
        if self.jugadas == 0:
            return 0
        return round((self.ganadas / self.jugadas) * 100, 2)

    def resumen(self):
        """
        Resumen general del sistema.
        """

        return {
            "capital_inicial": self.capital_inicial,
            "capital_actual": self.capital,
            "jugadas": self.jugadas,
            "ganadas": self.ganadas,
            "perdidas": self.perdidas,
            "porcentaje": self.porcentaje_aciertos(),
            "racha_max_ganadora": self.max_racha_ganadora,
            "racha_max_perdedora": self.max_racha_perdedora,
            "ultimo_numero": self.historial[-1] if self.historial else None,
            "historial": self.historial
        }

    def reset(self):
        """
        Reinicia estadísticas.
        """

        self.__init__(self.capital_inicial)


# ==========================================
# PRUEBA RÁPIDA
# ==========================================
if __name__ == "__main__":

    s = Estadisticas(1000)

    s.registrar({
        "numero": 10,
        "gano": True,
        "ganancia": 50
    })

    s.registrar({
        "numero": 22,
        "gano": False,
        "ganancia": -10
    })

    print(s.resumen())