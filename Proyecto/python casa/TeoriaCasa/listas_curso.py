miLista = ["Maria", 5, True, 78.35, 'Antonio'] #UNA LISTA PUEDE CONTENER DISTINTOS TIPOS DE DATOS
miLista2= ["Paula","Elena"]
miLista3 = miLista+miLista2 #EL OPERADOR SUMA(+) CUANDO SE TRABAJA CON LISTAS, SE USA COMO CONCATENADOR
print(miLista3[:])

print(miLista[:]) #IMPRIME TODA LA LISTA 
print(miLista[2]) #ACCEDER A UN INDICE ESPECIFICO DE LA LISTA
print(miLista[-2]) #CON NUMEROS NEGATIVOS EMPIEZA A CONTAR DESDE EL FINAL PARA EL COMIENZO Y DESDE EL -1
print(miLista[0:3]) #IMPRIME POR PORCIONES, INCLUYE EL 0 Y EXCLUYE EL 3, IMPRIME DESDE EL 0 AL 2
print(miLista[:2]) #IMPRIME POR PORCIONES, LO MISMO QUE ARRIBA PERO OTRA FORMA DE HACERLO
print(miLista[1:2]) #IMPRIME POR PORCIONES, IMPRIME EL INDICE 1 Y EXCLUYE EL 2
print(miLista[2:]) #IMPRIME DESDE EL INDICE 2 HASTA EL FINAL DE LA LISTA


#miLista.append("Sandra") # APPEND AGREGA EL ELEMENTO AL FINAL
#miLista.insert(2,"Sandra") #INSERT AGREGA EL ELEMENTO EN LA POSICION QUE QUERAMOS
miLista.extend(["Sandra","Ana","Luciano"]) #AGREGAR VARIOS ELEMENTOS A UNA LISTA

print(miLista.index("Antonio")) #INDEX PARA SABER EN QUE POSICION ESTÁ EL ELEMENTO QUE QUIERO

print("PepeS" in miLista) #IN PARA SABER SI UN ELEMENTO ESTÁ EN LA LISTA CON TRUE O FALSE

miLista.remove("Ana") #REMOVE PARA ELIMINAR UN ELEMENTO DE UNA LISTA
miLista.pop() #ELIMINA EL ULTIMO ELEMENTO DE UNA LISTA



print(miLista[:]) 





