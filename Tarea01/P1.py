size = 5


def cuadro():
    for i in range(size):
        for j in range(size - i - 1):
            print('', end=' ')
        for k in range(i + 1):
            print('*', end=' ')
        print()


def matriz_cuadrada():
    matriz = []
    for _ in range(size):
        matriz.append([0]*size)
    return matriz


def mostrar(matriz):
    for i in matriz:
        print(i)


if __name__ == '__main__':
    cuadro()
    mostrar(matriz_cuadrada())

