#Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas. 

# Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario.

usuario_numeros = input("Ingresa cinco numeros separados por comas: ")
trozos_numeros = usuario_numeros.split(",")


def suma_total (cadena_troceada):
    contador = 0
    for i in (cadena_troceada):
        i = int(i)
        contador += i
    return contador


print(f"La suma total es {suma_total(trozos_numeros)}")


