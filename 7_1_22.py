
while(True):
    nombre = (str(input("\t Ingrese su nombre completo    ")))
    campus = (str(input("\t Ingrese su Campus    ")))
    edad = int(input("\t Ingrese su edad    "))
    with open("base.txt", "r+") as archivo:
        if (archivo.read()==""):
            archivo.write("\n\t Nombre \t Campus \t Carrera\n")
        archivo.write(f"\t{nombre}        \t      {campus}    \t   {edad}\n")
        x = str.lower(input("\n Desea agregar otro registro: [si/no]   "))
        if x != "si":
            exit()