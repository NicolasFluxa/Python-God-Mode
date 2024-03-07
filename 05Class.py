
class vehiculo:

    def __init__(self, nombre, color):
        self.__nombre = nombre
        self.__color = color

    def getColor(self):
        return self.__color

    def getNombre(self):
        return self.__nombre

    def setColor(self, color):
        self.__color = color

    def setNombre(self, nombre):
        self.__nombre = nombre

# descripcion es por valor


class auto(vehiculo):
    def __init__(self, nombre, color, modelo):
        super().__init__(nombre, color)
        self.__modelo = modelo

    def getDescripcion(self):
        return self.getNombre() + self.__modelo + ' de color ' + self.getColor()


carro = auto("suzuki ", "Azul", "Celerio")

print(carro.getDescripcion())
print(carro.getNombre())
print(carro.getColor())
