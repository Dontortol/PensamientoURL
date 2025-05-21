matriz= [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(matriz):
    for i in matriz:
        print(i)

def siguiente_generacion(matriz):
    n = []
    for i in range(len(matriz)):
        n.append([])
        for j in range(len(matriz[i])):
            #supervivencia
            if 0 < j < len(matriz[i])-1:
                if (matriz[i][j-1] or matriz[i][j+1]) and matriz[i][j] == 1:
                    n[i].append(1)
                elif(matriz[i][j-1] or matriz[i][j+1]) and matriz[i][j] == 0:
                    n[i].append(1)
                else:
                    n[i].append(0)
            else: 
                n[i].append(matriz[i][j])
            
            #sobrepoblacion    
            if  1 <= j <= len(matriz[i])-2:
                if matriz[i][j] == 1 and (matriz[i][j+1] == 1 and matriz[i][j+2] == 1):
                    n[i][j] = 0
                else:
                    n[i][j]
            
            #revivir
            
                
    return n

print("Generación 0:")
imprimir_tablero(matriz)
generacion_1 = siguiente_generacion(matriz)
print("Generación 1:")
imprimir_tablero(generacion_1)
generacion_2 = siguiente_generacion(generacion_1)
print("Generación 2:")
imprimir_tablero(generacion_2)