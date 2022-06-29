from datetime import datetime
cajero = ["Usuario", 15600, "registro.txt"]

def ingreso(x,y):
    x +=y
    return  x
def salida(x,y):
    if y <= x:
        x -= y
        return x
    else:
        print("\t #### No hay saldo suficiente ####")

with open(cajero[2], 'a') as arc:
    continuar = True
    hora = datetime.now()
    arc.write(f"\n Se ingreso al banco el dia {hora}")
    while(continuar):
        op = str(input("\n\n\t ******* Cajero ******* \n\t 1.Ingresar dinero a la cuenta \n\t 2. Retirar dinero de la cuenta"
            "\n\t 3. Consultar saldo \n\t Seleccione su opcion: "))
        if op == "1":
            cantidad = float(input(" Ingrese la cantidad a depositar: "))
            arc.write(f"\n Se ingresaron {cantidad} lempiras el dia {hora}")
            cajero[1] = ingreso(float(cajero[1]),cantidad)
        elif op == "2":
            cantidad = float(input(" Ingrese la cantidad a retirar: "))
            arc.write(f"\n Se retiraron {cantidad} lempiras el dia {hora}")
            cajero[1] = salida(float(cajero[1]), cantidad)
        elif op == "3":
            print(f" \n\t {cajero[0]} su saldo actual es {float(cajero[1]):.2f}")
            arc.write(f"\n Se consulto el saldo actual de: {cajero[1]} lempiras el dia {hora}")
        else:
            print("\n\t Opcion Incorrecta")
        cont= str.lower(input(" Desea realizar otra operacion [s/n]"))
        if cont != "s":
            continuar = False
