print("=== Desafío de Calificaciones y Estadísticas ===\n") 

# 1. Ingreso y validación de una calificación individual
while True:
    try:
        calificacion = int(input("Ingresa una calificación individual (0-100): "))
        if 0 <= calificacion <= 100:
            break
        else:
            print("Debe ser un número entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

# 2. Determinar si aprueba o reprueba
if calificacion >= 60:
    print("¡Aprobado!")
else:
    print("Reprobado.")

# 3. Ingreso de una lista de calificaciones
while True:
    entrada = input("\nIngresa una lista de calificaciones separadas por comas (ej: 70,80,90): ")
    try:
        lista = [int(x.strip()) for x in entrada.split(",")]
        if all(0 <= x <= 100 for x in lista):
            break
        else:
            print("Todas las calificaciones deben estar entre 0 y 100.")
    except ValueError:
        print("Asegúrate de ingresar solo números enteros separados por comas.")

# 4. Calcular el promedio
suma = 0
for nota in lista:
    suma += nota
promedio = suma / len(lista)
print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")

# 5. Contar cuántas calificaciones son mayores que un valor dado
while True:
    try:
        valor = int(input("\nIngresa un valor para comparar (0-100): "))
        if 0 <= valor <= 100:
            break
        else:
            print("Ingresa un valor entre 0 y 100.")
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")

contador_mayores = 0
i = 0
while i < len(lista):
    if lista[i] > valor:
        contador_mayores += 1
    i += 1
print(f"Hay {contador_mayores} calificaciones mayores que {valor}.")

# 6. Verificar si una calificación específica está en la lista y cuántas veces aparece
while True:
    try:
        valor_especifico = int(input("\nIngresa una calificación específica para buscar: "))
        if 0 <= valor_especifico <= 100:
            break
        else:
            print("Debe estar entre 0 y 100.")
    except ValueError:
        print("Entrada inválida.")

conteo = 0
for cal in lista:
    if cal == valor_especifico:
        conteo += 1
        continue  # Si se encuentra, cuenta y continúa
    if cal > 100:
        break  # Aunque no debe ocurrir, añadimos una ruptura como ejemplo

if conteo > 0:
    print(f"La calificación {valor_especifico} aparece {conteo} veces.")
else:
    print(f"La calificación {valor_especifico} no se encuentra en la lista.")
