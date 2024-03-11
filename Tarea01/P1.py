# Esta función calcula el coeficiente binomial (n choose k) utilizando recursión.
def calcular_numero_binomial(n, k):
    # Si k es 0 o igual a n, el coeficiente binomial es 1.
    if k == 0 or k == n:
        return 1
    # De lo contrario, el coeficiente binomial se calcula
    # como la suma de dos coeficientes binomiales de la fila anterior.
    else:
        return calcular_numero_binomial(n-1, k-1) + calcular_numero_binomial(n-1, k)


# Esta función genera el Triángulo de Pascal con el número especificado de filas.
def generar_triangulo_pascal(filas):
    # Inicializa una lista vacía para almacenar las filas del triángulo.
    triangulo = []
    # Itera sobre el rango de filas.
    for i in range(filas+1):
        # Inicializa una lista vacía para almacenar los números de la fila actual.
        fila = []
        # Itera sobre el rango de números en la fila actual.
        for j in range(i+1):
            # Calcula el coeficiente binomial para el número actual y lo añade a la fila.
            fila.append(calcular_numero_binomial(i, j))
        # Añade la fila al triángulo.
        triangulo.append(fila)
    # Devuelve el triángulo completo.
    return triangulo


# Esta función imprime el Triángulo de Pascal de manera legible.
def imprimir_triangulo_pascal(triangulo):
    # Itera sobre el rango de filas en el triángulo.
    for i in range(len(triangulo)):
        # Imprime espacios en blanco para alinear correctamente los números.
        print(" " * (len(triangulo) - i), end="")
        # Itera sobre el rango de números en la fila actual.
        for j in range(i+1):
            # Imprime el número actual seguido de un espacio.
            print(triangulo[i][j], end=" ")
        # Imprime un salto de línea después de cada fila.
        print()


# Este es el punto de entrada principal del programa.
if __name__ == '__main__':
    # Solicita al usuario que ingrese el número de filas.
    filas = int(input("Ingrese el número de filas: "))
    # Genera el Triángulo de Pascal con el número especificado de filas.
    triangulo = generar_triangulo_pascal(filas)
    # Imprime el Triángulo de Pascal.
    imprimir_triangulo_pascal(triangulo)
