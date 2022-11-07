#FUNCION QUE CONCATENE LAS CADENAS CONTENIDAS EN ARGS Y LAS SEPARA CON EL SEPARADOR

def encadenar (separador, *args):
    return separador.join(args)



# -----------------------------------------

#Pedimos lista de cadenas
#Pedimos separador
#Llamamos a encadenar
#Imprimimos el resultado

palabras = []

while True:
    entrada = input("Dime una palabra: ")
    if entrada == "":
        break
    else:
        palabras.append(entrada)

sep = input("Dame un separador: ")

print(encadenar(sep,*palabras))



