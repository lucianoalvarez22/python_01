def introduce_numero_en_lista():
    lista_numeros = []
    while True:
        ingresa_usuario = int(input("Ingresa un número entero o presiona el número 0 para terminar de ingresar números: "))
        if ingresa_usuario == 0:
            break
        lista_numeros.append(ingresa_usuario)

    return lista_numeros 



def calcular_suma_pares(lista_numeros):
    contador_suma_pares = 0
    for i in lista_numeros:
        if i%2 == 0:
            contador_suma_pares += i
    return contador_suma_pares



def calcular_suma_impares(lista_numeros):
    contador_suma_impares = 0
    for i in lista_numeros:
        if i%2 != 0:
            contador_suma_impares += i
    return contador_suma_impares


listado_numeros = introduce_numero_en_lista()
print("Suma de numeros pares:")
print(calcular_suma_pares(listado_numeros))
print("Suma de numeros impares:")
print(calcular_suma_impares(listado_numeros))