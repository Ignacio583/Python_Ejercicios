#13. Intercalar dos listas del mismo tamaño.
lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]

intercalar=[x for pair in zip(lista1,lista2) for x in pair]
print(intercalar)
print("****"*5)
#Por módulos:
a=[1,2,3,4,5]
b=[6,7,8,9,10]

intercalar=[]
for i in range(len(a)):
    intercalar.append(a[i])
    intercalar.append(b[i])
print(intercalar)

print("****"*5)

#Si las listas son Distintas:
from itertools import zip_longest

a=[1,2,3]
b=[4,5]
intercalar=[x for pair in zip_longest(a,b) for x in pair if x is not None]
print(intercalar)

print("****"*5)

 #por Módulos:
a=[1,2,3]
b=[4,5]
intercalar=[]

for i in range(max(len(a),len(b))):
    if i < len(a):
        intercalar.append(a[i])
    if i< len(b):
        intercalar.append(b[i])
print(intercalar)