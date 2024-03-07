

class a:
    def __init__(self):
        self.__x = 1

    def minumero(self):
        print("mifuncionA")


class b(a):
    def __init__(self):
        self.__y = 1

    def minumero(self):
        print("mifuncionB")


c = a()
c.minumero()

c = b()
c.minumero()
