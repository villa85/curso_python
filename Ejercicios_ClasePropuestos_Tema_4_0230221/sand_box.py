import time
import re

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        print('La función tardó {0} segundos'.format(t2-t1))
        return f
    return inner

# @timer
# def convertir_a_romano(entero):
#     numeros = [1000,9000,500,400,100,90,50,40,10,9,5,4,1]
#     romanos = ["M","CM","D","CD","C","XC","L", "XL","X","IX","V","IV","I"]
#     zipped = zip(romanos, numeros)
#     dicc = dict(zipped)

#     romano = ""
#     i = 0

#     while entero > 0:

#         for _ in range (entero // list(dicc.values())[i]):
#                 romano += list(dicc.keys())[i]
#                 entero -= list(dicc.values())[i]
#         i += 1
#     return romano

def convertir_a_romano(entero):
    numeros = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romanos = ["M","CM","D","CD","C","XC","L", "XL","X","IX","V","IV","I"]

    romano = ""
    i = 0

    while entero > 0:
        for _ in range(entero // numeros[i]):
            romano += romanos[i]
            entero -= numeros[i]
        i += 1
    return romano

t = convertir_a_romano(1985)

# print(t)

def convert_to_normal(valor):
        numeros = list(reversed([1000,900,500,400,100,90,50,40,10,9,5,4,1]))
        romanos = list(reversed(["M","CM","D","CD","C","XC","L", "XL","X","IX","V","IV","I"]))
        zipped = zip(romanos, numeros)
        dicc = dict(zipped)

        entero = 0
        i = 12
        for i in range(len(valor)):
            if dicc[valor[i]] > dicc[valor[i - 1]]:
                entero += dicc[valor[i]] - 2 * dicc[valor[i - 1]]
            else:
                entero += dicc[valor[i]]
        return entero

# h = convert_to_normal("MCMLXXXV")
# print(h)

def romano_a_entero(romano):
    n = list(reversed([1000,900,500,400,100,90,50,40,10,9,5,4,1]))
    r = list(reversed(["M","CM","D","CD","C","XC","L", "XL","X","IX","V","IV","I"]))
    zipped = zip(r, n)
    dic_romanos = dict(zipped)
    entero = 0

    for i in range(len(romano)):
        if i > 0 and dic_romanos[romano[i]] > dic_romanos[romano[i - 1]]:
            entero += dic_romanos[romano[i]] - 2 * dic_romanos[romano[i - 1]]
        else:
            entero += dic_romanos[romano[i]]

    return entero

x = romano_a_entero("V")

print(x)



patron = r"^M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$"	# Do not delete 'r'.

