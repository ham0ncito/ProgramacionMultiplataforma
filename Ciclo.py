import math
numero =  int(input("Digite un numero entero positivo"))
while numero < 0 :
    print(f"Error el numero es negativo")
    numero =  int(input("Digite un numero entero positivo"))

print(f" La raiz cuadrada es : {math.sqrt(numero)}" )
