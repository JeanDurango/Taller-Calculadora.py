
import sys #se hace la importacion de la libreria sys para salir del programa
import funcion # se importan las fuuncioness
n1 = 0
n2 = 0

menu = """
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Potencia
6.- Raiz
7.- Seno
8.- Coseno
9.- Tangente
10.- Numeros pares
0.- Salir
"""


print("Bienvenido, A la  Calculadora...")
print("Selecione que opercion quiere realizar...")
while True:
    print(menu)
    opc = int(input())
    if opc == 1:
        funcion.Sumar()
    elif opc == 2:
        funcion.Restar()
    elif opc == 3:
        funcion.Multiplicar()
    elif opc == 4:
        funcion.Dividir()
    elif opc == 5:
        funcion.Potencia()
    elif opc == 6:
        funcion.Raiz()
    elif opc == 7:
        funcion.Seno()
    elif opc == 8:
        funcion.Coseno()
    elif opc == 9:
        funcion.Tangente()
    elif opc == 10:
        funcion.Generar_numeros_pares()
    elif opc == 0:
        sys.exit()