import re

def texto_en_minusculas(cadena):
    """
    Funcición que devuelve una cadena todo en minusculas
    parametros: String
    return: String
    """
    texto = "".join(cadena.lower())
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

def normalize(s, find = False):
    if find:
        lista = ["á", "é", "í", "ó", "ú"]
        lista_sig = []
        for i in s:
            if i in lista:
                lista_sig.append(i)
        return lista_sig
    else:
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

def extrae_numeros(s, number = False):
    patron = '[^0-9]+'
    p = '[0-9]+'
    l = []
    if number:
        l = re.findall(p, s)
        return l
    else:
        l = re.findall(patron, s)
        cadena = "".join(l)
        return cadena
