#Programa que valide si una contraseña especificada por el usuario es segura

#Una contraseña segura:
# Tiene mas de 8 caracteres
#Tiene al menos una letra mayuscula
# Tiene al menos un numero

""" print(len("hola"))
    print("a".isupper())
    print("1".isnumeric())"""

def comprobar_contraseña (contraseña_ingresada):
    largo = False #LOS HEMOS PUESTO TODOS EN FALSE PARA HACER LAS VERIFICACIONES
    mayus = False
    numer = False
    if len(contraseña_ingresada) > 8: #LEN PARA VERIFICAR SI LA CONTRASEÑA TIENE MAS DE 8 LETRAS
        largo = True
    for i in range(len(contraseña_ingresada)):
        if contraseña_ingresada[i].isupper(): #ISUPPER ES PARA VERIFICAR SI HAY MAYUSCULAS EN CONTRASEÑA
            mayus = True
        elif contraseña_ingresada[i].isnumeric(): #ISNUMERIC PARA VERIFICAR SI HAY ALGUN NUMERO EN "CONTRASEÑA"
            numer = True

    if largo and mayus and numer: #VERIFICAMOS SI LOS TRES SON VERDADEROS(CORRECTOS)
        return True
    else:
        return False


contraseña = input("Escribe una contraseña: ")
verificacion = comprobar_contraseña(contraseña)

if verificacion == True:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")

