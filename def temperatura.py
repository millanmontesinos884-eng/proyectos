def temperatura2():
    n_valores = int(input("Introduce el numero de temperaturas que quieres analizar:"))
    temperaturas = []
    for i in range (0, n_valores, 1):
        temp = int(input("Introduce la temperatura {i+1}:"))
        temperaturas.append(temp)
    print("temperaturas guardadas:", temperaturas)
    return 0
temperatura2()
        

    