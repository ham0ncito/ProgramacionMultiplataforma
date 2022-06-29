import os

seguir = True
lista = []
print("\n\t Programa Listas")
for i in range(5):
    x = str(input("\n\t Ingrese un caracter: "))
    lista.append(x)
print("\n\t Los valores ingresados fueron", lista)
while(seguir):
    x =str(input("\n\n\t #### Menu ### \n\t 1. Agregar un nuevo valor \n\t 2. Eliminar un valor \n\t 3. Salir \n\t Opcion: "))
    if x == "1":
        y = input(" \n\t Valor que desea agregar: ")
        lista.append(y)
        print("\n\t La nueva lista es la siguiente: ", lista)
    elif x=="2":
        y = str(input(" \n\t El valor que desea eliminar es:  "))
        busqueda = lista.index(y)
        del lista[busqueda]
        print("\n\t La nueva lista es la siguiente: ", lista)
    elif x == "3":
        print(" \n\t Nos vemooossss ")
        exit()
    else:
        print("\n\t Opcion incorrecta")
    continuar = str(input("\n\t Desea continuar [s/n]: "))
    if continuar != "s":
        exit()