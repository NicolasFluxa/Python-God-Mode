# Aquí se define una función llamada 'operacion' que toma dos argumentos:
# un número 'numr' y una función 'funcion'.
def operacion(numr, funcion):
    # Esta línea aplica la función 'funcion' al número 'numr' y devuelve el resultado.
    return funcion(numr)

# Aquí se define una función llamada 'raiz' que toma un número 'numr'
# como entrada y devuelve su raíz cuadrada.
def raiz(numr):
    return numr**0.5

# Aquí se define una función llamada 'cubo' que toma un número
# 'numr' como entrada y devuelve su cubo.
def cubo(numr):
    return numr**3

# Aquí se define una función llamada 'cuadrado' que toma un número
# 'numr' como entrada y devuelve su cuadrado.
def cuadrado(numr):
    return numr**2

# Estas líneas llaman a la función 'operacion' con el número 16 y
# cada una de las funciones definidas anteriormente como argumentos. Luego imprimen el resultado.
print(operacion(16, raiz))
print(operacion(16, cubo))
print(operacion(16, cuadrado))
