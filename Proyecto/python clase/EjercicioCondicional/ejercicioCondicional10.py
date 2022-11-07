#Escribe un programa que pida una distancia en centímetros y que Escribe esa distancia en
#kilómetros, metros y centímetros (escribiendo solamente las unidades necesarias).

numero = 54
km = numero / 100_000
restokm = numero%100_000

m=restokm/100
restom = restokm%100

mensaje= f"Nuestro numero {numero} es \n {km} kilómetros \n {m} metros \n {restom} centímetros"

print(mensaje)


