#LE PIDO SACAR DINERO AL CAJERO Y QUE ME DIGA EN CUANTOS BILLETES ME LO VA A DAR
import pprint
monedas = [500,200,100,50,20,10,5,2,1]
numero= int(input("Dame tu numero: "))

desglose = {}

for m in monedas:

    desglose[m] = numero // m #DIVISION ENTRE EL NUMERO Y LA MONEDA = LOS BILLETES QUE ME DA CON CADA MONEDA
    numero = numero % m #EL RESTO DE DINERO QUE ME QUEDA

#pprint.pprint(desglose)

for clave,valor in desglose.items():
    if valor > 0:
        print(f"{valor} X {clave}")