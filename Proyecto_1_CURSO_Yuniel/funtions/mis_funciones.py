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
        patron = '[^a-zA-Z0-9|á|é|í|ó|ú|ñ|\w ]+'
        texto = re.findall(patron, cadena)
        return texto
    else:
        patron =  '[a-zA-Z0-9|á|é|í|ó|ú|ñ|\w]+'
        texto = " ".join(re.findall(patron, cadena))
        return texto

def elimina_repetidos(cadena):
    """
    Función que devuelve una lista de sin elementos repetidos
    parametros: Lista, Booleano
    return: Lista
    """
    lista =[]
    for i in cadena:
        if i not in lista:
            lista.append(i)
    return lista

def letras_acentuadas(s, find = False):
    """
    Función que devuelve una lista con todas las letras acentuadas o
    reemplaza las letras acentuadas por las mismas sin acentuar
    parametros: String, Booleano
    return: String o Lista
    """
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

def extrae_mayusculas(s, siglas = False):
    patron = '[A-Z][a-z|á|é|í|ó|ú]+' # Palablas en mayusculas
    p = '[A-Z][A-Z]+' # Siglas
    l = []
    if siglas:
        l = re.findall(p, s)
        return l
    else:
        l = re.findall(patron, s)
        return l

def elimina_stop_words(cadena, stop_w, stw = False):
    """
    Función que devuelve el texto sin la stop_words o las stop_words encontrdas
    parametros: String, Stop_Words, Booleano
    return: String
    """
    l = []
    lista = cadena.split()
    lista_stop_w = stop_w.split()
    if stw: # si stw es True devuelve las stop_word
        for i in lista:
            if i in stop_w:
                l.append(i)
                s = " ".join(l)
        return s
    else: # el texto sin stop_word
        for i in lista_stop_w:
            for j in lista:
                if i == j:
                    lista.remove(j)
        s = " ".join(lista)
        return s
        # for i in lista:
        #     if i not in stop_w:
        #         l.append(i)
        #         s = " ".join(l)
        # return s


def contar_palabras(s):
    l = s.split()
    lista_tupla = []
    result = []
    t = []
    for i in l:
        t = i, l.count(i)
        lista_tupla.append(t)
    for j in lista_tupla:
        if j not in result:
            result.append(j)
    # for k in result:
    #     t.append((result[0], float(result[1])))
    return result

def extraer_url(s):
    patron_5 = "http[s]*\S+" #'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL  "http[s]*\S+"
    url_list = []
    url_list = re.findall(patron_5, s)
    for i in url_list:
        if i in s:
            s = re.sub(i, "", s)
    return s

def extraer_usuarios(s):
    patron_5 = "(@[^  \ ]*)"  # Usuarios @usuarioabc
    user_list = []
    user_list = re.findall(patron_5, s)
    for i in user_list:
        if i in s:
            s = re.sub(i, "", s)
    return s

def normaliza(s): # toma el archivo de palabras posistivas o negativas y la convierte en una lista de tuplas [("palabla", float)]
    l = (s.split("\n"))
    li = []
    t = []
    for i in l:
        li = i.split()
        t.append((li[0], float(li[1])))
    return t

def calculo_puntuacion_palabras(p, texto):
    """
    Función que devuelve listado con la puntuación por palabra de un texto
    parametros: lista de palabras con su puntuacion, texto normalizado con la cantidad por palabras
    return: lista de palabras y puntuacion
    """
    lista_total_palabras = []
    for i in p:
        for j in texto:
            if i[0] == j[0]:
                lista_total_palabras.append((i[0], i[1]*j[1]))
    return lista_total_palabras

def total_puntuacion(l):
    suma = 0
    for i in l:
        suma += i[1]
    return suma
