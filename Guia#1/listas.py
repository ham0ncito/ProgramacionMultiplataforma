import os

seguir = True
lista = []
print("\n\t Programa Listas")
for i in range(5):
    x = str(input("\n\t Ingrese un caracter: "))
    lista.append(x)
print("\n\t Los valores ingresados fueron", lista)
while(seguir):
    x =str(input("\n\n\t #### Menu ### \n\t 1. Agregar un nuevo valor \n\t 2. Eliminar un valor \n\t 3. Salir"))
    if x == "1":
        y = input(" \n\t Valor que desea agregar: ")
        lista.append(y)
        print("\n\t La nueva lista es la siguiente: ", lista)
    elif x=="2":
        y = str(" \n\t El valor que desea eliminar es:  ")
        del lista[y]
        print("\n\t La nueva lista es la siguiente: ", lista)
