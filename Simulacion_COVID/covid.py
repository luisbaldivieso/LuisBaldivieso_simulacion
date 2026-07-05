import tkinter as tk

from covid_app import CovidApp


if __name__ == "__main__":
    root = tk.Tk()
    app = CovidApp(root)
    root.mainloop()