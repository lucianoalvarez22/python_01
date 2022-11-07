#Escribe un programa que pida por teclado en primer lugar el año actual 
# y después un año cualquiera. 
# A continuación, el programa ha de indicar cuántos años faltan para llegar o
#cuantos años han pasado al/desde ese segundo año.


print("Comparador de años")

añoactual= int(input("¿En que año estamos? "))
añocualquiera= int(input("Escribe un año cualquiera: "))

años_restantes = añocualquiera - añoactual
años_transcurridos = añoactual - añocualquiera

if añoactual < añocualquiera:
    print(f"Para llegar al año {añocualquiera} faltan {años_restantes} años")

elif añoactual > añocualquiera:
    print(f"Desde el año {añocualquiera} han pasado {años_transcurridos} años")

elif añoactual > añocualquiera+1:
    print(f"Para llegar al año {añocualquiera} falta 1 año")

else:
    print("¡Son el mismo año!")

