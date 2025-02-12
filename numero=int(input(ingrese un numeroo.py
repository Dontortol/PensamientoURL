numero=int(input("ingrese un numeroo entre 1-9: "))
resultado=""
if numero >=1 and numero <=9:
    if numero>=1 and numero<=3:
        resultado=numero*"I"
        print("El",numero,"en romano es:",resultado)
    elif numero ==4:
        resultado=numero
        print("El numero 4 en Romano es: IV")
    
    if numero>=5 and numero <=8:
        resultado= "V"+(numero-5)*"I"
        print("El",numero,"en romano es:",resultado)
    elif numero ==9:
        resultado=numero
        print("El numero 9 en romano es: IX")

else:
    print("numero no valido")