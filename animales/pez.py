from animal import Animales


class Pez(Animales):
    def __init__(self, nombre, edad, habitat, dieta, tamano, color, respira_branquias=True):
        super().__init__(nombre, edad, habitat, dieta, tamano, color)
        self.__respira_branquias = respira_branquias

    def get_respira_branquias(self):
        return self.__respira_branquias

    def set_respira_branquias(self, respira_branquias):
        self.__respira_branquias = respira_branquias

    def moverse(self):
        return ("Este animal nada moviendo sus aletas y su cuerpo bajo el agua")

    def adaptacion(self):
        return ("Está adaptado a la vida acuática, respira mediante branquias y tiene aletas para nadar")
