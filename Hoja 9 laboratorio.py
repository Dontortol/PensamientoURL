Ejercicio 1
INICIO
def es_par_o_impar (n):
    if n % 2 == 0:
        print("es par")
    else:
        print("es impar")
es_par_o_impar (4)
FIN

Ejercicio 2
INICIO
def suma_lista(lista):
    return sum(lista)

numeros = [1,2,3]  
resultado = suma_lista(numeros)  
print("la suma de", numeros, "es: ",resultado)
FIN

Ejercicio 3
INICIO
def cuenta_regresiva(n):
    if n < 0:
        print("¡Dedspegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)
cuenta_regresiva(5)
FIN

Ejercicio 4
INICIO
def cuenta_ascendente(n, inicia=1):
    if inicia > n:
        return
    print(inicia)
    cuenta_ascendente(n, inicia + 1)
cuenta_ascendente(4)
FIN

Ejercicio 5
INICIO
def suma_hasta(n):
    return sum(range(1, n + 1))

resultado = suma_hasta(4)
print(resultado)  
FIN

Ejercicio 6
INICIO
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

resultado = factorial(5)
print(resultado)  
FIN

Ejercicio 7
INICIO
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    menor = minimo(lista[1:])  
    return lista[0] if lista[0] < menor else menor

resultado = minimo([5, 3, 8, 1, 2])
print(resultado) 
FIN

Juego 
INICIO
import time
import random

def adivina_el_numero(numero_secreto, intentos, tiempo_inicio):
    if intentos == 0:
        print("¡Te has quedado sin intentos! El número era", numero_secreto)
        return
    
    try:
        numero_usuario = int(input(f"Tienes {intentos} intentos restantes. Ingresa un número: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)
        return
    
    if numero_usuario == numero_secreto:
        tiempo_final = time.time()
        tiempo_total = round(tiempo_final - tiempo_inicio, 2)
        print(f"🎉 ¡Felicidades! Adivinaste el número {numero_secreto} en {tiempo_total} segundos.")
    elif numero_usuario < numero_secreto:
        print("El número es mayor.")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)
    else:
        print("El número es menor.")
        adivina_el_numero(numero_secreto, intentos - 1, tiempo_inicio)

numero_secreto = random.randint(1, 100) 
print("Bienvenido al juego de Adivina el Número.")
print("Elige un número entre 1 y 100.")
print("¡Buena suerte!")

tiempo_inicio = time.time() 
adivina_el_numero(numero_secreto, 5, tiempo_inicio)
FIN
