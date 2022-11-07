#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. 
# Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por
#teclado)


nombre= input("Inserta tu nombre: ")
direccion= input("Inserta tu direccion: ")
telefono= int(input("Inserta tu telefono: "))

datosalmacenados= nombre, direccion, int(telefono)

Lista= [datosalmacenados]

print(f"Los datos almacenados son: {nombre}, {direccion}, {telefono}")

