def monitoreo_dinamico():
    monitoreo_dinamic = {}
    monitoreo_dinamic  ["Compresor"] = (6.8, 56.3)
    monitoreo_dinamic  ["Motor 1"] = (6.2, 73.8)
    monitoreo_dinamic  ["Motor 2"] = (6.0, 40.3)
    monitoreo_dinamic  ["Bomba 1"] = (5.9, 48.3) 
    monitoreo_dinamic  ["Bomba 2"] = (4.3, 45.1)
    for equipo, (presion, temperatura) in monitoreo_dinamic.items():
        print(f"Equipo: {equipo} | Presion: {presion} bar | Temperatura : {temperatura}º")
monitoreo_dinamico()

