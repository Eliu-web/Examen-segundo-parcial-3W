print (" ")#Salto de linea
print ("Velazquez mares jesus eliu 3W 1276")#Nombre del creador del programa
print (" ")#Salto de linea
#Crea un diccionario semivacio
Diccionario = {
    "nombre" : "",
    "edad" : "",
    "direccion" : "",
    "telefono" : ""
}
#Pregunta a el usuario sus datos
q =(input("Ingresa tu nombre: "))
w = (input("Ingresa tu edad: "))
e = (input("Ingresa tu direccion : "))
r = (input("Ingresa tu numero telefonico: "))
#Llena el vacio del diccionario con los datos del usuario
Diccionario["nombre"] = q 
Diccionario["edad"] = w
Diccionario["direccion"] = e
Diccionario["telefono"] = r
#Imprime en panatalla la sintaxis 
print(Diccionario["nombre"], "tiene")
print(Diccionario["edad"], "años, vive en ", Diccionario["direccion"], "y su número de teléfono es")
print(Diccionario["telefono"])
