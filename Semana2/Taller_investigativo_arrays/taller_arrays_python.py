#EJERCICIOS ARRAYS PYTHON
#EJEMPLO PRACTICO 1
mi_lista = [1, 2, 3, 4, 5]
print ("Mi lista", mi_lista)


#EJEMPLO PRACTICO 2
numeros = [10, 20, 30, 40]
# Primer elemento: 10
print ("Primer numero", numeros[0])
# Último elemento: 40
print ("Ultimo elemento", numeros [-1])

#EJEMPLO PRACTICO 3
lista2 = [10,20,30,40,50]
#[20,30,40]
print ("Los elementos del índice 1 al 3", lista2 [1:4]) 
#[10,20,30]
print ("Los primeros 3 elementos", lista2 [:3])
#[30,40,50]
print ("Los elementos desde el índice 2 hasta el final", lista2 [2:])

#EJEMPLO PRACTICO 4
lista3 = [10,20,30,40]
lista3[2] = 99
#[10,20,99,40]
print ("Se cambio el tercer elemento de la lista por el numero 99", lista3)

#EJERCICIO PRACTICO 5
lista4 = [10,20,30]
lista4_1 = [10,20,30]
lista4_1.append(40)
lista4_2 = [10,20,30,40]
lista4_2.insert(0,15)
lista4_3 = [15,20,30,40]
lista4_3 += [50,60]
print ("Lista inicial", lista4)
print ("Agregar el número 40 al final", lista4_1)
print ("Agregar el número 15 en la posición 1", lista4_2)
print ("Agregar los números 50 y 60 al final de la lista", lista4_3)

#EJERCICIO PRACTICO 6
lista5 = [10, 20, 30, 40, 50]
lista5_1 = [10, 20, 30, 40, 50]
lista5_1.remove (30)
lista5_2 = [10, 20, 40, 50]
lista5_2.pop()
lista5_3 = [10, 20, 40,]
lista5_3.pop(1)
print ("Lista inicial", lista5)
print ("Elimina el número 30", lista5_1)
print ("Elimina el último elemento", lista5_2)
print ("Elimina el segundo elemento", lista5_3)

#EJERCICIO PRACTICO 7
lista6 = [10, 20, 30, 40, 50]
#Verifica si el número 20 está en la lista
print (20 in lista6)
#Encuentra el índice del número 30
print (lista6.index(30))
#Cuenta cuántas veces aparece el número 20
print (lista6.count(20))

#EJERCICIO PRACTICO 8
lista7 = [40, 10, 30, 20]
print("Lista original", lista7)
#Orden ascendente
lista7.sort()
print("Lista odenada", lista7)
#Orden descendente
lista7.sort(reverse=True)
print("Lista en orden desendente", lista7)
#Lista ordenada sin modificar la original.
lista_ordenada =  sorted(lista7)
print("Lista ordenada sin modificar la original", lista_ordenada)

#EJERCICIO PRACTICO 9
lista8 = [10, 20, 30, 40]
lista8.reverse()
print("Invertir una lista usando reverse()", lista8)
lista_invertida = lista8[::-1]
print ("Invertir una lista usando slicing", lista_invertida)

#EJERCICIO PRACTICO 10
lista9 = [10, 20, 30]
#copiar una lista usando slicing
Lista_slicing = lista9 [:]
# copiarla una lista usando list()
lista_list = list(lista9)
#opiarla usando copy()
lista_copy = lista9.copy()
print ("lista usando slicing", Lista_slicing)
print ("lista usando list()", lista_list)
print ("lista usando Copy()", lista_copy)

#EJERCICIO PRACTICO 10
lista_vacia = []
#Lista vacía y escribe "La lista está vacía" si no contiene datos.
if not lista_vacia:
    print ("La lista está vacía")
else:
    print ("La lista tiene elementos")