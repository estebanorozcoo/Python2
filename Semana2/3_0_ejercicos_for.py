#Contar del 1 al 10:
#Escribe un programa que use un for para imprimir los números del 1 al 10.

for i in range(1, 11):
    print(i)







#Contar hacia atrás:
#Usa un for para imprimir los números del 10 al 1 en orden descendente.

for i in range(10, 0, -1):
    print(i)







#Sumar los primeros 10 números:
#Usa un for para sumar los números del 1 al 10 e imprime el resultado.

suma = 0
for i in range(1, 11):
    suma += i
print("La suma de los primeros 10 números es:", suma)







#Números pares del 1 al 20:
#Usa un for y condicionales para imprimir solo los números pares del 1 al 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)







#Detectar múltiplos de 3:
#Escribe un programa que use un for y condicionales para imprimir los números del 1 al 30 que sean múltiplos de 3.

for i in range(1, 31):
    if i % 3 == 0:
        print(i)







#Contar letras "a":
#Pide al usuario una palabra y usa un for con un condicional para contar cuántas veces aparece la letra "a".

palabra = input("Introduce una palabra: ")
contador_a = 0
for letra in palabra:
    if letra == 'a' or letra == 'A':
        contador_a += 1
print("La letra 'a' aparece", contador_a, "veces.")







#Tabla de multiplicar del 5:
#Usa un for para imprimir la tabla de multiplicar del 5 (del 1 al 10).

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")







#Números positivos en una lista:
#Dada una lista de números (por ejemplo, [3, -1, 5, -2, 7, -8]), usa un for y condicionales para imprimir solo los positivos.

lista = [3, -1, 5, -2, 7, -8]
for num in lista:
    if num > 0:
        print(num)







#Mayúsculas y minúsculas:
#Pide al usuario una palabra y usa un for para contar cuántas letras son mayúsculas y cuántas son minúsculas.

palabra = input("Introduce una palabra: ")
mayusculas = 0
minusculas = 0
for letra in palabra:
    if letra.isupper():
        mayusculas += 1
    elif letra.islower():
        minusculas += 1
print(f"Mayúsculas: {mayusculas}, Minúsculas: {minusculas}")







#Simulación de contraseña:
#Pide al usuario que ingrese una contraseña e imprime "Acceso permitido" solo si la contraseña es "python123", 
#usando un for para simular tres intentos.

for intento in range(3):
    contrasena = input("Introduce la contraseña: ")
    if contrasena == "python123":
        print("Acceso permitido")
        break
    else:
        print("Contraseña incorrecta")
else:
    print("Has agotado los tres intentos.")
