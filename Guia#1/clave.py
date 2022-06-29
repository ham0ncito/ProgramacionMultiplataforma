print("\n\t Programa Claves")
condicional = ["macarronesConQueso22"]
y = 1
for i in range (3):
    x = str(input(" Ingrese la contrasena: "))
    condicional.append(x)
valor = len(condicional)-1
for i in range(valor):
    if str.lower(condicional[0]) == str.lower(condicional[y]):
        print(f"La contraseña {y} coincide ")
    else:
        print(f"La contraseña {y} no coincide con la original")
    y +=1