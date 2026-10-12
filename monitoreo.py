def monitoreo_planta():
    sensores_planta = {}
    sensores_planta["presion_caldero"] = 6.8
    sensores_planta["presion_reductora"] = 4.2
    sensores_planta["presion_retorno"] = 1.5
    for sensor,valor in sensores_planta.items():
        print(f"El sensor '{sensor}' marca un valor de {valor} bar")
    return 0
monitoreo_planta()