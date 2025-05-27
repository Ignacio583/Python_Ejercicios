#7. Eliminar los elementos duplicados de una lista.

lista=[1,4,2,4,7,6,3,5,1,6,7,9,0,5,11,1,43,65,5,1,87,3,99,546,9,1,24]

sin_duplicado=[]

for elemento in lista:
    if elemento not in sin_duplicado:
        sin_duplicado.append(elemento)

print(lista)
print(sin_duplicado) 