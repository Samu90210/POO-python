from botellita import Botellita
from botellota import Botellota


def mostrar_info(botella, nombre):
    print(f"===== {nombre} =====")
    print(botella.contencion())
    print(botella.servir())
    print(botella.cierre_hermetico())
    print(botella.transporte())
    print(botella.manejo())
    print(botella.compatibilidad())
    print(botella.reutilizacion())
    print(botella.transparencia())
    print()


def main():
    botellita = Botellita(
        "500 ML", "PLASTICO", "CILINDRICA", "MINIMALISTA", "TAPA ROSCA", "LOGO PEQUENO"
    )
    
    botellota = Botellota(
        "3050 LITROS", "VIDRIO", "PRISMATICA", "RTX 3050", "TAPA EN FORMA DE HDMI", "LOGO DE NVIDIA"
    )

    mostrar_info(botellita, "BOTELLITA")
    mostrar_info(botellota, "BOTELLOTA")


if __name__ == "__main__":
    main()
