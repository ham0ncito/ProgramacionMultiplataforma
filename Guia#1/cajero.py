from datetime import datetime
cajero = ["Usuario", 15600, "registro.txt"]
def ingreso(x,y):
    x +=y
def salida (x,y):
    x -= y
with open(cajero[2], "r+") as arc:
    print("\t ******* Cajero ******* \n\t 1.Ingresar dinero a la cuenta \n\t 2. Retirar dinero de la cuenta"
        "\n\t 3. Consultar saldo \n\t Seleccione su opcion: ")
    hora = datetime.now()
    arc.write("Se ingreso al archivo el dia ",hora.date()," con hora ", hora.time() )
