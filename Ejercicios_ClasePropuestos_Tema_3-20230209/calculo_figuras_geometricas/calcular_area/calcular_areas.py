# con esta funcion calculamos el area de cualquier paralerogramo (cuadrado, rectángulo)
import math


def area_paralelogramo(b, h=None, cuadrado=False):
    if not cuadrado:
        area_rectangulo = b * h
        return area_rectangulo
    elif cuadrado:
        area_cuadrado = math.pow(b, 2)
        return area_cuadrado


def area_triangulo(base, altura):
    return base * altura / 2


def area_rombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2


def area_circulo(radio):
    return math.pi * radio ** 2


def area_trapecio(B, b, h):
    return ((B + b) / 2) * h


def area_poligono_regular(cant_lados, medida_lados, apotema):
    return ((cant_lados * medida_lados) * apotema) / 2

