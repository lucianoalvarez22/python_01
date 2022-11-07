#En este ejercicio, creará un programa que calcule el promedio de una colección de valores ingresados por el usuario. 
# El usuario ingresará 0 como valor centinela para indicar que no se proporcionarán más valores. 
# Su programa debería mostrar un mensaje de error apropiado si el primer valor ingresado por el usuario es 0.

def dame_lista_valores (stop):
    valor_usuario = float(input("Dame un valor: "))
    coleccion_valores = []
    coleccion_valores.append(valor_usuario)

    if coleccion_valores[0] == stop:
        print("Error")
    else:
        while valor_usuario != stop:
            valor_usuario = float(input("Dame un valor: "))
            coleccion_valores.append(valor_usuario)
    return coleccion_valores
def promedio (lista_valores):
    contador = 0
    for i in (lista_valores):
        contador += i
    return contador/(len(lista_valores)-1)
stop = 0
coleccionvalores = dame_lista_valores(stop)
print(promedio(coleccionvalores))
