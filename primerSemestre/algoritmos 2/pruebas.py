class Saludo:

    _nombre: str
    __apellido: str
    def __init__(self, nombre: str, apellido: str):
        self._nombre = nombre
        self.__apellido = apellido
        print('Me acaban de instanciar 🤘')

    def __del__(self):
        print('Este es mi fin')

    def saludar(self):
        print(f'Hola {self._nombre} {self.__apellido}')


saludo = Saludo('Alber', 'Ramírez')
print(saludo.__apellido)