#DIME SI UN NUMERO ES PAR O IMPAR



numero = int(input("Dame un numero: "))
numero_par = numero%2

if numero_par == 0:
    print("Es par")

else:
    print("Es impar")