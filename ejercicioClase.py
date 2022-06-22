'''
Escribí un programa que permita al usuario ingresar 6 números enteros, que
pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los
números negativos y el promedio de los positivos. No olvides que no es posible
dividir por cero, por lo que es necesario evitar que el programa arroje un error si
no se ingresaron números positivos.

'''

tipo_numero = [0, 0, 0]
acumuladores = [0, 0, 0]
valores = [0,0,0,0,0,0]
for i in range (6):
    valores[i] = int(input(f"\t {i+1}. Ingrese un valor \n"))
    if valores[i] < 0:
        tipo_numero[0] += 1
        acumuladores[0] += valores[i]
    elif valores[i] > 0:
        tipo_numero[1] += 1
        acumuladores[1] += valores[i]
    else:
        tipo_numero[2] += 1
        acumuladores[2] += valores[i]
if acumuladores[0] != 0 and tipo_numero[0] != 0:
    print(f"\t La sumatoria de los valores negativos es {float(acumuladores[0]):.2f} \n")
if acumuladores[1] != 0 and tipo_numero[1] != 0:
    print(f"\t El promedio de los valores positivos es {float(acumuladores[1] / tipo_numero[1]):.2f}\n")
if acumuladores[2] > 0:
    print(f"\t La sumatoria de los valores 0 es {float(acumuladores[2] / tipo_numero[2]):.2f}.2f")
print("\n Los valores ingresados fueron: ")
for i in  valores:
    print("\n {i}")