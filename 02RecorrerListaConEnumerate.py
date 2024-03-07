mi_lista = [1, 2, 3, 4, 5, 6]

# Aquí se define una función llamada 'doble' que toma una lista 'x' como entrada.
def doble(x):

    # Este bucle 'for' recorre la lista 'x'.
    # 'enumerate(x)' devuelve pares de índice-valor,
    # que se almacenan en 'i' y 'n', respectivamente.
    for i, n in enumerate(x):
        # Esta línea multiplica por 2 el elemento de 'x'
        # en la posición 'i'. Como las listas en Python son mutables,
        # esto modifica directamente la lista 'x'.
        x[i] *= 2

# Esta línea llama a la función 'doble' con 'mi_lista'
# como argumento. Como las listas en Python son mutables,
# esto modifica 'mi_lista' directamente.
doble(mi_lista)


# Esta línea imprime en la consola el contenido de 'mi_lista', que ahora ha sido modificada por la función 'doble'.
print(mi_lista)
