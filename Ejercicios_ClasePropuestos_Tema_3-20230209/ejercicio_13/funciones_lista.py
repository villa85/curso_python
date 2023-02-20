def maximo_valor(lista):
    mayor = lista[0]
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor

def minimo_valor(lista):
    menor = lista[0]
    for i in lista:
        if i < menor:
            menor = i
    return menor

def pares(lista, par = False):
    lista_pares = []
    lista_impares = []
    if par:
        for i in lista:
            if i % 2 == 0:
                lista_pares.append(i)
        return lista_pares
    else:
        for i in lista:
            if i % 2 != 0:
                lista_impares.append(i)
        return lista_impares

def sumatoria(lista):
    return sum(lista)

def promedio(suma, lista):
    return suma / len(lista)