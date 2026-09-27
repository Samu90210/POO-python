from caballo import Caballo
from pez import Pez


def mostrar_info(animal, nombre):
    print(f"===== {nombre} =====")
    print(animal.moverse())
    print(animal.comunicacion())
    print(animal.reproduccion())
    print(animal.alimentarse())
    print(animal.adaptacion())
    print(animal.instintos())
    print(animal.descanso())
    print(animal.sueno())
    print(animal.interaccion_social())
    print()


def main():
    caballo = Caballo(
        "CABALLO", "5 AÑOS", "PRADERA", "HERBIVORA", "GRANDE", "MARRON"
    )

    pez = Pez(
        "PEZ DISCO", "1 AÑO", "ACUARIO", "OMNIVORA", "PEQUENO", "AZUL Y NARANJA"
    )

    mostrar_info(caballo, "CABALLO")
    mostrar_info(pez, "PEZ")


if __name__ == "__main__":
    main()
