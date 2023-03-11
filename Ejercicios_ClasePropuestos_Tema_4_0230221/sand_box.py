import time

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

@timer
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

t = convertir_a_romano(10000000)

print(t)

