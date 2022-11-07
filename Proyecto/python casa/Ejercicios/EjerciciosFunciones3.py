# Programa que calcula la tabla de multiplicar de cualquier numero entero dado por 
# el usuario. Debe calcular la tabla del 0 hasta el 12.

def tablaMultiplicar (n1,n2):
    return str(n1) + " * " + str(n2) + " = " + str(n1*n2)

num = int(input("Dame un numero entero: "))

for i in range(0,13):
    print(tablaMultiplicar(num,i))

       