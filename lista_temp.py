def temperatura2():
    n_valores = int(input("Introduce el numero de temperaturas que quieres analizar:"))
    temperaturas = []
    for i in range (0, n_valores, 1):
        temp = int(input(f"Introduce la temperatura {i+1}: "))
        temperaturas.append(temp)
    print("temperaturas guardadas:", temperaturas)
    analisis(temperaturas)
    return 0


def analisis(lista_recibida):
    print("\n--- Analizando resultados ---")
    for temp in lista_recibida:
        if temp <= 10:
            print(f"Temperatura {temp}ºC: Pega rasca abrigate")
        elif 10 < temp <= 25:
            print(f"Temperatura {temp}ºC: Buena temperatura")
        elif 25 < temp < 35:
            print(f"Temperatura {temp}ºC: Hace calor vigila las condiciones climaticas")
        else:
            print(f"Temperatura {temp}ºC: Alarma de incendio LLAMAR A LOS BOMBEROS")
    return 0

temperatura2()
        

    