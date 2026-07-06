# ==========================================
# ruleta.py - CASINO PRO CON ANIMACIÓN
# ==========================================

import tkinter as tk
from tkinter import messagebox
import random

from motor_ruleta import jugar


class RuletaApp:

    def __init__(self, root):

        self.root = root
        self.root.title("🎰 Casino Ruleta Pro")
        self.root.geometry("1200x800")
        self.root.configure(bg="black")

        # 💰 saldo
        self.var_apuesta = tk.IntVar(value=10)
        self.saldo = 1000

        # 🎯 apuesta
        self.tipo = None
        self.valor = None

        # 🎡 animación
        self.ultimo = None
        self.girando = False

        self.crear_ui()

    # =========================
    # UI
    # =========================
    def crear_ui(self):

        # 🎯 INFO SELECCIÓN
        self.panel_info = tk.Frame(self.root, bg="black")
        self.panel_info.pack(fill="x")

        self.lbl_info = tk.Label(
            self.panel_info,
            text="🎯 Selección: ninguna",
            fg="white",
            bg="black",
            font=("Arial", 12, "bold")
        )
        self.lbl_info.pack(pady=5)

        # 🎡 RUEDA
        self.top = tk.Frame(self.root, bg="#0b6623", height=350)
        self.top.pack(side="top", fill="both", expand=True)

        # 💰 BARRA SALDO
        self.bar = tk.Frame(self.root, bg="#111")
        self.bar.pack(fill="x")

        # 🎲 TABLA
        self.bottom = tk.Frame(self.root, bg="#1a1a1a")
        self.bottom.pack(side="bottom", fill="both")

        self.crear_ruleta()
        self.crear_barra_saldo()
        self.crear_tabla()

    # =========================
    # 🎡 RULETA
    # =========================
    def crear_ruleta(self):

        self.canvas = tk.Canvas(self.top, bg="#0b6623")
        self.canvas.pack(fill="both", expand=True)

    def dibujar_base(self):
        self.canvas.delete("all")

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        cx, cy = w // 2, h // 2
        r = min(w, h) // 4

        self.canvas.create_text(
            cx, 40,
            text="🎰 RULETA CASINO",
            fill="white",
            font=("Arial", 20, "bold")
        )

        self.canvas.create_oval(
            cx - r, cy - r,
            cx + r, cy + r,
            outline="gold",
            width=4
        )

        return cx, cy

    # =========================
    # 💰 BARRA SALDO
    # =========================
    def crear_barra_saldo(self):

        tk.Label(self.bar, text="💰 SALDO:", fg="white", bg="#111").pack(side="left", padx=10)

        self.lbl_saldo = tk.Label(
            self.bar,
            text=str(self.saldo),
            fg="gold",
            bg="#111",
            font=("Arial", 12, "bold")
        )
        self.lbl_saldo.pack(side="left")

        tk.Label(self.bar, text="Apuesta:", fg="white", bg="#111").pack(side="left")

        tk.Entry(self.bar, textvariable=self.var_apuesta, width=10).pack(side="left")

        tk.Button(
            self.bar,
            text="🎰 GIRAR",
            bg="green",
            fg="white",
            command=self.girar
        ).pack(side="right", padx=20)

    # =========================
    # 🎲 TABLA
    # =========================
    def crear_tabla(self):

        tk.Label(
            self.bottom,
            text="🎲 TABLA 0–36",
            fg="white",
            bg="#1a1a1a",
            font=("Arial", 14, "bold")
        ).pack(pady=5)

        grid = tk.Frame(self.bottom, bg="#1a1a1a")
        grid.pack()

        rojos = {
            1,3,5,7,9,12,14,16,18,
            19,21,23,25,27,30,32,34,36
        }

        for n in range(37):

            if n == 0:
                bg = "#00aa00"
            elif n in rojos:
                bg = "#b30000"
            else:
                bg = "#111"

            tk.Button(
                grid,
                text=str(n),
                width=4,
                height=2,
                bg=bg,
                fg="white",
                font=("Arial", 10, "bold"),
                command=lambda n=n: self.sel("numero", n)
            ).grid(row=n // 7, column=n % 7, padx=2, pady=2)

        tk.Button(self.bottom, text="🔴 ROJO",
                  bg="red", fg="white",
                  command=lambda: self.sel("color", "rojo")).pack(fill="x")

        tk.Button(self.bottom, text="⚫ NEGRO",
                  bg="black", fg="white",
                  command=lambda: self.sel("color", "negro")).pack(fill="x")

    # =========================
    # 🎯 SELECCIÓN
    # =========================
    def sel(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.lbl_info.config(text=f"🎯 Selección: {tipo} → {valor}")

    # =========================
    # 🎰 GIRAR
    # =========================
    def girar(self):

        if self.girando:
            return

        if not self.tipo:
            messagebox.showwarning("Casino", "Selecciona apuesta")
            return

        try:
            monto = int(self.var_apuesta.get())
        except:
            messagebox.showerror("Error", "Monto inválido")
            return

        # 🎯 resultado real del motor
        self.ultimo = jugar(0, self.tipo, self.valor, monto)

        # 🎡 iniciar animación
        self.girando = True
        self.animar_ruleta(30)

    # =========================
    # 🎡 ANIMACIÓN RULETA
    # =========================
    def animar_ruleta(self, delay):

        cx, cy = self.dibujar_base()

        num = random.randint(0, 36)

        self.canvas.create_text(
            cx, cy,
            text=str(num),
            fill="white",
            font=("Arial", 50, "bold"),
            tags="anim"
        )

        # ⏱ desaceleración
        if delay < 180:
            delay += 10

        # 🎯 FINAL
        if delay >= 180:

            self.canvas.delete("anim")

            final = self.ultimo["numero"]

            self.canvas.create_text(
                cx, cy,
                text=str(final),
                fill="yellow",
                font=("Arial", 60, "bold")
            )

            self.girando = False

            # 💰 actualizar saldo
            self.saldo += self.ultimo["ganancia"]
            self.lbl_saldo.config(text=str(self.saldo))

            self.mostrar_resultado()
            return

        self.root.after(delay, lambda: self.animar_ruleta(delay))

    # =========================
    # 💥 RESULTADO
    # =========================
    def mostrar_resultado(self):

        r = self.ultimo

        if r["gano"]:
            msg = f"🎉 GANASTE\nNúmero: {r['numero']}"
        else:
            msg = f"💀 PERDISTE\nNúmero: {r['numero']}"

        messagebox.showinfo("Resultado", msg)


# =========================
# 🚀 RUN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = RuletaApp(root)
    root.mainloop()