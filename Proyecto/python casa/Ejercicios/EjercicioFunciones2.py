# Programa que calcule el IVA de una compra, siendo el IVA del 19% sobre el
# valor total de la compra

valorCompra = float(input("Dime el valor total de la compra: "))

def calculaIva (valorCompra):
    return valorCompra * 0.19

precioAumentado = calculaIva(valorCompra)
precioTotal = calculaIva(valorCompra) + valorCompra

print(f"Tu compra ha aumentado en {round(precioAumentado,2)} al añadirle el IVA. El precio total es de {round(precioTotal,2)}")

