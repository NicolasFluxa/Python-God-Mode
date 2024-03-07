mi_lista = [1, 2, 3, 4, 5, 6]


def doble(x):
    return x * 2


listaNueva = [doble(x) for x in mi_lista]
listaNueva2 = list(map(doble, mi_lista))

print(listaNueva)

print(listaNueva2)