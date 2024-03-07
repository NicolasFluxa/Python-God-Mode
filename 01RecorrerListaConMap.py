# Esta línea crea una lista llamada 'mi_lista' con los números del 1 al 6.
mi_lista = [1, 2, 3, 4, 5, 6]

# Aquí se define una función llamada 'doble' que toma un número
# 'x' como entrada y devuelve el doble de 'x'.
def doble(x):
    return x * 2

# Esta línea crea una nueva lista llamada 'listaNueva'.
# Para cada número 'x' en 'mi_lista', aplica la función 'doble'
# y guarda el resultado en 'listaNueva'.
listaNueva = [doble(x) for x in mi_lista]

# Esta línea hace lo mismo que la anterior, pero utilizando
# la función 'map'. 'map' aplica una función a todos los elementos de una lista.
listaNueva2 = list(map(doble, mi_lista))

# Esta línea imprime en la consola el contenido de 'listaNueva'.
print(listaNueva)

# Esta línea imprime en la consola el contenido de 'listaNueva2'.
print(listaNueva2)
