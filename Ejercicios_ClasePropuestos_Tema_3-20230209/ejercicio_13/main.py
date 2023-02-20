import random
import funciones_lista as fl


lista = []
for i in range(10):
    lista.append(random.randint(0, 1000))

maxi = fl.maximo_valor(lista)
minimo = fl.minimo_valor(lista)
impares = fl.pares(lista)
pares = fl.pares(lista, par = True)
sumatoria = fl.sumatoria(lista)
promedio = fl.promedio(sumatoria, lista)

print(lista)
print(f"El valor máximo del lista es: {maxi}")
print(f"El valor minimo del lista es: {minimo}")
print(f"Hay {len(impares)} números impares")
print(f"Hay {len(pares)} números impares")
print(f"La sumatoria es {sumatoria}")
print(f"El promedio es {promedio}")