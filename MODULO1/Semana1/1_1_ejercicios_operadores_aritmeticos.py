# 1. Intercambio de variables
# Pide dos valores al usuario e imprime los valores intercambiados.

print("1. Intercambio de variables")
a = input("Ingrese el valor de a: ")
b = input("Ingrese el valor de b: ")
a, b = b, a
print("Valores intercambiados → a =", a, ", b =", b)

# 2. Inverso de número de tres cifras
# Pide un número de tres cifras y muestra sus cifras en orden inverso (ej. 123 → 321).

print("\n2. Inverso de número de tres cifras")
numero = int(input("Ingrese un número de tres cifras: "))
c = numero // 100
d = (numero // 10) % 10
u = numero % 10
inverso = u * 100 + d * 10 + c
print("Número invertido:", inverso)

# 3. Extraer hora, minuto y segundo de segundos totales
# Pide segundos totales y muestra cuántas horas, minutos y segundos son.

print("\n3. Extraer hora, minuto y segundo de segundos totales")
total_segundos = int(input("Ingrese los segundos totales: "))
horas = total_segundos // 3600
minutos = (total_segundos % 3600) // 60
segundos = total_segundos % 60
print(f"{horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)")

# 4. Fecha formateada
# Pide día, mes y año por separado e imprime en formato "DD/MM/AAAA" y "AAAA-MM-DD"

print("\n4. Fecha formateada")
dia = input("Día: ")
mes = input("Mes: ")
anio = input("Año: ")
print(f"Formato DD/MM/AAAA: {dia.zfill(2)}/{mes.zfill(2)}/{anio}")
print(f"Formato AAAA-MM-DD: {anio}-{mes.zfill(2)}-{dia.zfill(2)}")

# 5. 🌡 Convertir temperatura (F → C)
# Pide una temperatura en Fahrenheit y muestra el equivalente en Celsius.

print("\n5. 🌡 Convertir temperatura (F → C)")
f = float(input("Temperatura en Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f"Equivalente en Celsius: {c:.2f}°C")

# 6. Cálculo de propina y cuenta total
# Pide el costo de una comida y calcula 10%, 15% y 20% de propina.

print("\n6. Cálculo de propina y cuenta total")
costo = float(input("Costo de la comida: "))
for porcentaje in [10, 15, 20]:
    propina = costo * porcentaje / 100
    total = costo + propina
    print(f"Propina {porcentaje}%: ${propina:.2f} → Total: ${total:.2f}")

# 7. Extraer dígitos de un número de 4 cifras
# Pide un número de 4 cifras e imprime cada dígito separado por coma.

print("\n7. Extraer dígitos de un número de 4 cifras")
numero = int(input("Ingrese un número de 4 cifras: "))
mil = numero // 1000
cen = (numero // 100) % 10
dec = (numero // 10) % 10
uni = numero % 10
print(f"Dígitos: {mil}, {cen}, {dec}, {uni}")

# 8. Formato de precio con dos decimales
# Pide un precio (float) y muestra el resultado con dos decimales y símbolo de moneda.

print("\n8. Formato de precio con dos decimales")
precio = float(input("Ingrese el precio: "))
print(f"Precio formateado: ${precio:.2f}")

# 9. Conversor de minutos a días y horas
# Pide una cantidad de minutos y muestra días, horas y minutos.

print("\n9. Conversor de minutos a días y horas")
minutos = int(input("Ingrese la cantidad de minutos: "))
dias = minutos // 1440
horas = (minutos % 1440) // 60
resto_min = minutos % 60
print(f"{dias} día(s), {horas} hora(s), {resto_min} minuto(s)")

# 10. Área y perímetro de un círculo
# Pide el radio de un círculo y muestra área y perímetro. Usa pi = 3.1416

print("\n10. Área y perímetro de un círculo")
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416
area = pi * radio ** 2
perimetro = 2 * pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")
