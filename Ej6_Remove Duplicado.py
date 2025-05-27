#5. Eliminar los elementos duplicados de una lista.

lista=[1,4,2,4,7,6,3,5,1,6,7,9,0,5,11,1,43,65,5,1,87,3,99,546,9,1,24]

conjunto=set(lista)#pasa una lista a conjunto
print(conjunto)
sinduplicados=list(set(lista)) #Es una lista con principio de conjunto
print(sinduplicados)


