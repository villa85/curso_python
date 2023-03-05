import re
import time

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('La función tardó {0} segundos'.format(t2-t1))
        return f
    return inner

def texto_en_minusculas(cadena):
    """
    Funcición que devuelve una cadena todo en minusculas
    parametros: String
    return: String
    """
    texto = "".join(cadena.lower())
    return texto


def split_cadena(cadena):
    return cadena.split(" ")

def elimina_signos_puntuacion(s, signos = False):
    """
    Función que devuelve una cadena sin signos de puntuación o
    devuelve un listado con todos los signos de puntuación
    parametros: String , Booleano
    return: String o Lista
    """
    if signos:
        patron = '[^a-zA-Z0-9|á|é|í|ó|ú|ñ|\w ]+'
        texto = re.findall(patron, s)
        return texto
    else:
        patron =  '[^a-zA-Z0-9|á|é|í|ó|ú|ñ|\w]+'
        s = re.sub("j[aeoujm]+","",s) # elimina las risas
        return re.sub(patron, " ", s)

def elimina_repetidos(cadena):
    """
    Función que devuelve una lista de sin elementos repetidos
    parametros: Lista
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
    """
    Función que devuelve un texto sin números o uno con los números encontrados
    parametros: String, Booleano
    return: String
    """
    patron = '[0-9]+'
    p = '[^0-9]+'
    if number:
        return re.sub(p, " ", s)
    else:
        return re.sub(patron, "", s)

def extrae_mayusculas(s, siglas = False):
    """
    Función que devuelve extrae las palabras en mayusculas o las siglas 
    parametros: String, Booleano
    return: Lista
    """
    patron = '[A-Z][a-z|á|é|í|ó|ú]+' # Palablas en mayusculas
    p = '[A-Z][A-Z]+' # Siglas
    if siglas:
        return re.findall(p, s)
    else:
        return re.findall(patron, s)

def elimina_stop_words(cadena, stop_w, stw = False):
    """
    Función que devuelve el texto sin la stop_words o las stop_words encontrdas
    parametros: String, Stop_Words, Booleano
    return: String
    """
    lista = cadena.split()
    s = ""
    if stw: # si stw es True devuelve las stop_word
        for i in lista:
            if i in stop_w:
                s += i+ " "
        return s
    else: # el texto sin stop_word
        for i in lista:
                if i not in stop_w:
                    s += i+ " "
        return s

def contar_palabras(s):
    """
    Función que devuelve una lista de tuplas("palabra", cantidad)
    parametros: String
    return: Lista
    """
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
    return result

def extraer_url(s):
    """
    Función que elimina las urls de un texto
    parametros: String
    return: String
    """
    patron_5 = "http[s]*\S+" #'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL  "http[s]*\S+"
    return re.sub(patron_5, "", s)


def extraer_usuarios(s):
    """
    Función que elimina los usuarios de un texto
    parametros: String
    return: String
    """
    patron_5 = "(@[^  \ ]*)"  # Usuarios @usuarioabc
    return re.sub(patron_5, "", s)


def normaliza(s):
    """
    Función que toma el archivo de palabras posistivas o negativas
    y la convierte en una lista de tuplas [("palabla", float)]
    parametros: String
    return: Lista
    """
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
    """
    Función que devuelve el total del puntaje de una lista
    parametros: lista
    return: float
    """
    suma = 0
    for i in l:
        suma += i[1]
    return suma
