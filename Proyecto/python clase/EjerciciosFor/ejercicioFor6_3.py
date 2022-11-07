#Crea un programa que cree dibujos del tipo mostrado en el ejemplo. 
# El programa ha de preguntar por el número de filas que tenga la estructura:



numero = int(input("Numero de filas: "))

asterisco= "*"
guion= "-"
tab = "\t"
incremento = 1

for i in range(numero-1,-1,-1):
    print(tab*i, asterisco)
