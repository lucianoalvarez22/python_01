#Escribe un programa que solicite los coeficientes de una ecuación de primer grado (a.x + b =0)
# y que a continuación calcule y muestre como resultado la solución a la ecuación.

import math

print("Ecuacion a x + b = 0")

a=float(input("Escribe el valor del coeficiente a = "))
b=float(input("Escribe el valor del coeficiente b = "))

if a==0:

    if b==0:
        print("Todos son solucion")
    else:
        print("Sin solucion")

else:
    solucion = -b/a
    print(f"La solucion de la ecuacion es {solucion}")