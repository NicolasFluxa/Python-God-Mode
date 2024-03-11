
import math  # Importamos la biblioteca math para usar la función factorial.


def calcular_numero_binomial(n):  # Esta función genera el Triángulo de Pascal hasta la fila n.
    # Inicializamos una lista vacía para almacenar las filas del triángulo.
    triangulo = []
    # Iteramos desde 0 hasta n.
    for aux in range(n+1):
        # Inicializamos una lista vacía para almacenar los números de la fila actual.
        fila = []
        # Iteramos desde 0 hasta aux.
        for k in range(0, aux + 1):
            # Calculamos el coeficiente binomial (aux choose k)
            # utilizando la fórmula del coeficiente binomial y la función factorial de la biblioteca math.
            # Añadimos el coeficiente binomial a la fila actual.
            fila.append(math.comb(n, k))
        # Añadimos la fila al triángulo.
        triangulo.append(fila)
    # Devolvemos el triángulo completo.
    return triangulo


# Esta función imprime el Triángulo de Pascal.
def imprimir_triangulo_pascal(triangulo):
    # Iteramos sobre cada fila en el triángulo.
    for i in range(len(triangulo)):
        # Imprime espacios en blanco para alinear correctamente los números.
        print(" " * (len(triangulo) - i), end="")
        # Itera sobre el rango de números en la fila actual.
        for j in range(i + 1):
            # Imprime el número actual seguido de un espacio.
            print(triangulo[i][j], end=" ")
        # Imprime un salto de línea después de cada fila.
        print()


# Este es el punto de entrada principal del programa.
if __name__ == '__main__':
    # Solicitamos al usuario que ingrese el número de filas que desea en el Triángulo de Pascal.
    # Generamos el Triángulo de Pascal con el número especificado de filas.
    # Imprimimos el Triángulo de Pascal.
    imprimir_triangulo_pascal(calcular_numero_binomial(n=int(input("Ingrese limite!"))))
