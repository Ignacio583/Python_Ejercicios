#3. Contar cuántas veces aparece un elemento específico en una lista.

lista=[1,4,6,3,5,1,6,7,9,0,5,11,1,43,65,5,1,87,3,99,546,9,1,24]
repeticion=lista.count(1)
print (repeticion)
print("****"*5)

numero=int(input("Ingrese un numero entero para identificar en la lista: "))
print(lista)
repeticion=lista.count(numero)
print(f'El número {numero} se repite {repeticion} cantidad de veces')