import pprint

#BUCLES FOR - CONTROLADOR POR UN CONTROLADOR - SABEMOS CUANTAS VUELTAS VA A DAR
#SINTAXIS DEL FOR ----  FOR VARIABLE (INICIO-FIN-SALTO)

#for i in range(20,50,2):  #LA i EMPIEZA A EJECUTARSE DESDE 0 HASTA EL 9 (10 EXCLUIDO) - Y CON DOS VALORES, EL PRIMERO ES EL INICIO Y EL SEGUNDO ES EL FINAL
    #print(f'La i vale {i}')



#EJEMPLO METIENDA ELEMENTOS EN UNA LISTA CON UN BUCLE
lista = []

for i in range(20):
    lista.append(f"Elemento {i}")

pprint.pprint(lista)



#OTRA FORMA DE FOR - PARA CADA ELEMENTO QUE HAYA EN LA LISTA, IMPRIMELO
for x in lista:      
    print(x)

























#WHILE CONTROLADO POR UNA CONDICION - NO SABEMOS CUANTAS VUELTAS VA A DAR, HASTA QUE SE CUMPLA LA CONDICION