
def encontrar_impares (integers):
    lista_pares = []
    lista_impares = []
    for i in integers:
        if i% 2 == 0: #Es par
            lista_pares.append(i)
        else:
            lista_impares.append(i)
    
    if len(lista_pares) == 1:
        return lista_pares[0]
    else:
        return lista_impares[0]

numeros = [2,4,0,100,4,11]
print(encontrar_impares(numeros))
    
