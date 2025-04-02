Ejercicio 1
Inicio
n = int(input("tamaño array: "))
m = int(input("multiplos: "))
salida =[] 
for i in range (0,n):
    salida.append (i*m)
print( salida) 

Fin

Ejercicio 2
Inicio
tam = int(input("Ingrese la cantidad de nombres: "))
nom = []
largo = []
for i in range (tam):
    nom.append(input("Ingrese un nombre: "))
for i in nom:
    largo.append(len(i))

print(nom)
print(largo)

Fin

escenario 1 
Inicio
cant = int(input("Ingrese la cantidad de personas que calificaron: "))

print("pon tu calificación \n"
"5. excelente \n"
"4. Muy Buena \n"
"3. Buena \n"
"2. Regular \n"
"1. Malo")

nota = []
cliente = []

for i in range(cant):
    notas = int(input("coloque su calificacion: "))
    nota.append(notas) 
    
print (f"Excelente:{nota.count(5)}")   
print (f"Muy Buena:{nota.count(4)}")
print (f"Buena:{nota.count(3)}")
print (f"Regular:{nota.count(2)}")
print (f"Malo:{nota.count(1)}")
Fin