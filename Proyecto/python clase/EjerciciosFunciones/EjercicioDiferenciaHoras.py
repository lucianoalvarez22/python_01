# FUNCION QUE RECIBA DOS HORAS EN FORMATO HH:MM:SS
#DEVOLVERÁ LA DIFERENCIA ENTRE ELLAS EN FORMATO HH:MM:SS

def dif(inicio,fin):
    
    lista_primera_hora = []
    for i in inicio:
        i = int(i)
        lista_primera_hora.append(i)

    lista_segunda_hora = []
    for s in fin:
        s = int(s)
        lista_segunda_hora.append(s)
    
    print(lista_primera_hora)
    print(lista_segunda_hora)
    
    resta_indice_cero = (lista_primera_hora[0] - lista_segunda_hora[0])
    resta_indice_uno = (lista_primera_hora[1] - lista_segunda_hora[1])
    resta_indice_dos = (lista_primera_hora[2] - lista_segunda_hora[2])
    restageneral = (f"{resta_indice_cero}, {resta_indice_uno},{resta_indice_dos}")
    return restageneral



hora_uno = "20:00:00"
trozos_primera = hora_uno.split(":")
hora_dos = "19:59:00"
trozos_segunda = hora_dos.split(":")
print(dif(trozos_primera,trozos_segunda))




