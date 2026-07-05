import tkinter as tk
from tkinter import ttk, messagebox

from motor_ruleta import jugar
from estrategias import crear_estrategia
from estadisticas import Estadisticas


class RuletaApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta Monte Carlo")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 650)

        self.estadisticas = Estadisticas(1000)
        self.estrategia = crear_estrategia("Martingala", 10)

        self.var_capital = tk.IntVar(value=1000)
        self.var_apuesta = tk.IntVar(value=10)
        self.var_tipo = tk.StringVar(value="color")
        self.var_valor = tk.StringVar(value="Rojo")
        self.var_estrategia = tk.StringVar(value="Martingala")

        self.ultimo_resultado = None
        self.casillas = {}

        self.crear_interfaz()

    def crear_interfaz(self):
        self.panel_izquierdo = tk.Frame(self.root, width=260, bg="#ECECEC")
        self.panel_izquierdo.pack(side="left", fill="y")

        self.panel_derecho = tk.Frame(self.root)
        self.panel_derecho.pack(side="right", fill="both", expand=True)

        self.crear_panel_control()
        self.crear_canvas()

    def crear_panel_control(self):
        tk.Label(
            self.panel_izquierdo,
            text="RULETA",
            font=("Arial", 18, "bold"),
            bg="#ECECEC"
        ).pack(pady=10)

        tk.Label(self.panel_izquierdo, text="Capital Inicial", bg="#ECECEC").pack()
        tk.Entry(self.panel_izquierdo, textvariable=self.var_capital).pack(fill="x", padx=15)

        tk.Label(self.panel_izquierdo, text="Monto Apuesta", bg="#ECECEC").pack(pady=(10, 0))
        self.entry_apuesta = tk.Entry(self.panel_izquierdo, textvariable=self.var_apuesta)
        self.entry_apuesta.pack(fill="x", padx=15)

        tk.Label(self.panel_izquierdo, text="Estrategia", bg="#ECECEC").pack(pady=(10, 0))
        self.combo_estrategia = ttk.Combobox(
            self.panel_izquierdo,
            textvariable=self.var_estrategia,
            state="readonly",
            values=["Martingala", "Fibonacci", "DAlembert", "Fija"],
        )
        self.combo_estrategia.pack(fill="x", padx=15)

        tk.Label(self.panel_izquierdo, text="Tipo de apuesta", bg="#ECECEC").pack(pady=(10, 0))
        self.combo_tipo = ttk.Combobox(
            self.panel_izquierdo,
            textvariable=self.var_tipo,
            state="readonly",
            values=["color", "numero", "paridad", "mitad", "docena", "columna"],
        )
        self.combo_tipo.pack(fill="x", padx=15)

        tk.Label(self.panel_izquierdo, text="Valor", bg="#ECECEC").pack(pady=(10, 0))
        self.entry_valor = tk.Entry(self.panel_izquierdo, textvariable=self.var_valor)
        self.entry_valor.pack(fill="x", padx=15)

        tk.Button(
            self.panel_izquierdo,
            text="🎲 GIRAR",
            bg="green",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.girar,
        ).pack(fill="x", padx=15, pady=20)

        self.lbl_resultado = tk.Label(
            self.panel_izquierdo,
            text="Esperando jugada...",
            bg="#ECECEC",
            justify="left",
        )
        self.lbl_resultado.pack(pady=10)

        self.lista = tk.Listbox(self.panel_izquierdo, height=10)
        self.lista.pack(fill="x", padx=15, pady=(10, 0))

        self.lbl_estadisticas = tk.Label(
            self.panel_izquierdo,
            text="Estadísticas",
            bg="#ECECEC",
            justify="left",
        )
        self.lbl_estadisticas.pack(pady=10)

    def crear_canvas(self):
        self.canvas = tk.Canvas(self.panel_derecho, bg="#0B6623")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.dibujar_mesa)

    def dibujar_mesa(self, event=None):
        self.canvas.delete("all")

        ancho = self.canvas.winfo_width()
        alto = self.canvas.winfo_height()

        self.canvas.create_text(ancho // 2, 30, text="MESA DE RULETA", fill="white", font=("Arial", 20, "bold"))
        self.canvas.create_rectangle(50, 60, ancho - 50, alto - 80, outline="gold", width=3)

        if self.ultimo_resultado is None:
            self.canvas.create_text(ancho // 2, alto // 2, text="La mesa se dibujará aquí", fill="white", font=("Arial", 18))
            return

        self.canvas.create_text(ancho // 2, alto // 2 - 40, text="Último resultado", fill="white", font=("Arial", 16, "bold"))
        self.canvas.create_text(
            ancho // 2,
            alto // 2,
            text=f"Número: {self.ultimo_resultado['numero']}\nColor: {self.ultimo_resultado['color']}\n{'GANÓ' if self.ultimo_resultado['gano'] else 'PERDIÓ'}",
            fill="white",
            font=("Arial", 18),
        )

    def redibujar(self):
        self.dibujar_mesa()

    def _valor_para_apuesta(self):
        tipo = self.var_tipo.get().lower()
        valor = self.var_valor.get().strip()

        if tipo == "mitad":
            if valor.lower() in {"1", "1-18", "primera", "primera mitad"}:
                return 1
            return 2

        if tipo in {"docena", "columna", "numero"}:
            try:
                return int(valor)
            except ValueError:
                return valor

        return valor

    def actualizar_estadisticas(self):
        resumen = self.estadisticas.resumen()
        self.lbl_estadisticas.config(
            text=(
                f"Capital: {resumen['capital']}\n"
                f"Jugadas: {resumen['jugadas']}\n"
                f"Aciertos: {resumen['ganadas']} ({resumen['porcentaje']}%)\n"
                f"Racha ganadora: {resumen['racha_ganadora']}\n"
                f"Racha perdedora: {resumen['racha_perdedora']}"
            )
        )

    def girar(self):
        try:
            monto = int(self.var_apuesta.get())
            if monto <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Ingrese una apuesta válida.")
            return

        nombre = self.var_estrategia.get()
        self.estrategia = crear_estrategia(nombre, monto)

        tipo = self.var_tipo.get().lower()
        valor = self._valor_para_apuesta()

        resultado = jugar(tipo, valor, monto)
        self.estadisticas.registrar(resultado)

        self.ultimo_resultado = resultado
        self.redibujar()

        numero = resultado["numero"]
        texto = f"Número: {numero}\nColor: {resultado['color']}\n"
        texto += "Resultado: GANÓ" if resultado["gano"] else "Resultado: PERDIÓ"
        self.lbl_resultado.config(text=texto)

        self.lista.insert(tk.END, f"{numero} ({resultado['color']})")
        if self.lista.size() > 20:
            self.lista.delete(0)

        self.var_apuesta.set(int(self.estrategia.actualizar(resultado["gano"])))
        self.actualizar_estadisticas()


if __name__ == "__main__":
    root = tk.Tk()
    app = RuletaApp(root)
    root.mainloop()