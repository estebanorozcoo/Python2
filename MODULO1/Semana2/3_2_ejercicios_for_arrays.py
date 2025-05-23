#1 Invertir una lista:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4, 5]), usa un for para invertir la lista sin usar funciones incorporadas.

lista = [1, 2, 3, 4, 5]
invertida = []
for i in range(len(lista)-1, -1, -1):
    invertida.append(lista[i])
print(invertida)







#2 Eliminar los números negativos:
#Dada una lista de números (por ejemplo, [3, -1, 5, -2, 7]), usa un for para crear una nueva lista que contenga solo los números positivos.

numeros = [3, -1, 5, -2, 7]
positivos = []
for num in numeros:
    if num >= 0:
        positivos.append(num)
print(positivos)







#3 Encontrar la suma de los cuadrados:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4]), usa un for para calcular la suma de los cuadrados de los números en la lista.

numeros = [1, 2, 3, 4]
suma_cuadrados = 0
for num in numeros:
    suma_cuadrados += num ** 2
print(suma_cuadrados)








#4 Duplicar los valores de una lista:
#Dada una lista de números, usa un for para crear una nueva lista donde cada número sea el doble del valor original.

original = [1, 2, 3, 4]
duplicados = []
for num in original:
    duplicados.append(num * 2)
print(duplicados)







#5 Contar elementos específicos:
#Pide al usuario que ingrese un número y una lista. Usa un for para contar cuántas veces aparece el número ingresado en la lista.

numero = int(input("Ingresa el número a buscar: "))
lista = [int(x) for x in input("Ingresa una lista de números separados por espacio: ").split()]
contador = 0
for num in lista:
    if num == numero:
        contador += 1
print(f"El número {numero} aparece {contador} veces.")








#6 Eliminar duplicados de una lista:
#Dada una lista con elementos repetidos, usa un for para crear una nueva lista sin elementos duplicados.
lista = [1, 2, 2, 3, 4, 4, 5]
sin_duplicados = []
for elem in lista:
    if elem not in sin_duplicados:
        sin_duplicados.append(elem)
print(sin_duplicados)







#7 Generar una lista de múltiplos de un número:
#Pide al usuario un número N y usa un for para crear una lista con los primeros 10 múltiplos de N.
n = int(input("Ingresa un número: "))
multiplos = []
for i in range(1, 11):
    multiplos.append(n * i)
print(multiplos)








#8 Sumar los elementos en las posiciones pares:
#Dada una lista de números, usa un for para sumar los números que se encuentran en las posiciones pares (índices 0, 2, 4, etc.).

numeros = [10, 20, 30, 40, 50]
suma_pares = 0
for i in range(0, len(numeros), 2):
    suma_pares += numeros[i]
print(suma_pares)






#9 Filtrar cadenas con más de 5 caracteres:
#Dada una lista de cadenas de texto, usa un for para crear una nueva lista con solo aquellas cadenas que tengan más de 5 caracteres.
cadenas = ["hola", "programación", "Python", "sol", "computadora"]
filtradas = []
for texto in cadenas:
    if len(texto) > 5:
        filtradas.append(texto)
print(filtradas)







#10 Ordenar una lista de manera ascendente:
#Dada una lista de números, usa un for para ordenar la lista de menor a mayor sin utilizar las funciones sorted() o sort().

lista = [4, 2, 7, 1, 3]
# Método de burbuja
for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
print(lista)
