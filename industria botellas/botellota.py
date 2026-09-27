from botella import botellas


class Botellota(botellas):
    def __init__(self, capacidad, material, forma, design, tapa, grabados, requiere_dos_manos=True):
        super().__init__(capacidad, material, forma, design, tapa, grabados)
        self.__requiere_dos_manos = requiere_dos_manos

    def get_requiere_dos_manos(self):
        return self.__requiere_dos_manos

    def set_requiere_dos_manos(self, requiere_dos_manos):
        self.__requiere_dos_manos = requiere_dos_manos

    def transporte(self):
        return ("Esta botella es tan grande que necesitas las dos manos para cargarla")

    def compatibilidad(self):
        return ("Perfecta para fiestas, reuniones familiares o para llenar el minibar del gamer")
