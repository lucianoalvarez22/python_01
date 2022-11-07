#Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual
#que el primero. A continuación, el programa debe mostrar como resultado la suma de
#todos los enteros comprendidos entre el primero y el segundo incluidos ambos. Observa
#el formato del resultado en el modelo:

numero = int(input("Escribe un numero entero: "))
numeroMayor = int(input(f"Escribe un numero entero mayor que {numero}: "))

while numeroMayor<=numero:
    numeroMayor = int(input(f"Te he pedido un numero entero mayor que {numero}: "))


suma = 0
for i in range(numero,numeroMayor+1):
    suma = suma + i

print(f"La suma de los numeros comprendidos entre {numero} y {numeroMayor} es {suma}")