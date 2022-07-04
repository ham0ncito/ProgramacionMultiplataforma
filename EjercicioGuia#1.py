numeros_negativos = []
y = 1
while y <= 5:
        x = int(input("Ingrese un numero negativo "))
        if x < 0:
            numeros_negativos.append(x)
             
            y+=1
            continue
        else:
            print(("\n\t El valor anterior no es un numero negativo"))
else:
    print(numeros_negativos)

