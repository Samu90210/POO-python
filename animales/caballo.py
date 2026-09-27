from animal import Animales


class Caballo(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, corre_rapido=True):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.__corre_rapido = corre_rapido

    def get_corre_rapido(self):
        return self.__corre_rapido

    def set_corre_rapido(self, corre_rapido):
        self.__corre_rapido = corre_rapido

    def moverse(self):
        return ("Este animal corre a galope sobre sus cuatro patas por el pastizal")

    def adaptacion(self):
        return ("Está adaptado a la vida terrestre, con patas fuertes para correr largas distancias")
