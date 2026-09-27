from botella import botellas


class Botellita(botellas):
    def __init__(self, capacidad, material, forma, design, tapa, grabados, apta_bolsillo=True):
        super().__init__(capacidad, material, forma, design, tapa, grabados)
        self.__apta_bolsillo = apta_bolsillo

    def get_apta_bolsillo(self):
        return self.__apta_bolsillo

    def set_apta_bolsillo(self, apta_bolsillo):
        self.__apta_bolsillo = apta_bolsillo

    def transporte(self):
        return ("Esta botella es tan pequena que cabe perfecto en tu bolsillo o cartera")

    def compatibilidad(self):
        return ("Ideal para llevar contigo al gimnasio, la universidad o el trabajo")
