
print("\t Calculadora en Python \n 1. Suma \n 2. Resta \n 3. Division \n 4. Multiplicacion \n Opcion :")
opcion_elegida = int(input())

print("\n Elija los valores 1 y 2 ")
num1 =int(input())
num2 = int(input())
if opcion_elegida == 1:
    print("La suma total es de : ", num1 + num2)
elif opcion_elegida == 2:
    print("La resta total es de : ", num1 - num2)
elif opcion_elegida == 3:

    print("La division total es de:", int(num1/num2))
elif opcion_elegida == 4:

    print("La multiplicacion total es de:", int(num1 * num2))

#condicionales
while(True):
    numero1 = int(input("Ingrese un numero"))
    if numero1 >0:
        print("Numero es positivo")
    elif numero1  <0:
        print("Nunmero es negativo")
    else:
        print("Numero es 0")

while (True):
    numero_Ganador = "1010"
    edad_Ganador = 21
    numero_Boleto = str(input("\nIngrese su numero de boleto"))
    edad_Usuario = int(input("\nIngrese su edad"))

    if (numero_Boleto == numero_Ganador and edad_Usuario >= edad_Ganador):
        print(f"El numero ingresado {numero_Boleto} es el ganador y eres mayor de {edad_Ganador } \n\n\t Ganaste pero no su amor ;) ")
    elif (numero_Boleto == numero_Ganador and (edad_Ganador != edad_Usuario)):
        print(f"El numero ingresado {numero_Boleto} es el ganador, pero no tienes la edad suficiente de {edad_Ganador}",numero_Boleto, edad_Ganador )
    elif(edad_Usuario >= edad_Ganador and numero_Boleto != numero_Ganador):
        print(f"Eres mayor de edad : {edad_Ganador}, pero no tienes el numero de boleto ganador")
    else:
        print(f"Terrible no eres ganador, porque no tienes la edad de {edad_Ganador}, ni el boleto ganador {numero_Boleto}")


variable_a = int(input("Ingrese el valor a"))
if variable_a < 0:
    variable_a *= -1
variable_b = int(input("Ingrese el valor b"))
if variable_b < 0:
    variable_b *= -1
variable_c = int(input("Ingrese el valor c"))
if variable_c < 0:
    variable_c *= -1
deter = variable_b**2 - 2 * variable_a * variable_c
print("\n\t El resultado es ", (variable_a**3 * deter) / (2*variable_b))

#dec a bin
n = bin(-3)
print(n)

#dec a hexa
n = int("0xa",16)
print(n)

'''Ingrese numero entero, que sea positivo, que lo muestre en base decimal, binario, octal, hexadecimal'''

numero_ingresado = int(input("Ingrese un valor"))
if numero_ingresado <0:
    numero_ingresado *= -1
print(f"El numero ingresado {numero_ingresado} en decimal es: ", numero_ingresado)
print(f"El numero ingresado {numero_ingresado} en binario es: ", bin(numero_ingresado))
print(f"El numero ingresado {numero_ingresado} en octal es: ", oct(numero_ingresado))
print(f"El numero ingresado {numero_ingresado} en hexadecimal es: ", hex(numero_ingresado))
