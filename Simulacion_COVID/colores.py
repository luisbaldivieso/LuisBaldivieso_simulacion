"""
===========================================================
PROYECTO FINAL - SIMULACIÓN COVID
Archivo: colores.py

Este archivo contiene todos los estados posibles de una
persona dentro de la simulación y los colores que serán
utilizados para dibujar la cuadrícula.

Todos los demás módulos importarán este archivo.
===========================================================
"""

# ==========================================================
# ESTADOS DE LAS CELDAS
# ==========================================================

VACIO = 0
SANO = 1
INFECTADO = 2
RECUPERADO = 3
FALLECIDO = 4


# ==========================================================
# NOMBRES DE LOS ESTADOS
# ==========================================================

NOMBRES_ESTADOS = {
    VACIO: "Vacío",
    SANO: "Sano",
    INFECTADO: "Infectado",
    RECUPERADO: "Recuperado",
    FALLECIDO: "Fallecido"
}


# ==========================================================
# COLORES DE CADA ESTADO
# (Tkinter acepta nombres o códigos HEX)
# ==========================================================

COLORES = {

    VACIO: "#FFFFFF",          # Blanco
    SANO: "#2ECC71",           # Verde
    INFECTADO: "#E74C3C",      # Rojo
    RECUPERADO: "#3498DB",     # Azul
    FALLECIDO: "#2C3E50"       # Negro / Gris oscuro

}


# ==========================================================
# LEYENDA
# ==========================================================

LEYENDA = [

    ("Vacío", COLORES[VACIO]),
    ("Sano", COLORES[SANO]),
    ("Infectado", COLORES[INFECTADO]),
    ("Recuperado", COLORES[RECUPERADO]),
    ("Fallecido", COLORES[FALLECIDO])

]


# ==========================================================
# FUNCIÓN PARA OBTENER EL COLOR
# ==========================================================

def obtener_color(estado):
    """
    Devuelve el color correspondiente al estado recibido.
    """

    return COLORES.get(estado, "#FFFFFF")


# ==========================================================
# FUNCIÓN PARA OBTENER EL NOMBRE
# ==========================================================

def obtener_nombre(estado):
    """
    Devuelve el nombre del estado.
    """

    return NOMBRES_ESTADOS.get(estado, "Desconocido")


# ==========================================================
# FUNCIÓN PARA VALIDAR UN ESTADO
# ==========================================================

def estado_valido(estado):
    """
    Verifica si un estado existe.
    """

    return estado in NOMBRES_ESTADOS


# ==========================================================
# LISTA GENERAL DE ESTADOS
# ==========================================================

ESTADOS = [

    VACIO,
    SANO,
    INFECTADO,
    RECUPERADO,
    FALLECIDO

]