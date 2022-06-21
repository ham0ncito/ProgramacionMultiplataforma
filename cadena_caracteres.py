'''
Programa que compara dos contrasenas
6/16/22
Escribir un programa que almacene la cadena de caracteres contrasena en una variable
, pregunte al usuario por la contrasena e imprima por la patanlla si la contrasea introducida por el
usuario coincide con la guardada en la variable sin tener en cuenta las mayusculas o minusculas
'''
contrasena_usuario = str(input("\n\t Ingrese su contrasena: "))
contrasena_verificacion = contrasena_usuario
contrasena_usuario = str(input("\n\n\t Ingrese nuevamente su contrasena: "))
if(contrasena_usuario.lower() == contrasena_verificacion.lower() or contrasena_usuario.upper() == contrasena_verificacion.upper()):
    print("\n\t Contrasena correcta")
else:
    print("\n\t Contrasena incorrecta")

for i in ["Francisco Morazan: Tegucigalpa", "Comayagua Comayagua", "Olancho Juticalpa", "La Paz La Paz", "Atlantida La Ceiba", "Colon Trujillo", "Copan Santa Rosa de Copan",
          "Cortes San Pedro Sula", "Choluteca Choluteca", "Santa Barbara Santa Barbara", "El Paraíso, Yuscarán", "Gracias a Dios, Puerto Lempira",
          "Intibucá, La Esperanza", "Lempira, Gracias","Ocotepeque, Nuevo Ocotepeque", "Valle, Nacaome", "Yoro Yoro"]:
    print(f"Departamento y Cabezera: {i}")

collection = {"johan": 10, "sofia": 15}
for i in collection:
    print(f"{collection[i]}")
 i = 0
while i < 5:
    print("Danilo Paguada")
    i+=1; 