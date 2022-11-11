#Escriba un programa que solicite al usuario que ingrese 5 números, separados por comas. 

# Calcule la suma de los 5 números y muestre los números ingresados y la suma al usuario.

usuario_numeros = input("Ingresa cinco numeros separados por comas: ") #valores en string
trozos_numeros = usuario_numeros.split(",") #Lo troceo con split y me lo devuelve en una lista


def suma_total (cadena_troceada): #Funcion de devuelva la suma total de los numeros introducidos por el usuario
    contador = 0
    for i in (cadena_troceada): #Itero la lista troceada
        i = int(i) #Lo convierto a entero antes para poder sumar los valores
        contador += i #A cada iteracion voy añadiendo y sumando los valores
    return contador


print(f"La suma total es {suma_total(trozos_numeros)}")


