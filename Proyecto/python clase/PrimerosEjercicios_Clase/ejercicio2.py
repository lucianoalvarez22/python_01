#PEDIR AL USUARIO QUE TE DÉ UN NUMERO 
#Imprimir: "EL doble de 20 son 40
#Imprimir: "el cuadrado de 20 son 400"

numero = int(input())

doble = numero*2
cuadrado = numero * numero
print(doble)

#PRIMERA OPCION DE CONCATENAR CON "COMAS" ","
print("El doble de " , numero , "es " , doble)
print("El cuadrado de " , numero , "es " , cuadrado)


#SEGUNDA FORMA DE CONCATENAR PASANDO A STRING UN NUMERO CON "STR"
print("El doble de " + str(numero) , "es " + str(doble))
print("El cuadrado de " , str(numero) , "es " , str(cuadrado))

#INTERPOLACION CON "F"
mensaje = f"El doble de {numero} es {doble}"  
print(mensaje)


