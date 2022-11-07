#Escribe un programa que pida dos números enteros, el segundo ha de ser mayor o igual 
# que el primero. A continuación, se debe mostrar por pantalla una lista con todos los 
# números enteros comprendidos entre los números introducidos, indicando en cada caso 
# si el número escrito es par o impar.

numero = int(input("Escribe un numero entero: "))
numeroMayor = int(input(f"Escribe un numero entero mayor o igual que {numero}: "))


while numeroMayor<numero:
    numeroMayor = int(input(f"Te he pedido un numero entero mayor que {numero}: "))

for i in range(numero,numeroMayor+1):

    if i%2 == 0:
        print(f"El numero {i} es par")
    else:
        print(f"El numero {i} es impar") 
    

    





        """ if numero != int and numeroMayor != int:
            numero = int(input(f"Porfavor introduzca un numero entero: "))
            numeroMayor = int(input(f"Porfavor introduzca un numero entero: ")) """

        
            
            







    #print(i)