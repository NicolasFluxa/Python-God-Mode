# Aquí se define una clase llamada 'a'.
class a:
    # Este es el método constructor de la clase 'a'.
    # Se llama automáticamente cuando se crea un objeto de la clase 'a'.
    def __init__(self):
        # Esta línea crea un atributo privado llamado '__x' y
        # le asigna el valor 1.
        self.__x = 1

    # Aquí se define un método llamado 'minumero' para la clase 'a'.
    # Cuando se llama a este método, imprime la cadena "mifuncionA".
    def minumero(self):
        print("mifuncionA")

# Aquí se define una clase llamada 'b' que hereda de la clase 'a'.
class b(a):
    # Este es el método constructor de la clase 'b'. Se llama automáticamente
    # cuando se crea un objeto de la clase 'b'.
    def __init__(self):
        # Esta línea crea un atributo privado llamado '__y' y le asigna el valor 1.
        self.__y = 1

    # Aquí se define un método llamado 'minumero' para la clase 'b'.
    # Cuando se llama a este método, imprime la cadena "mifuncionB".
    def minumero(self):
        print("mifuncionB")

# Esta línea crea un objeto de la clase 'a' y lo almacena en la variable 'c'.
c = a()
# Esta línea llama al método 'minumero' del objeto 'c'. Como 'c'
# es un objeto de la clase 'a', esto imprime "mifuncionA".
c.minumero()

# Esta línea crea un objeto de la clase 'b' y lo almacena en la variable 'c'.
c = b()
# Esta línea llama al método 'minumero' del objeto 'c'. Como 'c'
# es un objeto de la clase 'b', esto imprime "mifuncionB".
c.minumero()
