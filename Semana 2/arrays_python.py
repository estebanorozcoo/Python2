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