# Esta línea importa el módulo 'random' con el alias 'rd'.
# Este módulo contiene funciones para generar números aleatorios.
import random as rd

# Esta línea crea una lista llamada 'lista' con 10 números aleatorios entre 1 y 11.
lista = [rd.randint(1, 11) for i in list(range(1, 11))]

# Estas líneas inicializan las variables 'valorMenor' y 'valorMayor'
# con el primer elemento de la lista.
valorMenor = lista[0]
valorMayor = lista[0]

# Este bucle 'for' recorre cada número en la lista.
for num in lista:
    # Si el número actual es menor que 'valorMenor',
    # entonces 'valorMenor' se actualiza con este número.
    if num < valorMenor:
        valorMenor = num
    # Si el número actual es mayor que 'valorMayor',
    # entonces 'valorMayor' se actualiza con este número.
    elif num > valorMayor:
        valorMayor = num

# Estas líneas imprimen la lista completa, el valor menor y el valor mayor.
print(lista)
print(valorMenor)
print(valorMayor)
