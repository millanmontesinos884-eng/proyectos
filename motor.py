def motor():
    temperaturas_equipos = {}
    temperaturas_equipos["Bomba_1"] = 45.2
    temperaturas_equipos["Motor_2"] = 68
    temperaturas_equipos["Compresor"] = 32.5

    print("Diccionario completo", temperaturas_equipos)

    print(f"La temperatura de la Bomba_1 es {temperaturas_equipos['Bomba_1']} ºC ")
    print(f"La temperatura del motor_2 es {temperaturas_equipos['Motor_2']} ºC")
    print(f"La temperatura del Compresor es {temperaturas_equipos['Compresor']} ºC")
    return 0
motor()