# Aquí se define una clase llamada 'poligono'.
class poligono:
    # Este es el método constructor de la clase 'poligono'.
    # Se llama automáticamente cuando se crea un objeto de la clase 'poligono'.
    def __init__(self, lado):
        # Estas líneas crean dos atributos: 'n' que es el
        # número de lados del polígono, y 'lados' que es una lista de ceros de longitud 'n'.
        self.n = lado
        self.lados = [0 for i in range(lado)]

    # Este método permite al usuario ingresar la longitud de cada lado del polígono.
    def ingresarLados(self):
        self.lados = [float(input("Ingrese lado" + str(i+1) + ": ")) for i in range(self.n)]

    # Este método imprime la longitud de cada lado del polígono.
    def mostrarLados(self):
        for i in range(self.n):
            print("lado", i+1, "es ", self.lados[i])

# Aquí se define una clase llamada 'triangulo' que hereda de la clase 'poligono'.


class triangulo(poligono):
    # Este es el método constructor de la clase 'triangulo'.
    # Se llama automáticamente cuando se crea un objeto de la clase 'triangulo'.
    def __init__(self):
        # Esta línea llama al constructor de la clase padre 'poligono'
        # con 3 como argumento, indicando que un triángulo tiene 3 lados.
        poligono.__init__(self, 3)

    # Este método calcula y muestra el área del triángulo usando la fórmula de Herón.
    def area(self):
        a, b, c = self.lados
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))**0.5
        print("El area del triangulo es: %0.2f" % area)

# Estas líneas crean un objeto de la clase 'triangulo',
# permiten al usuario ingresar las longitudes de los lados,
# muestran las longitudes de los lados y calculan y muestran el área del triángulo.


t = triangulo()
t.ingresarLados()
t.mostrarLados()
t.area()
