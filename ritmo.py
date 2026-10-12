def registro_consumo():
    n_valores = int(input("Introduce el numero de lecturas de consumo que quieres registrar:"))
    lista = []
    for i in range (0, n_valores, 1):
        dato = int(input(f"Introduce la lectura numero {i+1} : "))
        lista.append(dato)
        print("lecturas guardadas:", lista)
        analisis(lista)
    return 0


def analisis(lista_recibida):
    print("\n<<< Analizando respuestas >>>")
    for dato in lista_recibida:
        if dato <= 5:
            print(f"Vas bien el consumo es bajo")
        elif 5 < dato < 15:
            print("Consumo moderado no esta mal pero vigila")
        elif 15 <= dato < 30:
            print("Consumo elevado revisar equipos en marcha")
        else:
            print("ALERTA!! sobrecarga LLAMEN A LOS BOMBEROS!!!")  
    return 0
registro_consumo()