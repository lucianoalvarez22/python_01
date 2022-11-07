#Escribe un programa que pida por pantalla un número entero y que a continuación calcule
#su factorial. En número ha de ser mayor que cero.

numero = int(input("Escribe un numero entero mayor que cero: "))


while numero == 0:
    numero = int(input(f"Te he pedido un numero entero mayor que 0: "))

multi = 1
for i in range(1, numero+1):
    multi = multi * i

print(f"El factorial de {numero} es: {multi}")


