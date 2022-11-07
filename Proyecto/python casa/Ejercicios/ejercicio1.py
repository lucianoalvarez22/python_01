
#Crea un programa que pida dos números por teclado. El programa tendrá una función
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.



numero1= int(input("Dame Numero 1: "))
numero2= int(input("Dame NUmero 2: "))

def DevuelveMax(numero1, numero2):
    if numero1 < numero2:
        print(numero2)
    
    elif numero2 > numero1:
        print(numero1)

    else:
        print("Son iguales")

print("El numero mas alto es: ")

DevuelveMax(numero1, numero2)

