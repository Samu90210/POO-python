class botellas:
    def __init__(self, capacidad, material, forma, design, tapa, grabados):
        self.__material = material
        self.__capacidad = capacidad
        self.__forma = forma
        self.__design = design
        self.__tapa = tapa
        self.__grabados = grabados

    def get_capacidad(self):
        return self.__capacidad

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material

    def get_forma(self):
        return self.__forma

    def set_forma(self, forma):
        self.__forma = forma

    def get_design(self):
        return self.__design

    def set_design(self, design):
        self.__design = design

    def get_tapa(self):
        return self.__tapa

    def set_tapa(self, tapa):
        self.__tapa = tapa

    def get_grabados(self):
        return self.__grabados

    def set_grabados(self, grabados):
        self.__grabados = grabados

    
    def contencion(self):
        return("El liquido ta adentro de la bottle bro, todo good")

    def servir(self):
        return ("El liquido ha sido serivido de la botella a un vaso")
    
    def cierre_hermetico(self):
        return ("El liquido está protegido del exterior exitosamente")
    
    def transporte(self):
        return ("Estás llevando la botella en la mano")

    def manejo(self):
        return ("Puedes abrir o cerrar la botella")
    
    def compatibilidad(self):
        return ("Esta botella es preferencialmente de uso para liquidos a temperatura ambiente - fría")
    
    def reutilizacion(self):
        return ("Deja esta botella en un depósito de reciclaje o guardala y vuelve a usarla para contener otro liquido")
    
    def transparencia(self):
        return ("puedes ver el contenido de la botella sin destaparla")


