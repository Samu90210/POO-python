class Vehiculo:
    def __init__(self, modelo, color, motor, numero_puertas, capacidad_pasajeros, tipo_combustible):
        self.__modelo = modelo
        self.__color = color
        self.__motor = motor
        self.__numero_puertas = numero_puertas
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__tipo_combustible = tipo_combustible

   
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_motor(self):
        return self.__motor

    def set_motor(self, motor):
        self.__motor = motor

    def get_numero_puertas(self):
        return self.__numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self.__numero_puertas = numero_puertas

    def get_capacidad_pasajeros(self):
        return self.__capacidad_pasajeros

    def set_capacidad_pasajeros(self, capacidad_pasajeros):
        self.__capacidad_pasajeros = capacidad_pasajeros

    def get_tipo_combustible(self):
        return self.__tipo_combustible

    def set_tipo_combustible(self, tipo_combustible):
        self.__tipo_combustible = tipo_combustible


    def arranque(self):
        return ("El vehiculo ha encendido su motor correctamente")

    def apagado(self):
        return ("El vehiculo ha apagado su motor")

    def aceleracion_y_frenado(self):
        return ("El vehiculo acelera y frena de manera segura")

    def sistema_direccion(self):
        return ("El volante responde correctamente a los giros")

    def climatizacion(self):
        return ("El aire acondicionado o la calefaccion estan funcionando")

    def tipo_seguridad(self):
        return ("Cuenta con cinturones de seguridad y airbags")

    def luces(self):
        return ("Las luces delanteras y traseras encienden correctamente")

    def sistema_ventanas(self):
        return ("Las ventanas suben y bajan sin problema")

    def sistema_espejo(self):
        return ("Los espejos permiten ver el entorno del vehiculo")
