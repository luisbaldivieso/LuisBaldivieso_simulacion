"""
reportes.py
Exportación de datos.
"""

import csv
from tkinter import filedialog, messagebox


def exportar_csv(tiempo, stock, procesamiento):

    if tiempo is None:

        messagebox.showwarning(
            "Aviso",
            "No existen datos para exportar."
        )

        return

    ruta = filedialog.asksaveasfilename(

        defaultextension=".csv",

        filetypes=[

            ("Archivo CSV","*.csv")

        ]

    )

    if not ruta:

        return

    with open(ruta,"w",newline="",encoding="utf-8") as archivo:

        escritor = csv.writer(archivo)

        escritor.writerow([

            "Tiempo",

            "Stock",

            "Procesamiento"

        ])

        for t,x,y in zip(

            tiempo,

            stock,

            procesamiento

        ):

            escritor.writerow([

                round(t,2),

                round(x,2),

                round(y,2)

            ])

    messagebox.showinfo(

        "Proceso terminado",

        "Archivo CSV guardado correctamente."

    )


def exportar_imagen(figura):

    ruta = filedialog.asksaveasfilename(

        defaultextension=".png",

        filetypes=[

            ("Imagen PNG","*.png")

        ]

    )

    if not ruta:

        return

    figura.savefig(

        ruta,

        dpi=300,

        bbox_inches="tight"

    )

    messagebox.showinfo(

        "Proceso terminado",

        "Imagen guardada correctamente."

    )