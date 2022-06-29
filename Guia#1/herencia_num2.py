class Persona:
    nombre = ""
    edad = 0
    def mostrar_informacion(self):
        print(f" \n\t Hola {self.nombre}, de {self.edad} anios")
    def __init__(self,x,y):
        self.nombre = x
        self.edad = y

class Empleado(Persona):
    sueldo = 0
    def calcular_suelod(self):
        if self.sueldo > 3000:
            print(f"\n\t {self.nombre}, tiene que pagar impuestos, con una tasa de 15%")
            print(f"su impuesto a pagar es de {float(self.sueldo * 0.15):.2f}")
    def __initFuncional__(self,x):
        self.sueldo = x

Mario = Empleado(Persona)

print("\n\t Programa Herencia")
nombre = str(input("\n\t Ingrese su nombre: "))
edad = int(input("\n\t Ingrese su edad: "))
Mario.mostrar_informacion()
salario = float(input("\n\t Ingrese su salario: "))
Mario.__init__(Persona, nombre,edad)
Mario.__initFuncional__(salario)
Mario.calcular_suelod()