from vehiculo import Vehiculo


class Camion(Vehiculo):
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros,
                 tipo_combustible, capacidad_carga_toneladas=5):
        super().__init__(modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible)
        self.__capacidad_carga_toneladas = capacidad_carga_toneladas

    def get_capacidad_carga_toneladas(self):
        return self.__capacidad_carga_toneladas

    def set_capacidad_carga_toneladas(self, capacidad_carga_toneladas):
        self.__capacidad_carga_toneladas = capacidad_carga_toneladas

    def aceleracion_y_frenado(self):
        return ("El camion acelera lento debido al peso, pero frena con sistema reforzado")

    def sistema_direccion(self):
        return ("La direccion requiere mas esfuerzo por el tamano y peso del camion")
