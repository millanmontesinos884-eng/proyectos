def bateria():
    n = int(input("introduce el numero de equipos a analizar"))
    niveles = []
    for i in range(0, n, 1):
        valor = float(input(f"Introduce el valor de la bateria numero {i+1}: "))
        niveles.append(valor)
    print("Los valores introducidos son:" , niveles)
    analisis(niveles)
    return 0


def analisis(lista_recibida):
    print("<<< Analisis de los niveles de bateria >>>")
    for valor in lista_recibida:
        if valor <= 20:
            print(f"Bateria critica conectar inmediatemente!! El nivel de la bateria es {valor} % ")
        elif 20 < valor <60:
            print(f"Bateria media nivel aceptable El nivel de la bateria es {valor} % ")
        else:
            print(f"Bateria cargada, vas bien El nivel de la bateria es {valor} % ")
    return 0
bateria()
