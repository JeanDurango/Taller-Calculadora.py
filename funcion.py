import math
def Sumar():
    print("Ingresa el primer digito a Sumar: ")
    n1 = float(input())
    print("Ingresa el segundo  digito a Sumar: ")
    n2 = float(input())
    print("El resultado es: ", n1 + n2)

def Restar():
    print("Ingresa el primer digito a Restar: ")
    n1 = float(input())
    print("Ingresa el segundo  digito a Restar: ")
    n2 = float(input())
    print("El resultado es: ", n1 - n2)

def Multiplicar():
    print("Ingresa el primer digito a Multiplicar: ")
    n1 = float(input())
    print("Ingresael segundo  digito a Multiplicar: " )
    n2 = float(input())
    print("El resultado es: ", n1 * n2)

def Dividir():
    print("Ingresa el dividendo: ")
    n1 = float(input())
    print("Ingresa el divisor: ")
    n2 = float(input())
    print("El resultado es: ", n1 / n2)

def Potencia():
    print("Ingresa la base: ")
    n1 = float(input())
    print("Ingrese el exponente: ")
    n2 = float(input())
    print("El resultado es: ",n1 ** n2)

def Raiz():
    print("Ingresa el radicando: ")
    n1 = float(input())
    print("Ingresa el indice: ")
    n2 = float(input())
    print("El resultado es: ", n1 ** (1/n2) )

def Seno():
    print("ingres su numero para calcular el Seno")
    n1 = float(input())
    p = math.radians(n1)
    print("El resultado es: ", math.sin(p))

def Coseno():
    print("ingres su numero  para calcular el Coseno")
    n1 = float(input())
    p = math.radians(n1)
    print("El resultado es: ", math.cos(p))

def Tangente():
    print("ingres su numero para calcular la Tangente")
    n1 = float(input())
    p = math.radians(n1)
    print("El resultado es: ", math.tan(p))   

def Generar_numeros_pares():
    print("PARES E IMPARES")
    n1 = int(input("Escriba un número entero: "))    
    for i in range(n1):
        if i % 2 == 0:
            print(f"El número {i} es par.")
        
    