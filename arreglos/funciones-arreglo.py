
#Estos son arreglos/listas en python
lista = [1, 2, 3, 4, 5]
lista1 = [1, 2, 3, 4, 7]
lista.append(0) #Se agrega un elemento al ultimo lugar/final de la lista
print(lista)

lista.extend(lista) # agregar una lista 
print(lista)

lista = lista[::-1] #invertir una lista
print(lista)

lista.reverse() #Invertir una lista
print(lista)

lista.insert(0, 10) #Agregar un elemento en una posición especifica (0,10)
lista.insert(5, 11) #Posicion, Elemento
print(lista)


lista1.remove(2) #Elimina un elemento de la lista
print(lista1)

print(lista1.pop(1)) #Elimina un elemento y lo imprime
print(lista1)

print(lista1.count(7)) #Cuenta la cantidad de veces que aparece un elemento en la lista

lista3 =[1, 2, 3, 4, 5]
print(lista3.index(4)) #Devuelve la posición de un elemento de la lista

lista.sort() #Ordena la lista
print(lista)
lista.sort(reverse=True) #Ordena Descendente de la lista
print(lista)

lista4 =lista.copy() #Copiar una lista , Es una copia Superficial
print(lista4)

lista.clear()
print(lista)

lista5 = [] #Crear una lista vacia
print(lista5)