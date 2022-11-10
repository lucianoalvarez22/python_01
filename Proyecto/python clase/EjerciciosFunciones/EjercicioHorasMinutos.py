
#HACER UNA FUNCION QUE RECIBA UNA HORA EN FORMATO HH:MM:SS
#Y DEVOLVERÁ LA CANTIDAD DE SEGUNDOS DE DICHA HORA


def dame_segundos (hora_introducida):

    hora_lista = []
    for i in hora_introducida:
        i = int(i)
        hora_lista.append(i)

    calculohoras = hora_lista[0] * 3600
    calculominutos = hora_lista[1] * 60
    calculosegundos = calculohoras + calculominutos + hora_lista[2]

    return calculosegundos


usuario_hora = input("Dame una hora: ")
trocear_hora = usuario_hora.split(":")
print(dame_segundos(trocear_hora))



    
