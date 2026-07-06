# ==========================================
# montecarlo.py
# Simulación Monte Carlo - Ruleta Europea
# ==========================================

from motor_ruleta import girar, color


class MonteCarlo:

    def __init__(self):
        self.resultados = {i: 0 for i in range(37)}
        self.total = 0

    # ==========================
    # SIMULACIÓN MASIVA
    # ==========================
    def simular(self, n=1000):

        self.total = n

        for _ in range(n):
            num = girar()
            self.resultados[num] += 1

        return self.resultados

    # ==========================
    # PROBABILIDAD TEÓRICA
    # ==========================
    def probabilidad_teorica(self):

        return {i: round(100 / 37, 2) for i in range(37)}

    # ==========================
    # PROBABILIDAD EMPÍRICA
    # ==========================
    def probabilidad_empirica(self):

        if self.total == 0:
            return {i: 0 for i in range(37)}

        return {
            i: round((self.resultados[i] / self.total) * 100, 2)
            for i in range(37)
        }

    # ==========================
    # LIMITES (tipo tabla Excel)
    # ==========================
    def limites(self):

        limites = {}
        acumulado = 0

        for i in range(37):

            prob = 100 / 37
            lim_inf = acumulado
            lim_sup = acumulado + prob

            limites[i] = {
                "limite_inferior": round(lim_inf, 2),
                "limite_superior": round(lim_sup, 2),
                "probabilidad": round(prob, 2)
            }

            acumulado += prob

        return limites

    # ==========================
    # TABLA FINAL (FORMATO EXCEL)
    # ==========================
    def tabla(self):

        emp = self.probabilidad_empirica()
        teo = self.probabilidad_teorica()
        lim = self.limites()

        tabla = []

        for i in range(37):

            tabla.append({
                "resultado": i,
                "prob_teorica": teo[i],
                "prob_empirica": emp[i],
                "limite_inferior": lim[i]["limite_inferior"],
                "limite_superior": lim[i]["limite_superior"]
            })

        return tabla

    # ==========================
    # RESUMEN
    # ==========================
    def resumen(self):

        emp = self.probabilidad_empirica()

        return {
            "total_simulaciones": self.total,
            "promedio_rojo": sum(emp.values()) / 37
        }


# ==========================
# PRUEBA
# ==========================
if __name__ == "__main__":

    mc = MonteCarlo()

    mc.simular(1000)

    tabla = mc.tabla()

    for fila in tabla[:10]:
        print(fila)