'''
PROGRAMA QUE CALCULA SI SE DEBE TRIBUTAR A HACIENDA
PARA TRIBUTAR UN DETERMINADO IMPUESTO SE DEBE SER MAYOR DE 16 ANIOS
Y TENER UNOS INGRESOS IGUALES O SUPERIORES A 1000 MENSUALES, ESCRIBIR UN PROGRAMA
QUE PREGUNTE AL USUARUI SU EDAD Y SUS INGRESOS MENSUALES Y MUESTRE POR PANTALLA SI DEBE
TRIBUTAR O NO

'''
salario_tributar = 1000
edad_requerida = 16

print("Comprobacion de tributar")
nombre_usuario = str(input("\n\t Ingrese su nombre "))
edad_usuario = int(input("\n\t Ingrese su edad "))
salario_mensual = float(input("\n\t Ingrese su salario mensual"))
if (salario_mensual >= salario_tributar and edad_usuario > edad_requerida):
    print(f"\n\t {nombre_usuario}, tiene que tributar")
else:
    print(f"\n\n\t {nombre_usuario} , no es apto para tributar. \n\tAun queda tiempo para evadir impuestos")