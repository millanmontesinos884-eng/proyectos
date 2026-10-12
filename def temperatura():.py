def temperatura():
    valor = input("Introduce la temperatura")
    temperatura = int (valor)
    if temperatura < 10:
        print("Hace bastante frio")
    elif 10 < temperatura <= 25:
        print("Temperatura optima")
    elif 25 < temperatura <= 35:
        print("Temperatura elevada Precaucion")
    else:
        printf("Alerta! Temperatura crica LLAMEN A LOS BOMBEROS")