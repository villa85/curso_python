import re

def texto_en_minusculas(cadena):
    """
    Funcición que devuelve una cadena todo en minusculas
    parametros: String
    return: String
    """
    texto = " ".join(cadena.lower())
    return texto

def split_cadena(cadena):
    return cadena.split()

def elimina_signos_puntuacion(cadena, signos = False):
    """
    Función que devuelve una cadena sin signos de puntuación o
    devuelve un listado con todos los signos de puntuación
    parametros: String
    return: String o Lista
    """
    if signos:
        patron = '[¡!.*“”"(),¿?;]+'
        texto = re.findall(patron, cadena)
        lista = []
        cadena = ""
        for i in texto:
            if len(i) > 0:
                # print(len(i))
                lista.append(i)
        return lista
    else:
        patron = '[^¡!.*“”"(),¿?; ]+'
        texto = " ".join(re.findall(patron, cadena))
        return texto

def elimina_repetidos(cadena):
    """
    Función que devuelve una lista de sin elementos repetidos
    parametros: Lista
    return: Lista
    """
    for i in cadena:
        if cadena.count(i) > 1:
            cadena.remove(i)
    return cadena