import  os
def calculadora (x, y, z):
    total = 0
    if z == "1":
        total = x + y
    elif z == "2":
        total = x-y
    elif z == "3":
        total = x * y
    elif z == "4":
        total = x / y
    return total

while(True):
    print("\t ***** Calculadora ****** \n\t 1. Suma \n\t 2. Resta \n\t 3. Multiplicacin \n\t 4. Division")
    opcion_elegida = str(input("Seleccione una opcion: "))
    num1 = float(input(" Ingrese el primer valor "))
    num2 = float(input(" Ingrese el siguiente valor "))
    x = calculadora(num1,num2,opcion_elegida)
    print(f"\n\n \t #### El resultado de su operacion es: {float(x):.2f} ### \n\n\n\t")
    var = str.lower(input("\t Desea realizar otra operacion [s/n] "))
    if var == "n":
        exit()
    else:
        os.system("cls")