# 1. Pide dos números y muestra si el primero es mayor y distinto del segundo.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 > num2 and num1 != num2:
    print("El primero es mayor y distinto del segundo.")

# 2. Pide tres números y muestra si el primero es menor que el segundo y mayor que el tercero.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
if num1 < num2 and num1 > num3:
    print("El primero es menor que el segundo y mayor que el tercero.")

# 3. Pide una edad y muestra si está fuera del rango de 0 a 120.
edad = int(input("Ingresa una edad: "))
if edad < 0 or edad > 120:
    print("La edad está fuera del rango de 0 a 120.")

# 4. Pide un número y muestra si no es igual a 0 ni a 1.
num = int(input("Ingresa un número: "))
if num != 0 and num != 1:
    print("El número no es igual a 0 ni a 1.")

# 5. Pide dos textos y muestra si son exactamente iguales.
texto1 = input("Ingresa el primer texto: ")
texto2 = input("Ingresa el segundo texto: ")
if texto1 == texto2:
    print("Los textos son exactamente iguales.")

# 6. Pide un número y muestra si no es mayor que 100.
num = int(input("Ingresa un número: "))
if num <= 100:
    print("El número no es mayor que 100.")

# 7. Pide tres números y muestra si alguno de ellos es igual a 0.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
if num1 == 0 or num2 == 0 or num3 == 0:
    print("Alguno de los números es igual a 0.")

# 8. Pide un número y muestra si no está entre 10 y 20 (inclusive).
num = int(input("Ingresa un número: "))
if num < 10 or num > 20:
    print("El número no está entre 10 y 20 (inclusive).")

# 9. Pide dos números y muestra si el primero es mayor o igual que el segundo.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 >= num2:
    print("El primero es mayor o igual que el segundo.")

# 10. Pide una palabra y muestra si su longitud es menor o igual a 5 caracteres.
palabra = input("Ingresa una palabra: ")
if len(palabra) <= 5:
    print("La longitud de la palabra es menor o igual a 5 caracteres.")

# 11. Pide una calificación del 0 al 10 y muestra si es válida (entre 0 y 10, sin incluir extremos).
calificacion = int(input("Ingresa una calificación (entre 0 y 10): "))
if 0 < calificacion < 10:
    print("La calificación es válida.")

# 12. Pide una edad y muestra si es mayor de 17 y menor de 66.
edad = int(input("Ingresa una edad: "))
if 17 < edad < 66:
    print("La edad es mayor de 17 y menor de 66.")

# 13. Pide dos números y muestra si no son iguales y el primero es mayor que 5.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 != num2 and num1 > 5:
    print("Los números no son iguales y el primero es mayor que 5.")

# 14. Pide tres números y muestra si todos son diferentes.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))
if num1 != num2 and num1 != num3 and num2 != num3:
    print("Todos los números son diferentes.")

# 15. Pide un número decimal y muestra si es negativo o mayor que 100.
num = float(input("Ingresa un número decimal: "))
if num < 0 or num > 100:
    print("El número es negativo o mayor que 100.")

# 16. Pide una temperatura y muestra si no es inferior a 0 ni superior a 35.
temperatura = float(input("Ingresa una temperatura: "))
if 0 <= temperatura <= 35:
    print("La temperatura no es inferior a 0 ni superior a 35.")

# 17. Pide dos edades y muestra si alguna es menor que 18 y la otra mayor que 60.
edad1 = int(input("Ingresa la primera edad: "))
edad2 = int(input("Ingresa la segunda edad: "))
if (edad1 < 18 and edad2 > 60) or (edad2 < 18 and edad1 > 60):
    print("Una edad es menor que 18 y la otra es mayor que 60.")

# 18. Pide una letra y muestra si no es igual a "a", "e", "i", "o" ni "u".
letra = input("Ingresa una letra: ").lower()
if letra not in ['a', 'e', 'i', 'o', 'u']:
    print("La letra no es igual a 'a', 'e', 'i', 'o' ni 'u'.")

# 19. Pide dos números y muestra si el primero no es múltiplo del segundo.
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
if num1 % num2 != 0:
    print("El primero no es múltiplo del segundo.")

# 20. Pide un número y muestra si es igual a 0, o si es mayor que 10 y menor que 20.
num = int(input("Ingresa un número: "))
if num == 0 or (num > 10 and num < 20):
    print("El número es igual a 0, o es mayor que 10 y menor que 20.")
