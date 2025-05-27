#4. Invertir una lista usando reverse(), [::-1]y con una función.

lista=[1,2,3,4,5,6]
print(lista)
lista.reverse()
print(lista)
print("****"*5)

lista=[1,2,3,4,5,6]
print(lista)
nueva=lista[::-1]
print(nueva)

print("****"*5)

lista=[1,2,3,4,5,6]
invertida=[]

for i in range(len(lista)-1,-1,-1):
    invertida.append(lista[i])
print(invertida)
