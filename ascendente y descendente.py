n=int(input("Ingrese un numero de 5 digitos: "))
resultado=""
resultados=""

n1 =  n//10000
n2 = (n%10000)//1000
n3 = (n%1000)//100
n4 = (n%100)//10
n5 = (n%10)

if n1 >= n2 >= n3 >= n4 >= n5:
    resultado = n1,n2,n3,n4,n5
    print(resultado)

if n2 > n3 > n4 > n5 > n1:
    resultado = n2,n3,n4,n5,n1
    print(resultado)
    
if n3 > n4 > n5 > n2 > n1:
    resultado = n3,n4,n5,n2,n1
    print(resultado)
    
if n4 > n5 > n3 > n2 > n1:
    resultado = n4,n5,n3,n2,n1
    print(resultado)

if n5 > n4 > n3 > n2 > n1:
    resultado = n5,n4,n3,n2,n1
    print(resultado)
    
if n1 < n2 < n3 > n4 > n5:
    resultados=n1,n2,n5,n4,n3
    print (resultados )
    
if n5 < n4 < n3 < n2 <n1:
    resultados=n5,n4,n3,n2,n1
    print (resultados )
    
if n4 < n3 < n2 < n1 <n5:
    resultados=n4,n3,n2,n1,n5
    print (resultados )

if n3 < n2 < n1 < n5 <n4:
    resultados=n3,n2,n1,n5,n4
    print (resultados )

if n2 < n1 < n3 < n4 <n5:
    resultados=n2,n1,n3,n4,n5
    print (resultados )
    
if n1 < n2 < n3 < n4 > n5:
    resultados=n1,n2,n3,n5,n4
    print (resultados )

if n1 < n2 < n3 < n4 < n5:
    resultados=n1,n2,n3,n4,n5
    print (resultados )


    
