mi_lista = [1, 2, 3, 4, 5, 6]


def doble (x):
    for i, n in enumerate(x):
        x[i] *= 2


doble(mi_lista)

print(mi_lista)
