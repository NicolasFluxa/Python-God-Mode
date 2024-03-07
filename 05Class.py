# Aquí se define una clase llamada 'vehiculo'.
class vehiculo:
    # Este es el método constructor de la clase 'vehiculo'.
    # Se llama automáticamente cuando se crea un objeto de la clase 'vehiculo'.
    def __init__(self, nombre, color):
        # Estas líneas crean dos atributos privados '__nombre' y
        # '__color' y les asignan los valores pasados como argumentos al constructor.
        self.__nombre = nombre
        self.__color = color

    # Estos son los métodos get para los atributos '__color' y
    # '__nombre'. Devuelven el valor de los respectivos atributos.
    def getColor(self):
        return self.__color

    def getNombre(self):
        return self.__nombre

    # Estos son los métodos set para los atributos '__color' y
    # '__nombre'. Modifican el valor de los respectivos atributos.
    def setColor(self, color):
        self.__color = color

    def setNombre(self, nombre):
        self.__nombre = nombre

# Aquí se define una clase llamada 'auto' que hereda de la clase 'vehiculo'.
class auto(vehiculo):
    # Este es el método constructor de la clase 'auto'.
    # Se llama automáticamente cuando se crea un objeto de la clase 'auto'.
    def __init__(self, nombre, color, modelo):
        # Esta línea llama al constructor de la clase padre 'vehiculo'
        # para inicializar los atributos heredados.
        super().__init__(nombre, color)
        # Esta línea crea un nuevo atributo privado '__modelo' y
        # le asigna el valor pasado como argumento al constructor.
        self.__modelo = modelo

    # Este es un método que devuelve una descripción del auto en forma de cadena.
    def getDescripcion(self):
        return self.getNombre() + self.__modelo + ' de color ' + self.getColor()

# Estas líneas crean un objeto de la clase 'auto',
# llaman a sus métodos y luego imprimen los resultados.
carro = auto("suzuki ", "Azul", "Celerio")
print(carro.getDescripcion())
print(carro.getNombre())
print(carro.getColor())
