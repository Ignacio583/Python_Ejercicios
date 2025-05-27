#10. Contar cuántos números son mayores que un valor dado.

lista=[2,4,7,3,10,18,20,29,31,36,42,45,55,65,74,86,97]
num=int(input("Ingrese un número límite:"))

nueva=[]
for i in lista:
    if num < i:
        nueva.append(i)
print(lista)
print(nueva)
print(f'Hay {len(nueva)} números más allá del límite')