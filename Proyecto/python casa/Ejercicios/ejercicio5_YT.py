#Programa que valide si un numero es primo
#UN NUMERO ES PRIMO SI ES DIVISIBLE ENTRE ÉL MISMO Y ENTRE 1

def obtenerNumeroPrimo (numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2,numero):
            if numero % i == 0:
                return False #NO ES PRIMO
        return True #SI ES PRIMO
    

print(obtenerNumeroPrimo(100))