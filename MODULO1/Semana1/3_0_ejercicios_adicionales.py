# 1. Calculadora de promedio con validación
# Pide al usuario 3 notas (entre 0 y 10).  
# Si alguna nota está fuera del rango, muestra un mensaje de error. 
# Si todas son válidas, calcula el promedio y muestra si el estudiante aprueba (≥ 6) o reprueba.

print("1. Calculadora de promedio con validación")
notas = []
for i in range(1, 4):
    nota = float(input(f"Ingrese la nota {i} (0 a 10): "))
    if nota < 0 or nota > 10:
        print("Error: La nota debe estar entre 0 y 10.")
        break
    notas.append(nota)
else:
    promedio = sum(notas) / 3
    print(f"Promedio: {promedio:.2f}")
    if promedio >= 6:
        print("Resultado: Aprobado")
    else:
        print("Resultado: Reprobado")

# 2. Años para jubilarse
# Pide la edad y el género del usuario ("M" para mujer, "H" para hombre).
# Mujer se jubila a los 60 años / Hombre se jubila a los 65 años
# Si ya se puede jubilar, muestra un mensaje celebratorio. 
# Si no, indica cuántos años faltan para la jubilación.

print("\n2. Años para jubilarse")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese su género (M para mujer, H para hombre): ").upper()
if genero == "M":
    retiro = 60
elif genero == "H":
    retiro = 65
else:
    print("Género no válido.")
    retiro = None

if retiro:
    if edad >= retiro:
        print("¡Ya puedes jubilarte!")
    else:
        print(f"Te faltan {retiro - edad} años para jubilarte.")

# 3. Calculadora de salario neto
# Pide: Sueldo bruto y Porcentaje de descuento
# Calcula el sueldo neto con: sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)

print("\n3. Calculadora de salario neto")
sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)
print(f"Sueldo bruto: {sueldo_bruto}")
print(f"Descuento: {descuento}%")
print(f"Sueldo neto: {sueldo_neto}")

# 4. ¿Compatibles?
# Pide nombre y edad de dos personas. Verifica si:
# Ambos tienen al menos 18 años, se llaman distinto, y la diferencia de edad no supera los 10 años.
# Si cumplen todo, imprime que son compatibles.

print("\n4. ¿Compatibles?")
nombre1 = input("Nombre de la primera persona: ")
edad1 = int(input("Edad de la primera persona: "))
nombre2 = input("Nombre de la segunda persona: ")
edad2 = int(input("Edad de la segunda persona: "))

if edad1 < 18 or edad2 < 18:
    print("Uno o ambos son menores de edad.")
elif nombre1 == nombre2:
    print("Tienen el mismo nombre.")
elif abs(edad1 - edad2) > 10:
    print("La diferencia de edad es mayor a 10 años.")
else:
    print("¡Son compatibles! Cupido estaría orgulloso")

# 5. Calculadora de múltiplos
# Pide dos números y verifica si el primero es múltiplo del segundo usando %.

print("\n5. Calculadora de múltiplos")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
es_multiplo = num1 % num2 == 0
print(f"{num1} es múltiplo de {num2} → {es_multiplo}")

# 6. Número mágico
# Pide un número y responde según su divisibilidad por 3 y 5.

print("\n6. Número mágico")
numero = int(input("Ingrese un número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print("Nada mágico")

# 7. Conversor de unidades avanzado
# Pide una cantidad en kilómetros y convierte a metros, centímetros y milímetros.
# Muestra todo en una sola línea.

print("\n7. Conversor de unidades avanzado")
km = float(input("Ingrese la cantidad en kilómetros: "))
metros = km * 1000
cm = km * 100000
mm = km * 1000000
print(f"{km} km = {metros} metros, {cm} cm, {mm} mm")
