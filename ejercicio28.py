lista = []

for i in range (9):
    x = int(input("Ingrese un valor"))
    lista.append(x)
print("Los valores ingresados fueron")
for i in lista:
    print(i)
lista = lista.sort()
print("Los valores ingresados de menor a mayor son")
for i in lista:
    print(i)
lista = lista.sort(reverse=True)
print("Los valores ingresados de mayor a menor son")
for i in lista:
    print(i)


