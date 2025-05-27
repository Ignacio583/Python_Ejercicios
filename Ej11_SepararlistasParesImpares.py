#9. Separar elementos pares e impares en dos listas diferentes.

lista=[2,4,7,3,72,8,9,11,45,75,345,94,76,57]

pares=[]
impares=[]
for num in lista:
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)

print(lista)
print(f'Los números pares en la lista son {pares}')
print(f'Los números impares en la lista son {impares}')