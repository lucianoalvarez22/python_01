#UNA FUNCION PUEDE RECIBIR VARIOS PARAMETROS SEPARADOS POR COMAS
#LOS PARAMETROS O ARGUMENTOS PUEDEN SER DE DISTINTO TIPO (NUMEROS ENTEROS, TEXTO, BOOLEANOS, FLOAT)
#LAS FUNCIONES PUEDEN DEVOLVER VALORES CON LA INSTRUCCION "RETURN"

def suma(num1,num2): 

    resultado=num1+num2
    return resultado

almacena_resultado = suma(8,7)

print(almacena_resultado)
    
    # print(num1+num2) #ESTO ESTÁ DENTRO DE LA FUNCION

# print(suma(5,7)) #EN ESTA LLAMADA LE ESTAMOS DICIENDO QUE SUME NUM1=5 + NUM2=7


# print(suma(2,3)) #EN ESTA LLAMADA LE ESTAMOS DICIENDO QUE SUME OTROS PARAMETROS 2+3



# print(suma(35,200)) #EN ESTA LLAMADA OTROS PARAMETROS