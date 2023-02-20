import random
import funciones_lista as fl


lista = []
for i in range(10):
    lista.append(random.randint(0, 1000))

maxi = fl.maximo_valor(lista)
print(maxi)