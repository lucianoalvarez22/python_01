
#HACER UNA FUNCION QUE RECIBA UNA HORA EN FORMATO HH:MM:SS
#Y DEVOLVERÁ LA CANTIDAD DE SEGUNDOS DE DICHA HORA


def segundos (hora_introducida):
    trocear_hora = hora_introducida.split(":")
    hora_lista = []
    for i in trocear_hora:
        i = int(i)
        hora_lista.append(i)

    calculohoras = hora_lista[0] * 3600
    calculominutos = hora_lista[1] * 60
    calculosegundos = calculohoras + calculominutos + hora_lista[2]

    return calculosegundos

def dif_horas (inicio,fin):
    diferencia = abs(segundos(fin) - segundos(inicio))
    h = diferencia //3600
    m = diferencia % 3600//60
    s = diferencia % 3600 % 60

    return f"{h}:{m}:{s}"


""" usuario_hora = input("Dame una hora: ")
trocear_hora = usuario_hora.split(":")
print(segundos(trocear_hora)) """

print(dif_horas("20:00:00", "19:59:00"))


    
