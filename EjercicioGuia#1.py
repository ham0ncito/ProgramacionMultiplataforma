numeros_negativos = []
negativo = True
for i in range(4):
    while negativo:
        numeros_negativos.append(int(input("Ingrese un numero negativo")))
        if numeros_negativos[i] < 0:
            negativo = False
for i in numeros_negativos:
    print(i)

x = 1
lista = [x]

for i in range(0, 20, 1):
    list.insert(x, i)
    x += 1
for i in lista:
    print(i)
