def suma(num1,num2):
    return num1 + num2

#print(suma(5,6))



#EJERCICIO FUNCION QUE DEVUELVA ########1234 COMO UNA TARJETA DE CREDITO



def censura(cadena):
    inicio = "*" * (len(cadena) - 4)
    final = cadena[-4:]
    return inicio + final

#print(censura("12345467879"))


#EJERCICIO FUNCION LETRA Y DEVUELVE TRUE SI LO CONTIENE

def contiene_letra(cadena, letra):
    #Devuelve TRUE si contiene la letra y FALSE si no la contiene
    return letra in cadena

if contiene_letra("aknskjfnrkengvkenvglenp", "p"):
    print("Contiene la p")
else:
    print("No")