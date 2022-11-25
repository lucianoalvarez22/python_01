
#Funcion que calcule la letra del DNI
#Las letras válidas: TRWAGMYFPDXBNJZSVHLCKE
#UN DNI SERÁ VALIDO SI CUMPLE LO SIGUIENTE:
# LONGITUD DE 8 NUMEROS
# LA LETRA SERÁ VALIDA SI EL INDICE COINCIDE CON EL RESTO DE LA DIVISION ENTERA DEL NUMERO ENTRE 23

def calcula_letra (dni):
    letras_validas = 'TRWAGMYFPDXBNJZSQVHLCKE'
    indice = dni % 23
    letra = letras_validas[indice]
    return letra
    



def valida_dni(dni):
    return len(dni) == 9 and calcula_letra(int(dni[:8])) == dni[8].upper()



print(valida_dni('55000173C'))