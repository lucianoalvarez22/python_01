# Comúnmente se dice que un año humano equivale a 7 años caninos. 
# Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. 
# Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10,5 años caninos y luego contar cada año humano adicional como 4 años caninos.
# Escriba un programa que implemente la conversión de años humanos a años caninos descrita en el párrafo anterior. 
# Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más años humanos. 
# Su programa debería mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.

def validacion_negativo(): #Funcion para validar si mete una edad negativa y devuelve la edad correcta introducida por el usuario
    usuario_edad = int(input("Introduce tu edad: "))
    while usuario_edad < 0:
        print("No puedes ingresar un numero negativo")
        usuario_edad = int(input("Vuelve a introducir tu edad: "))
    return usuario_edad

def conversion (anio_humano): #Funcion para hacer la conversion a año canino. Devuelve años caninos.
    anio_canino = 0
    for i in range (0,anio_humano):
        if i >= 0 and i < 2:
            anio_canino += 10.5
        else:
            anio_canino += 4
    return anio_canino


edad = validacion_negativo() #Creo variable edad y meto dentro la edad introducida por el usuario
print(f"Tu edad es de {edad} años. Equivale a {conversion(edad)} años perrunos")
    
    






