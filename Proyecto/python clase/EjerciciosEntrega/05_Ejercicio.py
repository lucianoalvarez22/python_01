#En este ejercicio, creará un programa que calcule el promedio de una colección de valores ingresados por el usuario. 
# El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. 
# Su programa debería mostrar un mensaje de error apropiado si el primer valor ingresado por el usuario es 0.

def dame_lista_valores (stop): #Funcion que me devuelva una lista de valores introducidos
    valor_usuario = float(input("Dame un valor: "))
    coleccion_valores = []
    coleccion_valores.append(valor_usuario) #Introducir los valores del usuario en una lista

    if coleccion_valores[0] == stop: #Si el primer valor introducido de la lista es 0 = Error
        print("Error")
    else:
        while valor_usuario != stop: #Y sino mientras el valor introducido del usuario sea distinto de 0, vuelve a pedirme el input y sigue metiendolos en la lista "coleccion_valores"
            valor_usuario = float(input("Dame un valor: "))
            coleccion_valores.append(valor_usuario)
    return coleccion_valores #Devuelve todos los valores que hay en este momento dentro de la lista "coleccion_valores"


def promedio (lista_valores): #Funcion que devuelve los calculos del promedio
    contador = 0
    for i in (lista_valores): #Itero la lista de valores
        contador += i #Lo incremento al contador y voy sumando
    return contador/(len(lista_valores)-1) #Devuelvo el calcula de la suma del contador // la longitud de la lista -1 ("Menos 1" porque el ultimo elemento introducido es 0 que es para finalizar)

stop = 0 #Creo variable stop para poder cambiar el numero con el que se pare la introduccion de valores
coleccion_total_valores = dame_lista_valores(stop)
print(promedio(coleccion_total_valores))
