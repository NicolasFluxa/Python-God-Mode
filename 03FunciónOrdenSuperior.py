def operacion(numr, funcion):
    return funcion(numr)


def raiz(numr):
    return numr**0.5


def cubo(numr):
    return numr**3


def cuadrado(numr):
    return numr**2


print(operacion(16, raiz))
print(operacion(16, cubo))
print(operacion(16, cuadrado))

# Dada la función operacion, la cual recibe dos parametros,
# retorna el nombre de la función con el respectivo argumento

