'''Módulo para calcular el volumen de diferentes figuras geométricas'''

from math import pi

def volumen_ortoedro(lado, profundidad , altura):

    volumen = lado * profundidad * altura
    return volumen


def volumen_cubo(lado):
    '''
    :param lado, lo eleva al cubo
    :return: volumen del cubo
    '''
    volumen = lado ** 3
    return volumen


def volumen_prisma(lado, altura):
    '''
    :param lado y altura, vol = (lado**2)*alt
    :return: volumen de un prisma
    '''
    base = lado**2
    volumen = base * altura
    return volumen


def volumen_piramide(lado, altura):
    '''
    :param lado y altura, vol = (lado**2 * altura) / 3
    :volver volumen de una piramide
    '''
    base = lado**2
    volumen = (base * altura) / 3
    return volumen



def volumen_cilindro(radio, altura):
    '''
    :param radio y altura, vol = (pi * r**2) * alt
    :return: volumen del cilindro
    '''
    base = pi * radio ** 2
    volumen = base * altura
    return volumen


def volumen_cono(radio, altura):
    '''
    :param radio y altura, vol = (pi * radio ** 2) / 3
    : return: volumen del cono
    '''
    base = (pi * radio ** 2) / 3
    volumen = base * altura
    return volumen


def volumen_esfera(radio):
    '''
    :param radio, vol = r**3
    :return: volumen esfera
    '''
    volumen = (4/3 * pi) * radio ** 3
    return volumen
