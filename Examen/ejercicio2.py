'''
Realice un programa haciendo uso de listas o diccionario en donde se le pida ingresar los
datos de los empleados y guarde los datos en un archivo de texto con el nombre de
data.txt. (30%
'''

datos_usuarios = {}
archivo = open('data.txt', 'r+')
opc =str(input(" \t ### MENU ### \n\t1. Ingresar datos personales \n\t2.Mostrar datos guardados \n\t3.Mostrar el salario menor \n\t4. Salir \n\t Ingrese su opcion"))
if opc == "1":
    if archivo.read() == "":
        archivo.write("\n\tCodigo \t Nombre \t Direccion \t Salario")
    datos_usuarios["codigo"] = str(input("\t Codigo de empleado"))
    archivo.write(datos_usuarios["codigo"])
    archivo.write("\t")
    datos_usuarios["Nombre"] = str(input("\t Ingresu su nombre"))
    archivo.write(datos_usuarios["Nombre"])
    archivo.write("\t")
    datos_usuarios["Direccion"] = str(input("\t Ingrese su direccion"))
    archivo.write(datos_usuarios["Direccion"])
    archivo.write("\t")
    datos_usuarios["salario"] = float(input("\tIngrese su salario"))
    archivo.write(str(datos_usuarios["salario"]))
    archivo.write("\t\n")
elif opc == "2":
    print((archivo.readlines()))
elif opc == "3":
    minv = min(datos_usuarios, key=lambda key:datos_usuarios[key])
    print(minv)
else:
    exit()
