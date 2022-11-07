#Programa que calcule el nuevo salario de un trabajador si obtuvo un incremento del x%

def calcular_incremento (salario,incremento_x):
    aumento_salario = salario * (incremento_x /100)
    nuevo_salario = salario + aumento_salario
    return nuevo_salario



salario_actual = float(input("Ingresa el salario actual del trabajador: "))
incremento = float(input("Ingresa el porcentaje de incremento: "))

Salario_total = calcular_incremento(salario_actual,incremento)
print(f"El salario de trajador era {salario_actual}. Y ha incrementado en {Salario_total}")