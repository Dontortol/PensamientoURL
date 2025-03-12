consumo = int(input("ingrese su consumo en m cubicos: "))
habitantes = int(input("ingrese cantidad de habitantes: "))

if consumo < 15:
    consumo1 = consumo*5
    print(consumo1, "Quetzales")

if consumo >= 15 and consumo <= 30:
    if habitantes > 3:
        consumo2 = consumo*4
        print(consumo2, "Quetzales")
    elif habitantes == 3:
        consumo3 = consumo*4.5
        print(consumo3, "Quetzales")
    else:
        consumo4 = consumo*5
        print(consumo4, "Quetzales")

if consumo > 30:
    if habitantes > 5:
        consumo5 = consumo*3.5
        print(consumo5, "Quetzales")
    elif habitantes % 2 == 0:
        consumo6 = consumo*4
        print(consumo6, "Quetzales")
    else:
        consumo7 = consumo*4.2
        print(consumo7, "Quetzales")

Ejercicio 2
Inicio 
car = int(input("ingrese el año del carro: "))
placa = (input("ingrese la placa del carro: "))

if car >= 2001:
    if int(placa[len(placa)-1])%2 == 0:
        print("No cirula los lunes")
    elif int(placa[len(placa)-1])%2 != 0:
        print("No cirucla los viernes")
    if car % 2 == 0:
        print("No circula los sabados")
else:
    print("Mantenimiento obligatorio")
    
    