
#comentario en python
'''Comentario en python
multiline comment
Programacion multiplataforma
1301
variable = "hola mundo"
print(variable)
print(2+3)
print("\n Hola \n world")
'''



print("***************************** UNICAH  SCJ 2022 ******************************************* \nA.Ingrese sus datos personales \nB.Mostrar datos personales \nC.Salir \n\n ***************************************************************** \n\t Ingrese su opcion: ")

variable = str(input())
if variable != 'c' or variable != 'C':
    print("******************************Vehiculos / UNICAH SAP ******************************************* \nVEHICULO \t Placa \t Modelo \n Toyota \t HB4356 \tHilux \n\n ****************************************************************************************")
else:
    print("\n\t Adios")
    for x  in range(3,10) :
        print("Hello World")
menu = "***************************** UNICAH  SCJ 2022 ******************************************* \nA.Ingrese sus datos personales \nB.Mostrar datos personales \nC.Salir \n\n ***************************************************************** \n\t Ingrese su opcion: "
print(type(menu))
variable = "HOLA MUNDO"
print(type(variable))

variable = 2.4
print((type(variable)))
variable = 'c'

print(type(variable))
variable = True
print(type(variable))


"""
tipado dinamico, una variable puede
contener cualquier valor
"""
numero1 = 45
numero2 = 30
resultado = numero1 + numero2
print(resultado)

resultado = numero1 - numero2
print(resultado)

numero1 =50
numero2 = 50
print(numero1 * numero2)

print(float(numero1 / numero2))
print(float(numero1 ** numero2))



variable1 = float(13/5)
variable2 = 3
variable3 = 2
variable4 = 4

resultado_final = (variable1 - (variable3*variable4)) * variable2 ** variable2
print("El resultado final es ", float(resultado_final))



'''
operadores relacionales
'''

resultado = 10 > 30
print(resultado)
numero1= 10
numero2 = 30
resultado= numero1 < numero2
print(resultado)

resultado = numero1 <= numero2
print(resultado)
resultado = numero1 >= numero2
print(resultado)
resultado = numero1 == numero2
print(resultado)
resultado = numero1 != numero2
print(resultado)

#determine el valor booleano de la siguiente respuesta

a = 45
b = 56
c = 15
print (a==b and a >=12 and b<a)

a = 10
b= 8
c = 3
d = a

print((a>b or a<c )and (a==c or a>=b))
