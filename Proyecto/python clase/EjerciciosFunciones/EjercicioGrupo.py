#UN CONJUNTO DE PERSONAS 
#FUNCION DEVOLVER UNA LISTA Y DENTRO DE ESA LISTA OTRA LISTA CON NOMBRES
import random

def crea_equipos (lista_gente,miembros):
    if len(lista_gente) < miembros:
        return lista_gente
    elif miembros == 0:
        return []
        
    random.shuffle(lista_gente)
    num_grupos = len(lista_gente) // miembros
    lista_general = []

    for i in range(num_grupos):
        equipo = []
        for j in range (miembros):
            equipo.append(lista_gente.pop())
        lista_general.append(equipo)

    for p in range (len(lista_gente)):
        lista_general[p].append(lista_gente[p])

    return lista_general

alumnos = ["Javi","Jose","Miguel","A.Muñoz","Ana","A.Sanchez","Luciano","Juan","Pablo","Dani","Pedro","P.Gonzalez","Carlos","Adrian"]
print(crea_equipos(alumnos,3))