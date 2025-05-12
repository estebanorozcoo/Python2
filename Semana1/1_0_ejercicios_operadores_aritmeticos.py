# 1. Nombre y edad
# Pide al usuario su nombre y edad, y muestra un mensaje que diga: "Hola [nombre], tienes [edad] años."
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
print(f"Hola {nombre}, tienes {edad} años.")

# 2. Suma de dos números enteros
# Pide dos números enteros y muestra la suma de ambos.
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
print("La suma es:", a + b)

# 3. Multiplicación de decimales
# Pide dos números decimales (float) y muestra su multiplicación.
x = float(input("Ingresa el primer número decimal: "))
y = float(input("Ingresa el segundo número decimal: "))
print("El producto es:", x * y)

# 4. Doble y triple
# Pide un número entero y muestra el doble y el triple de ese número, separados por coma.
n = int(input("Ingresa un número entero: "))
print("Doble y triple:", n * 2, ",", n * 3)

# 5. Repetir palabra
# Pide al usuario una palabra y un número entero. Muestra la palabra repetida ese número de veces.
palabra = input("Escribe una palabra: ")
veces = int(input("¿Cuántas veces deseas repetirla? "))
print(palabra * veces)

# 6. División
# Pide al usuario dos números y muestra el resultado de dividir el primero entre el segundo.
num1 = float(input("Ingresa el dividendo: "))
num2 = float(input("Ingresa el divisor: "))
print("Resultado de la división:", num1 / num2)

# 7. Letras del nombre
# Pide al usuario su nombre y muestra cuántas letras tiene.
nombre = input("Escribe tu nombre: ")
print("Tu nombre tiene", len(nombre), "letras.")

# 8. División entera y módulo
# Pide al usuario dos números y muestra la división entera (//) y el módulo (%) entre ellos.
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("División entera:", a // b, ", Módulo:", a % b)

# 9. Todas las operaciones
# Pide al usuario dos números y muestra: suma, resta, multiplicación y división, separadas por coma.
x = float(input("Primer número: "))
y = float(input("Segundo número: "))
print("Suma:", x + y, ", Resta:", x - y, ", Multiplicación:", x * y, ", División:", x / y)

# 10. Potencias con f-strings
# Pide un número entero y muestra el número elevado a la 2 y a la 3 usando f-strings.
n = int(input("Ingresa un número entero: "))
print(f"{n} al cuadrado es {n**2} y al cubo es {n**3}")

# 11. Parte entera de un decimal
# Pide al usuario un número decimal y muestra solo la parte entera.
decimal = float(input("Ingresa un número decimal: "))
print("Parte entera:", int(decimal))

# 12. Mayor de edad (sin condicional)
# Pide la edad del usuario y muestra si es mayor de 18 (solo usando comparación).
edad = int(input("Ingresa tu edad: "))
print("Mayor de edad:", edad >= 18)

# 13. ¿Son iguales?
# Pide dos números enteros y muestra si son iguales (usar ==).
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("¿Son iguales?", a == b)

# 14. ¿Mayor que?
# Pide dos números y muestra si el primero es mayor que el segundo.
x = float(input("Primer número: "))
y = float(input("Segundo número: "))
print("¿El primero es mayor que el segundo?", x > y)

# 15. ¿Menor o igual?
# Pide dos números y muestra si el primero es menor o igual que el segundo.
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
print("¿El primero es menor o igual que el segundo?", a <= b)

# 16. Ambos mayores que 10
# Pide dos números y muestra si ambos son mayores que 10 (usar and).
x = int(input("Primer número: "))
y = int(input("Segundo número: "))
print("¿Ambos mayores que 10?", x > 10 and y > 10)

# 17. Al menos uno mayor que 10
# Pide dos números y muestra si al menos uno es mayor que 10 (usar or).
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("¿Al menos uno es mayor que 10?", a > 10 or b > 10)

# 18. No son iguales
# Pide dos números y muestra si el primero no es igual al segundo (usar not y ==).
x = int(input("Primer número: "))
y = int(input("Segundo número: "))
print("¿No son iguales?", not (x == y))

# 19. Promedio
# Pide tres números, calcula el promedio y muestra el resultado.
n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = (n1 + n2 + n3) / 3
print("Promedio:", promedio)

# 20. Divisible por 5
# Pide un número entero y muestra si es divisible entre 5 (usar % y ==).
numero = int(input("Ingresa un número entero: "))
print("¿Es divisible entre 5?", numero % 5 == 0)
