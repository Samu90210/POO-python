from vehiculo import Vehiculo


class Automovil(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros,
                 tipo_combustible, tipo_transmision="Automatica"):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.__tipo_transmision = tipo_transmision

    def get_tipo_transmision(self):
        return self.__tipo_transmision

    def set_tipo_transmision(self, tipo_transmision):
        self.__tipo_transmision = tipo_transmision

    def aceleracion_y_frenado(self):
        return ("El automovil acelera rapido gracias a su motor deportivo")

    def sistema_direccion(self):
        return ("La direccion es asistida y muy precisa a alta velocidad")
