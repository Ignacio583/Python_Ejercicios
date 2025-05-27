#11. Rotar los elementos de una lista n posiciones a la derecha.

def rotar_derecha(lista, k):
    k = k % len(lista)   #EL % es el resto de la lista
    return lista[-k:] + lista[:-k]# los suma como 2 grupos


mi_lista = [2,4,7,3,10,18,20,29,31,36,42,45,55,65,74,86,97]
k = 5  # Número de posiciones a rotar
resultado = rotar_derecha(mi_lista, k)
print(mi_lista)
print(resultado)  
