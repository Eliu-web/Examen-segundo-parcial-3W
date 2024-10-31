print (" ")#Salto de linea
print ("Velazquez mares jesus eliu 3W 1276")#Nombre del creador del programa
print (" ")#Salto de linea

#Crea una lista de algunas materias
materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
materias_a_repetir = []
for x in materias:#crea un bucle for
    n = float(input(f"¿Cuál es tu nota en {x}? "))#pregunta al usuario la calificacion de una materia
    if n < 6: 
        materias_a_repetir.append(x)
#Muestra en pantalla que materias reprobo el usuario
if materias_a_repetir:
    print("tendras que repetir la siguientes materias")
    for x in materias_a_repetir:
        print(x)
else:
    print("no tienes ninguna materia reprobada (:")
#imprime en panatlla la lis
print (materias)

