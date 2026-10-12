def vueltas():
    n = int(input("Introduce el numero de vueltas que quieres registrar:"))
    tiempos = []
    for i in range (0, n, 1):
        t = float (input(f"(Introduce el tiempo numero {i+1}: "))
        tiempos.append(t)
        print("Los tiempos registrados son:", tiempos)
        analisis(tiempos)
    return 0

def analisis(lista_recibida):
    print("\n<<< ANALISIS DE LAS VUELTAS >>>")
    for t in lista_recibida:
        if t < 60:
            print(f"Vuelta rapida estas volando {t} segundos :")
        elif 60 < t < 80:
            print(f"Buen ritmo vuelta solida {t} segundos:")
        else:
            print(f"Vuelta lenta ERES UN TROLEBUS!!! {t} segundos")
    return 0
vueltas()
