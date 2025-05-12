#1 Imprimir caracteres de una cadena:
#Pide al usuario una cadena y usa un for para imprimir cada carácter de la cadena en una línea separada.

cadena = input("Escribe una cadena: ")
for caracter in cadena:
    print(caracter)







#2 Sumar los números en una lista:
#Dada una lista de números (por ejemplo, [1, 2, 3, 4, 5]), usa un for para sumar todos los números e imprimir el resultado.

numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero
print("La suma es:", suma)






#3 Números impares del 1 al 30:
#Usa un for y un condicional para imprimir solo los números impares del 1 al 30.

for i in range(1, 31):
    if i % 2 != 0:
        print(i)







#4Encontrar la letra más frecuente:
#Pide al usuario una palabra y usa un for para encontrar cuál es la letra que más veces se repite en la palabra.

palabra = input("Escribe una palabra: ")
frecuencia = {}
for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] += 1
    else:
        frecuencia[letra] = 1

letra_frecuente = max(frecuencia, key=frecuencia.get)
print(f"La letra más frecuente es '{letra_frecuente}' con {frecuencia[letra_frecuente]} apariciones.")







#5 Verificar si un número es primo:
#Escribe un programa que pida un número y use un for para determinar si el número es primo (sin usar la función isprime()).

numero = int(input("Escribe un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print("Es un número primo.")
else:
    print("No es un número primo.")







#6 Sumar números negativos:
#Dada una lista de números (por ejemplo, [4, -2, -6, 7, -3]), usa un for para sumar solo los números negativos e imprimir el resultado.

numeros = [4, -2, -6, 7, -3]
suma_negativos = 0
for n in numeros:
    if n < 0:
        suma_negativos += n
print("Suma de números negativos:", suma_negativos)







#7 Contar palabras con más de 3 letras:
#Pide al usuario una oración y usa un for con un condicional para contar cuántas palabras tienen más de 3 letras.


oracion = input("Escribe una oración: ")
palabras = oracion.split()
contador = 0
for palabra in palabras:
    if len(palabra) > 3:
        contador += 1
print("Número de palabras con más de 3 letras:", contador)







#8 Imprimir los primeros N números:
#Pide al usuario un número N y usa un for para imprimir los primeros N números enteros.

N = int(input("¿Cuántos números quieres imprimir?: "))
for i in range(N):
    print(i)







#9 Número mayor en una lista:
#Dada una lista de números (por ejemplo, [10, 2, 30, 4]), usa un for para encontrar el número mayor.

numeros = [10, 2, 30, 4]
mayor = numeros[0]
for n in numeros:
    if n > mayor:
        mayor = n
print("El número mayor es:", mayor)







#10Divisores de un número:
#Pide al usuario un número y usa un for para imprimir todos sus divisores (excepto el número en sí).

numero = int(input("Escribe un número: "))
print(f"Divisores de {numero} (sin incluir el mismo):")
for i in range(1, numero):
    if numero % i == 0:
        print(i)
