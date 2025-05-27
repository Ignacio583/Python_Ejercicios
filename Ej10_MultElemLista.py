#8. Multiplicar todos los elementos de una lista.

lista=[1,2,3,4,5,6]

nueva=1
for i in lista:
    nueva*=i 

print(lista)
print(nueva)

##8. Multiplicar los elementos de una lista x2.

lista=[1,2,3,4,5,6]
nueva=[]
for i in lista:
    nueva.append(i*2)
print(lista)
print(nueva)