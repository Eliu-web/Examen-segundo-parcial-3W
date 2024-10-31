print (" ")#Salto de linea
print ("Velazquez mares jesus eliu 3W 1276")#Nombre del creador del programa
print (" ")#Salto de linea
#Pregunta al usuario por su calificacion
q = (float(input("Ingresa tu calificacion en matematicas: ")))
w = (float(input("Ingresa tu calificacion en fisica: ")))
e = (float(input("Ingresa tu calificacion en quimica: ")))
r = (float(input("Ingresa tu calificacion en historia: ")))
t = (float(input("Ingresa tu calificacion en lengua: ")))
#Crea una lista de las materias
lista = ("Matemáticas", "Física", "Química", "Historia", "Lengua")
#Muestra en pantalla el nombre de las materias y su calificacion correspondiente
print ("En", lista[0], "has sacado ", q)
print ("En", lista[1], "has sacado ", w)
print ("En", lista[2], "has sacado ", e)
print ("En", lista[3], "has sacado ", r)
print ("En", lista[4], "has sacado ", t)