class poligono:
    def __init__(self, lado):
        self.n = lado
        self.lados = [0 for i in range(lado)]

    def ingresarLados(self):
        self.lados =[float(input("Ingrese lado" + str (i+1) + ": ")) for i in range(self.n)]

    def mostrarLados(self):
        for i in range(self.n):
            print("lado", i+1, "es ", self.lados[i])


class triangulo(poligono):
    def __init__(self):
        poligono.__init__(self, 3)

    def area(self):
        a, b, c = self.lados
        s = (a + b + c) / 2
        are = (s * (s - a) * (s - b) * (s - c))**0.5
        print("El area del triangulo es: %0.2f" %are)


t = triangulo()
t.ingresarLados()
t.mostrarLados()
t.area()
