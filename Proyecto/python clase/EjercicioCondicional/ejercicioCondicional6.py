#Escribe un programa que pida un año y que determine si ese año es bisiesto o no. 


print("Comprobador de años bisiestos")

aniocualquiera = int(input("Escribe un año y le diré si es bisiesto: "))

if aniocualquiera%4 == 0:
    if aniocualquiera%100 == 0:
        if aniocualquiera%400==0:
            print(f"El año {aniocualquiera} es bisiesto porque es multiplo de 400")
        else:
            print (f"El año {aniocualquiera} no es bisiesto porque es multiplo de 100 sin ser de 400")
    else:
        print(f"El año {aniocualquiera} es bisiesto porque es multiplo de 4")

else:
    print(f"El año {aniocualquiera} no es un año bisiesto")

       