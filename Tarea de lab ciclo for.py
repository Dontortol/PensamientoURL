Ejercicio 1 
INICIO
for i in range (1,11):
    if i % 2 !=0:
        print(i)
FIN

Ejercicio 2
INICIO
n =  1

while n < 11:
    if n % 2 !=0:
        print(n)
    n +=1
FIN

Escenario 1
INICIO
while True:
    pb = input("ingrese una palabra: ")
    if pb =="chupacabra":
        print("¡Has dejado el bucle con éxito")
        break
FIN
Escenario 2
INICIO
user_word = input("Ingrese una palabra: ").upper()

for i in user_word:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue 
    else:
        print(i)
FIN