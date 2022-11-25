

""" 
Hacer un programa que pida al usuario una serie de caracteres
Al terminar le debe mostrar una lista con las vocales y otras con las consonantes
Además de decirle cuantas hay de cada una
Los caracteres que no son letra se descartan
 """

import string
def caracteres ():
    consonantes = 'BCDGHJKLMNÑPQRSTVXZWY'
    vocales = 'AEIOU'
    lista_vocales = []
    lista_consonantes = []
    while True:
        entrada = input('Dime una letra: ')
        if entrada == '':
            break
        if entrada.upper() in consonantes:
            lista_consonantes.append(entrada)
            
        elif entrada.upper() in vocales:
            lista_vocales.append(entrada)
    
    print(lista_consonantes)
    print(f"Consonantes: {len(lista_consonantes)}")

    print(lista_vocales)
    print(f"Vocales: {len(lista_vocales)}")
    


caracteres()

    