#Tenemos un texto 
# Limpiar el texto de signos de puntuacion
# Eliminar palabras no relevantes (Menos de 3 letras)
# Contabilizar palabras del texto en formato diccionario 
# Devolver el diccionario

#PENSEMOS:
# 0. PASAR A MINUSCULA
# 1. QUITAR SIGNOS DE PUNTUACION
# 2. DIVIDIR LA CADENA POR PALABRAS
# 3. IGNORAR PALABRAS DE 3 LETRAS O MENOS
# 4. PROCESAR LA CADENA

import string
def frecuencias(texto):
    salida_dict = {}
    # O.
    texto = texto.lower()
    #1.
    signos_puntuacion = list(string.punctuation)
    for s in signos_puntuacion:
        texto = texto.replace(s,"")

    
    palabras = texto.split() #3.
    for palabra in palabras:
        if len(palabra) > 3:
            if salida_dict.get(palabra) == None:
                salida_dict[palabra] = 1
            else:
                salida_dict[palabra] += 1
    return salida_dict

    

texto_ipsum = "Sed ut perspiciatis unde, omnis unde iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque!!!!!!!!!porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia ,non numquam eius modi tempora incidunt. ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis. nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

print(frecuencias(texto_ipsum))


""" signos_puntuacion = [".",",",";",":","!","¡","?","¿",")","("] """