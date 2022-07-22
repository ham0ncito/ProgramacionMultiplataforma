'''
Realizar un programa en donde se le solicite al usuario ingresar 10 números enteros, y
muestre el orden ascendente y descendente, la suma de total de todos los números
ingresados. (20%)
'''
x = 1
numeros = []
while x <= 10:
    llenar = int(input(f"\n\t {x}. Ingrese un valor  "))
    numeros.append(llenar)
    x+=1;
    continue
print(numeros)
numeros.sort()
print("Los numeros ordenados de menor a mayor son los siguientes", numeros)
numeros.sort(reverse= True)
print("Los siguientes son los valores ordenados de mayor a menor ", numeros)
print("El valor de la lista es de ", sum(numeros))