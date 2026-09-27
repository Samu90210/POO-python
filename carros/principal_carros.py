from automovil import Automovil
from camion import Camion


def mostrar_info(vehiculo, nombre):
    print(f"===== {nombre} =====")
    print(f"Modelo: {vehiculo.get_modelo()}")
    print(f"Color: {vehiculo.get_color()}")
    print(vehiculo.arranque())
    print(vehiculo.aceleracion_y_frenado())
    print(vehiculo.sistema_direccion())
    print(vehiculo.climatizacion())
    print(vehiculo.tipo_seguridad())
    print(vehiculo.luces())
    print(vehiculo.sistema_ventanas())
    print(vehiculo.sistema_espejo())
    print(vehiculo.apagado())
    print()


def main():

    automovil = Automovil(
        "BMW Z4", "Negro", "V6 3.0L", 2, 2, "Gasolina", tipo_transmision="Automatica"
    )


    camion = Camion(
        "Freightliner M2", "Blanco", "Diesel 6 cilindros", 2, 3, "Diesel", capacidad_carga_toneladas=8
    )

    mostrar_info(automovil, "AUTOMOVIL")
    mostrar_info(camion, "CAMION")


if __name__ == "__main__":
    main()
