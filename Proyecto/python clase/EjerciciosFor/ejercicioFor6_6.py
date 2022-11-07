#Crea un programa que cree dibujos del tipo mostrado en el ejemplo. 
# El programa ha de preguntar por el número de filas que tenga 
# la estructura:

numero = int(input("Dame un numero: "))
espacio = numero - 1
caracteres = 1

for i in range(numero):
    print("\t" * espacio + "*\t" * caracteres + "\t" * espacio )
    espacio -=1
    caracteres +=2

















""" numero = int(input("Dame el numero: "))
incremento = 1

for i in range(numero-1,-1,-1):
    print("\t"*i, "*\t" * incremento)
    incremento = incremento+2 """