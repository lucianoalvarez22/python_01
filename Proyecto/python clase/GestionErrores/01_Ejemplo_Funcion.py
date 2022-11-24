""" def division (numerador, denominador):
    #return numerador/denominador
    resultado = None
    try:
        resultado = numerador/denominador
    except ZeroDivisionError: #El error que me da al dividir entre 0
        print("Error 404 Not Found")
    return resultado
    


print(division(13,0)) """


def pide_numero ():
    try:
        numero = int(input("Inserta un numero entero: "))
        return True
    except Exception as e:
        print("No es un numero entero")


print(pide_numero())

