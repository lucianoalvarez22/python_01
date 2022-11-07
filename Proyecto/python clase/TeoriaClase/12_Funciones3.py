#EJERCICIO FACIL DE FUNCION DE SUMA


def suma_muchos(*args): # *args (ARGUMENTOS) INDICA UNA LISTA DE ARGUMENTOS Y ES UN ARGUMENTO OBLIGATORIO. 
                        #EN UNA FUNCION SIEMPRE SE PONE EN PRIMER LUGAR LOS PARAMETROS OBLIGATORIOS Y DESPUES LOS OPCIONALES
    total = 0
    for i in args:
        total += i
    
    return total


print(suma_muchos(1,2,3,4,5,6,7,8,9,12,21,21))