# ELSE - "Y SI NO ES VERDAD...HAZ ESTO"
#ELSE SIEMPRE TIENE QUE IR ACOMPAÑADO DE UN IF 
#ELSE SIEMPRE TOMARÁ COMO COMPAÑERO AL ULTIMO IF QUE APARECE
#ELIF PUEDE IR ENTRE IF Y ELSE Y HACE QUE FUNCIONE COMO UN UNICO BLOQUE

print("Verificacion de acceso")

edad_usuario= int(input("Introduce tu edad porfavor: "))

if edad_usuario <18:
    print("No puedes entrar")

elif edad_usuario>100:
    print("Edad incorrecta")

else: 
    print("Puedes entrar")
print("El programa ha finalizado")