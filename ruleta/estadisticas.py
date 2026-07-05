# ==========================================
# estadisticas.py
# Control de estadísticas y capital
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

        self.jugadas += 1

        numero = resultado["numero"]
        gano = resultado["gano"]
        ganancia = resultado["ganancia"]

        self.capital += ganancia

        self.historial.append(numero)

        # Guardar solo los últimos 20 números
        if len(self.historial) > 20:
            self.historial.pop(0)

        if gano:

            self.ganadas += 1

            self.racha_ganadora += 1
            self.racha_perdedora = 0

            if self.racha_ganadora > self.max_racha_ganadora:
                self.max_racha_ganadora = self.racha_ganadora

        else:

            self.perdidas += 1

            self.racha_perdedora += 1
            self.racha_ganadora = 0

            if self.racha_perdedora > self.max_racha_perdedora:
                self.max_racha_perdedora = self.racha_perdedora

    def porcentaje_aciertos(self):

        if self.jugadas == 0:
            return 0

        return round((self.ganadas / self.jugadas) * 100, 2)

    def ultimo_numero(self):

        if not self.historial:
            return "-"

        return self.historial[-1]

    def obtener_historial(self):

        return self.historial

    def reiniciar(self):

        self.capital = self.capital_inicial

        self.jugadas = 0
        self.ganadas = 0
        self.perdidas = 0

        self.historial.clear()

        self.racha_ganadora = 0
        self.racha_perdedora = 0

        self.max_racha_ganadora = 0
        self.max_racha_perdedora = 0

    def resumen(self):

        return {

            "capital": self.capital,

            "jugadas": self.jugadas,

            "ganadas": self.ganadas,

            "perdidas": self.perdidas,

            "porcentaje": self.porcentaje_aciertos(),

            "racha_ganadora": self.max_racha_ganadora,

            "racha_perdedora": self.max_racha_perdedora,

            "ultimo": self.ultimo_numero(),

            "historial": self.historial

        }


# ==========================================
# PRUEBA
# ==========================================

if __name__ == "__main__":

    stats = Estadisticas(1000)

    stats.registrar({
        "numero": 18,
        "gano": True,
        "ganancia": 100
    })

    stats.registrar({
        "numero": 7,
        "gano": False,
        "ganancia": -100
    })

    stats.registrar({
        "numero": 32,
        "gano": True,
        "ganancia": 100
    })

    print(stats.resumen())