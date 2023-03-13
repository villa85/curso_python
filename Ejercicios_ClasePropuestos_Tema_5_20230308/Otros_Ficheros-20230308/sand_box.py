def lista_compra():
    l = []
    f = ""
    stop = True
    while stop:
        f = input("Ingrese procductos a la lista de la compra (Fin para finalizar):  ")
        if f.lower() != "fin":
            l.append(f)
        else:
            stop = False
    return l

l = lista_compra()
print(f"{l}")

def cant_x_prod(lista_p):
    d = {}
    cant = len(lista_p)
    while cant > 0:
        for i in lista_p:
            c = input(f"Introduzca la cantidad de {i}: ")
            d.update( {i: c})
            cant -= 1
    return d

# z = ["agua", "pan", "aceite"]
d = cant_x_prod(l)
print(d)