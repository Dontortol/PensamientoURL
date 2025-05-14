dias = ["-Lunes-","-Martes-","-Miércoles-","-Jueves-","-Viernes-"]

niveles_azucar = [130,160,95,175,160]
niveles_sal = [2000, 2400, 1800, 2400, 2700]
presion = [115,130,110,125,175]

contador = 0
while contador < 5:
    print(f"{dias[contador]}")
    print(f">azucar: {niveles_azucar[contador]} mg/dl")
    if niveles_azucar[contador] > 70 and niveles_azucar[contador] < 140:
        print("dentro del rango saludable")
    else:
        print("fuera del rango saludable")
    print()
    print(f">sal: {niveles_sal[contador]} mg/dia")
    if niveles_sal[contador] > 2300:
        print("dentro del rango saludable ")
    else:
        print("fuera del rango saludable")
    print()
    print(f">presion: {presion[contador]}mmHg")
    if presion[contador] < 120:
        print("dentro del rango normal")
    elif presion[contador] > 120 and presion[contador] < 129:
        print("presion elevada")
    elif presion[contador] >= 130 and presion[contador] < 139:
        print("hipertension")
    else:
        print("hiértension etapa 2")
    
    contador+=1