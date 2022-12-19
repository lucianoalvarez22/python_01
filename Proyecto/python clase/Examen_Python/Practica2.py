def numero_mes (nombre_mes):
     
    meses = { 
        "enero":"1",
        "febrero":"2",
        "marzo": "3",
        "abril": "4",
        "mayo": "5",
        "junio": "6",
        "julio": "7",
        "agosto": "8",
        "septiembre": "9",
        "octubre": "10",
        "noviembre": "11",
        "diciembre": "12"
    }

    if nombre_mes not in meses:
        return "ERROR - NO EXISTE"
    return meses.get(nombre_mes) 

ingresa_mes = input("Ingresa el nombre del mes: ").lower()
resultado = numero_mes(ingresa_mes)
print(f"El número del mes {ingresa_mes} = {resultado}")