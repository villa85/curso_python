# Introduzca su código aqui
lista = [3, 67, "cat", [56, 57, "dog"], [5, 6, "bird" ], 3.14, [96, 85, "leche", 100], False]


def une_listas(l):

    p =0
    c = len(l)

    while c > 0:
        for i in l:
            if isinstance(i, list):
                p = l.index(i)
                lv = l.pop(p)
                for j in range(len(lv)):
                    l.insert(p, lv[j])
                    p +=1
        c -= 1
    return l

l = une_listas(lista)

print(l)