class Animales:
    def __init__(self, nombre, edad, habitat, dieta, tamano, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__dieta = dieta
        self.__tamano = tamano
        self.__color = color

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_habitat(self):
        return self.__habitat

    def set_habitat(self, habitat):
        self.__habitat = habitat

    def get_dieta(self):
        return self.__dieta

    def set_dieta(self, dieta):
        self.__dieta = dieta

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, tamano):
        self.__tamano = tamano

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


    def moverse(self):
        return ("El animal se desplaza de un lugar a otro")

    def comunicacion(self):
        return ("El animal emite señales o sonidos para comunicarse con otros")

    def reproduccion(self):
        return ("El animal se reproduce para dar continuidad a su especie")

    def alimentarse(self):
        return ("El animal consume su alimento según su dieta")

    def adaptacion(self):
        return ("El animal se adapta a las condiciones de su entorno")

    def instintos(self):
        return ("El animal actúa guiado por sus instintos naturales")

    def descanso(self):
        return ("El animal descansa para recuperar energía")

    def sueno(self):
        return ("El animal duerme siguiendo su ciclo natural")

    def interaccion_social(self):
        return ("El animal interactúa con otros individuos de su entorno")
