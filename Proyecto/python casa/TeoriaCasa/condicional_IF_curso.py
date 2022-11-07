#IF "SI(CONDICIONAL)....HAZ ESTO"
#SINTAXIS IF NOTA <5: 

print("Programa de evaluacion de notas de alumnos")

nota_alumno=int(input("Introduce la nota del alumno "))

def evaluacion(nota): #FUNCIONA EVALUACION - DENTRO DE LA FUNCION ESTÁ EL IF
    valoracion="aprobado"
    if nota<5:                  
        valoracion="Suspenso"
    return valoracion


print(evaluacion(nota_alumno)) #NOTA_ALUMNO ES LO QUE HA PUESTO EL USUARIO EN EL INPUT Y EQUIVALE AL PARENTESIS (NOTA) DE LA FUNCION

