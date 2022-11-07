import time

#time.sleep(5) #SLEEP SIRVE PARA QUE SE PARE EN ESTA LINEA 5 SEGUNDOS(SIEMPRE SEGUNDOS) HASTA IR A LA PROXIMA LINEA
#print('FIN')

#HACER UN PROGRAMA QUE LE PIDE AL USUARIO EL INTERVALO SLEEP "¿CUANTO TIEMPO VA TARDAR EL X COSA?"
#QUE SE ESPERE LOS 5 SEGUNDOS
#SACA EL POLLO

usuario = int(input("Cuanto tiempo va a tardar el pollo en el horno?"))

time.sleep(usuario)

print("Saca el pollo que se quema!!!!")
