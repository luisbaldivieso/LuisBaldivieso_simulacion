import tkinter as tk
from tkinter import ttk, messagebox
import random

from motor_covid import MotorCovid
from estadisticas import EstadisticasCovid
from graficos import GraficosCovid


class CovidApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación COVID")
        self.root.geometry("1100x700")
        self.root.minsize(1000, 650)

        self.motor = MotorCovid(
            filas=20,
            columnas=20,
            infectados_iniciales=10,
            probabilidad_contagio=0.4,
            dias_recuperacion=8,
            probabilidad_muerte=0.03,
        )
        self.estadisticas = EstadisticasCovid()
        self.graficos = GraficosCovid()

        self.crear_interfaz()
        self.actualizar_estado()

    def crear_interfaz(self):
        self.panel_izquierdo = tk.Frame(self.root, width=280, bg="#F3F4F6")
        self.panel_izquierdo.pack(side="left", fill="y")

        self.panel_derecho = tk.Frame(self.root, bg="#FFFFFF")
        self.panel_derecho.pack(side="right", fill="both", expand=True)

        self.crear_panel_control()
        self.crear_panel_simulacion()

    def crear_panel_control(self):
        tk.Label(self.panel_izquierdo, text="SIMULACIÓN COVID", font=("Arial", 16, "bold"), bg="#F3F4F6").pack(pady=10)

        tk.Label(self.panel_izquierdo, text="Población (filas/columnas)", bg="#F3F4F6").pack(anchor="w", padx=10)
        self.var_filas = tk.IntVar(value=20)
        self.var_columnas = tk.IntVar(value=20)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_filas).pack(fill="x", padx=10)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_columnas).pack(fill="x", padx=10)

        tk.Label(self.panel_izquierdo, text="Infectados iniciales", bg="#F3F4F6").pack(anchor="w", padx=10, pady=(10, 0))
        self.var_infectados = tk.IntVar(value=10)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_infectados).pack(fill="x", padx=10)

        tk.Label(self.panel_izquierdo, text="Probabilidad contagio", bg="#F3F4F6").pack(anchor="w", padx=10, pady=(10, 0))
        self.var_prob = tk.DoubleVar(value=0.4)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_prob).pack(fill="x", padx=10)

        tk.Label(self.panel_izquierdo, text="Días recuperación", bg="#F3F4F6").pack(anchor="w", padx=10, pady=(10, 0))
        self.var_dias = tk.IntVar(value=8)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_dias).pack(fill="x", padx=10)

        tk.Label(self.panel_izquierdo, text="Probabilidad muerte", bg="#F3F4F6").pack(anchor="w", padx=10, pady=(10, 0))
        self.var_muerte = tk.DoubleVar(value=0.03)
        tk.Entry(self.panel_izquierdo, textvariable=self.var_muerte).pack(fill="x", padx=10)

        tk.Button(self.panel_izquierdo, text="▶ Simular", command=self.simular, bg="#2563EB", fg="white", font=("Arial", 11, "bold")).pack(fill="x", padx=10, pady=15)
        tk.Button(self.panel_izquierdo, text="🔄 Reiniciar", command=self.reiniciar, bg="#16A34A", fg="white", font=("Arial", 11, "bold")).pack(fill="x", padx=10)

        self.lbl_info = tk.Label(self.panel_izquierdo, text="Esperando simulación...", justify="left", bg="#F3F4F6")
        self.lbl_info.pack(padx=10, pady=15, anchor="w")

    def crear_panel_simulacion(self):
        self.canvas = tk.Canvas(self.panel_derecho, bg="#0F172A")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.dibujar_poblacion)

        self.texto_resultados = tk.Text(self.panel_derecho, height=10, bg="#111827", fg="#F9FAFB")
        self.texto_resultados.pack(fill="x", padx=5, pady=5)

    def dibujar_poblacion(self, event=None):
        self.canvas.delete("all")
        matriz = self.motor.obtener_matriz()
        if not matriz:
            return

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()
        filas = len(matriz)
        columnas = len(matriz[0])
        celda_w = max(10, (ancho - 40) // columnas)
        celda_h = max(10, (alto - 40) // filas)

        for i in range(filas):
            for j in range(columnas):
                estado = matriz[i][j]
                color = "#FFFFFF"
                if estado == 2:
                    color = "#DC2626"
                elif estado == 3:
                    color = "#16A34A"
                elif estado == 4:
                    color = "#111827"
                elif estado == 0:
                    color = "#E5E7EB"
                self.canvas.create_rectangle(j * celda_w + 10, i * celda_h + 10, (j + 1) * celda_w + 10, (i + 1) * celda_h + 10, fill=color, outline="#94A3B8")

    def actualizar_estado(self):
        datos = self.motor.estadisticas()
        self.lbl_info.config(text=f"Generación: {datos['generacion']}\nSanos: {datos['sanos']}\nInfectados: {datos['infectados']}\nRecuperados: {datos['recuperados']}\nFallecidos: {datos['fallecidos']}")

    def reiniciar(self):
        try:
            filas = int(self.var_filas.get())
            columnas = int(self.var_columnas.get())
            infectados = int(self.var_infectados.get())
            prob = float(self.var_prob.get())
            dias = int(self.var_dias.get())
            muerte = float(self.var_muerte.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")
            return

        self.motor = MotorCovid(filas=filas, columnas=columnas, infectados_iniciales=infectados, probabilidad_contagio=prob, dias_recuperacion=dias, probabilidad_muerte=muerte)
        self.estadisticas = EstadisticasCovid()
        self.graficos = GraficosCovid()
        self.dibujar_poblacion()
        self.actualizar_estado()
        self.texto_resultados.delete("1.0", tk.END)
        self.texto_resultados.insert(tk.END, "Simulación reiniciada")

    def simular(self):
        try:
            filas = int(self.var_filas.get())
            columnas = int(self.var_columnas.get())
            infectados = int(self.var_infectados.get())
            prob = float(self.var_prob.get())
            dias = int(self.var_dias.get())
            muerte = float(self.var_muerte.get())
        except ValueError:
            messagebox.showerror("Error", "Ingresa valores numéricos válidos")
            return

        self.motor = MotorCovid(filas=filas, columnas=columnas, infectados_iniciales=infectados, probabilidad_contagio=prob, dias_recuperacion=dias, probabilidad_muerte=muerte)
        self.estadisticas = EstadisticasCovid()
        self.graficos = GraficosCovid()

        self.texto_resultados.delete("1.0", tk.END)
        self.texto_resultados.insert(tk.END, "Generando simulación...\n")
        self.root.update_idletasks()

        for _ in range(10):
            self.motor.avanzar()
            datos = self.motor.estadisticas()
            self.estadisticas.guardar(self.motor.obtener_matriz(), datos["generacion"])
            self.graficos.agregar(datos)
            self.actualizar_estado()
            self.dibujar_poblacion()
            self.root.update_idletasks()

        self.texto_resultados.delete("1.0", tk.END)
        self.texto_resultados.insert(tk.END, "Simulación completada.\n")
        self.texto_resultados.insert(tk.END, f"Generaciones: {self.graficos.total_generaciones()}\n")
        self.texto_resultados.insert(tk.END, f"Infectados finales: {self.motor.infectados()}\n")
        self.texto_resultados.insert(tk.END, f"Recuperados finales: {self.motor.recuperados()}\n")
        self.texto_resultados.insert(tk.END, f"Fallecidos finales: {self.motor.fallecidos()}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = CovidApp(root)
    root.mainloop()
