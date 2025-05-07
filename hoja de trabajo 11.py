ejercicio 1
INICIO
import math
from abc import ABC, abstractmethod

class Experimento_fisico:
    @abstractmethod
    def calculca_tiempo():
        pass
    
class caida_libre(Experimento_fisico):
    def __int__(self, altura, gravedad = 9.81):
        self.altura = altura
        self.gravedad = gravedad
        
    def calcuar_tiempo(self):
        try:
            return math.sqrt(2*self.altura/self.gravedad)
        except:
            print("no se permiten negativos o 0")
        
  caida = caida_libre(10)
  print(caida.calculcar_tiempo())
    
FIN

Ejercico 2
INICIO
import math
from abc import ABC, abstractmethod

class OperacionCientifica:
    @abstractmethod
    def calcular():
        pass

class RaizCuadrada:
    def __int__(self, n):
        self.n = n
    
    def calcular(self):
        try:
            return self.n**(1/2)
        except:
            print("no se puede raiz negativa")
        
class Potencia:
    def __int__(self, n, expo):
        self.n = n
        self.expo = expo
    
    def calcular(self):
        return self.n**self.expo
        
class Logaritmo:
    def __int__(self, n, base):
        self.n = n
        self.base = base
    
    def calcular(self):
        try:
            return math.log(self.n, self.base)
        except:
            print("no se puee menor o igual a 0")
            
class Logaritmo:
    def __int__(self, n):
        self.n = n
    
    def calcular(self):
        try:
            fac = 1
            for i in range (1,self.n+1):
                fac*=i
            return fac
        except:
            return "no se puede un numero negativo o decimal"
FIN
3