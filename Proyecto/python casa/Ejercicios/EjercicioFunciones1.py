# Programa que toma las tres notas de un estudiante y diga la nota final del curso
# Ten en cuenta que la primera y la segunda nota valen el 30% de la nota final.
# La tercera nota vale el 40%

def calcularNota (nota1,nota2,nota3):
    return (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)

nota1 = float(input("Dame la primera nota: "))
nota2 = float(input("Dame la segunda nota: "))
nota3 = float(input("Dame la tercera nota: "))

notaFinal = calcularNota(nota1,nota2,nota3)

print(f"La nota final del estudiante es {round(notaFinal,2)}")