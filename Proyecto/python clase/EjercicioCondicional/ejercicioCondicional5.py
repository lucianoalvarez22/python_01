#Escribe un programa que pida tres números. 
# El programa ha de indicar a continuación si estos tres valores son iguales, 
# si dos de ellos son iguales 
# o si son los tres distintos. 

print("Comparador de tres numeros: ")

numero1 = float(input("Escribe un numero: "))
numero2 = float(input("Escribe otro numero: "))
numero3 = float(input("Escribe otro numero mas: "))



if numero1 == numero2 == numero3: 
    print("Has escrito tres veces el mismo numero")

elif numero1==numero2 or numero2==numero3 or numero1==numero3:
    print("Has escrito uno de los numeros dos veces")

else:
    print("Los tres numeros que ha escrito son distintos")

