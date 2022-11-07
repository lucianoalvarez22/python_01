#La duración de un mes varía de 28 a 31 días. 
# En este ejercicio, creará un programa que lea el nombre de un mes del usuario como una cadena
# Entonces su programa debería mostrar el número de días en ese mes. 
# Muestre "28 o 29 días" para febrero para que se aborden los años bisiestos.


def dame_dias (mes_usuario):
    meses = {
        "enero":"31 dias",
        "febrero":"28 o 29 dias",
        "marzo": "31 dias",
        "abril": "30 dias",
        "mayo": "31 dias",
        "junio": "30 dias",
        "julio": "31 dias",
        "agosto": "31 dias",
        "septiembre": "30 dias",
        "octubre": "31 dias",
        "noviembre": "30 dias",
        "diciembre": "31 dias"
    }
    return meses.get(mes_usuario)

ingresa_mes = input("Ingresa un mesa del año: ")
resultado = dame_dias(ingresa_mes)
print(f"El mes {ingresa_mes} tiene {resultado}")

