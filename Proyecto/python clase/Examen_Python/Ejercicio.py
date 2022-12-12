""" 
Escribe una funcion que reciba como parametro una cadena de texto y devuelva una lista con las vocales que haya en dicha cadena
 """

def cadena_vocal(texto):
    vocales = ['a', 'e','i','o','u']
    lista_vocales = []
    for letra in texto:
        if letra.lower() in vocales and letra.lower() not in lista_vocales:
            lista_vocales.append(letra)
    return lista_vocales
            



cadena = 'luciano'
print(cadena_vocal(cadena))



""" 
Funcion que reciba una cadena y devuelva una cadena con los codigos ASCII de las letras
A = 65
B = 66
C = 67
 """

def txt_ascii (cadena):
    salida = []
    for i in cadena:
        salida.append(str(ord(i)))
    
    return ' '.join(salida)

cad = 'hola'
print(txt_ascii(cad))

""" Al reves ahora, de ASCCI a Cadena """

def ascii_txt(cadena):
    salida = ''
    cadena = cadena.split(' ')
    for c in cadena:
        salida += chr(int(c))
    return salida

print(ascii_txt(txt_ascii(cad)))