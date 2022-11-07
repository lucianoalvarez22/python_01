
#Escribe un programa que pida dos números enteros y que a continuación indique si el
#número mayor es múltiplo del menor. 

print("Comparador de multiplos")

numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))

if numero1 >= numero2:
    if numero1%numero2==0:
        print(f"{numero1} es multiplo de {numero2}")
    else: 
        print("No son multiplos")

else:
    if numero2%numero1==0:
        print(f"{numero2} es multiplo de {numero1}")
    else: 
        print(f"{numero2} no es multiplo de {numero1}")
