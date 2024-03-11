
import math # Importamos la biblioteca math para usar la función factorial.


def calcular_numero_binomial(n):  # Esta función genera el Triángulo de Pascal hasta la fila n.
    # Inicializamos una lista vacía para almacenar las filas del triángulo.
    triangulo = []
    # Iteramos desde 0 hasta n.
    for aux in range(n+1):
        # Inicializamos una lista vacía para almacenar los números de la fila actual.
        fila = []
        # Iteramos desde 0 hasta aux.
        for k in range(0, aux + 1):
            # Se Puede hacer mas eficiente con math.comb(n, k)
            # Calculamos el coeficiente binomial (aux choose k)
            # utilizando la fórmula del coeficiente binomial y la función factorial de la biblioteca math.
            # Añadimos el coeficiente binomial a la fila actual.
            fila.append(int(math.factorial(aux) / (math.factorial(k) * math.factorial(aux - k))))
        # Añadimos la fila al triángulo.
        triangulo.append(fila)
    # Devolvemos el triángulo completo.
    return triangulo


# Esta función imprime el Triángulo de Pascal.
def imprimir_triangulo_pascal(triangulo):
    # Iteramos sobre cada fila en el triángulo.
    for i in triangulo:
        # Imprimimos la fila.
        print(i)


# Este es el punto de entrada principal del programa.
if __name__ == '__main__':
    # Solicitamos al usuario que ingrese el número de filas que desea en el Triángulo de Pascal.
    # Generamos el Triángulo de Pascal con el número especificado de filas.
    # Imprimimos el Triángulo de Pascal.
    imprimir_triangulo_pascal(calcular_numero_binomial(n=int(input("Ingrese limite!"))))
