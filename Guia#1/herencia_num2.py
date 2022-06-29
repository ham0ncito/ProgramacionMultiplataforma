class Persona:
    nombre = ""
    edad = 0
    def mostrar_informacion(self):
        print(f" \n\t Hola {self.nombre}, de {self.edad} anios. Un gusto que trabajes con nosotros \n\n")
    def informacion (self):
        self.nombre = input(" Ingrese su nombre: ")
        self.edad = input(" Ingrese su edad:  ")

class Empleado(Persona):
    sueldo = 0
    def calcular_suelod(self):
        if self.sueldo > 3000:
            print(f"\n\t {self.nombre}, tiene que pagar impuestos, con una tasa de 15%")
            print(f"\t su impuesto a pagar es de {float(self.sueldo * 0.15):.2f}")
        else:
            print(f"\n\t {self.nombre}, no tiene que pagar impuestos todavia")
    def __salario__(self):
        self.sueldo = float(input("Ingrese su salario: "))

Mario = Empleado()

print("\n\t Programa Herencia \n")
Mario.informacion()
Mario.mostrar_informacion()
Mario.__salario__()
Mario.calcular_suelod()