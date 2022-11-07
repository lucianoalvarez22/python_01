#PEDIR LOS TRES CONEFICIENTES DE LA ECUACION DE SEGUNDO GRADO (A,B,C)
import math

a=int(input("Dame a= "))
b=int(input("Dame b= "))
c=int(input("Dame c= "))

cuadrado= b*b
raiz = cuadrado - 4 * a * c
a2 = 2 * a

if a == 0:
    if b == 0:
        print("No tiene solucion")
    else:
        solucion = -c/b
        print(f'Una solucion {solucion}')

else:
    if raiz >=0:
        solucionpos = ((-b + math.sqrt(raiz))/a2)
        solucionneg = ((-b - math.sqrt(raiz))/a2)

        if solucionneg == solucionpos:
            print(f'Una solucion {solucionpos}')
        else:
            print(f'Las soluciones de la ecuacion son {solucionpos} y {solucionneg}')
    else:
        print("No tiene solucion")