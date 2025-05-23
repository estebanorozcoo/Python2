#Contar del 1 al 10:
#Usa un while para imprimir los números del 1 al 10.

contador = 1

while contador <=10:
    print (contador)
    contador += 1








#Contar hacia atrás:
#Usa un while para imprimir los números del 10 al 1 en orden descendente.

contador = 10

while contador >=1:
    print (contador)
    contador -=1








#Suma de los primeros 10 números:
#Usa un while para sumar los números del 1 al 10 e imprimir el resultado.

contador = 1
suma = 0

while contador <=10:
    suma += contador
    contador += 1
print ("la suma del 1 al 10:", suma)








#Solicitar número positivo:
#Pide al usuario un número y usa un while para seguir pidiendo hasta que ingrese un número positivo.

numero1 = int(input("Ingresa un numero: "))

while numero1 <= 0:
    print ("Este numero no es correcto. Ingresa otro numero")
    numero1 = int(input("Ingresa un numero: "))
print (f"¡Gracias! el numero {numero1} que ingreso es correcto")








#Menú interactivo:
#Crea un menú con while que permita al usuario elegir entre opciones 
#(por ejemplo, "1. Saludar", "2. Despedirse", "3. Salir") y solo termine cuando elija la opción de salir.

def menu_interactivo():
    while True:
        print("\n--- Menú Interactivo ---")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            print("¡Hola! ¿Cómo estás?")
        elif opcion == "2":
            print("¡Hasta luego! Que tengas un buen día.")
        elif opcion == "3":
            print("Saliendo del programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")

# Ejecutar el menú
menu_interactivo()








#Adivina el número:
#Genera un número secreto (puedes usar una variable fija) y usa un while 
#para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor.

# Número secreto fijo
numero_secreto = 42

print("¡Bienvenido al juego de Adivina el Número!")
print("Estoy pensando en un número entre 1 y 100.")

# Inicializamos la variable
intento = None

# Bucle para seguir pidiendo al usuario hasta que adivine
while intento != numero_secreto:
    try:
        intento = int(input("Adivina el número: "))
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta con un número más alto.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta con un número más bajo.")
        else:
            print("¡Felicidades! Has adivinado el número.")
    except ValueError:
        print("Por favor, ingresa un número válido.")









#Contar vocales en una palabra:
#Pide al usuario una palabra y usa un while para contar cuántas vocales tiene.

# Solicitar palabra al usuario
palabra = input("Ingresa una palabra: ").lower()

# Inicializar variables
indice = 0
contador_vocales = 0
vocales = "aeiou"

# Recorrer la palabra con un while
while indice < len(palabra):
    if palabra[indice] in vocales:
        contador_vocales += 1
    indice += 1

# Mostrar resultado
print(f"La palabra '{palabra}' tiene {contador_vocales} vocales.")








#Validar contraseña:
#Pide al usuario una contraseña y usa un while para seguir pidiendo hasta que ingrese "python123".

# Contraseña correcta
clave_correcta = "python123"

# Solicitar contraseña al usuario
contraseña = input("Ingresa la contraseña: ")

# Bucle hasta que la contraseña sea correcta
while contraseña != clave_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contraseña = input("Ingresa la contraseña: ")

print("¡Acceso concedido!")









#Sumar hasta detenerse:
#Pide números al usuario y súmalos hasta que ingrese "0", momento en el que se imprimirá el total.

# Inicializar la suma
suma_total = 0

print("Ingresa números para sumarlos. Escribe '0' para terminar.")

# Bucle para pedir números y sumarlos
numero = int(input("Ingresa un número: "))
while numero != 0:
    suma_total += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

# Mostrar el resultado final
print(f"La suma total es: {suma_total}")










#Número de intentos:
#Pide al usuario que ingrese un número entre 1 y 10. Si no lo hace, sigue pidiéndolo hasta que lo haga correctamente.

# Bucle hasta que el usuario ingrese un número entre 1 y 10
while True:
    try:
        numero = int(input("Ingresa un número entre 1 y 10: "))
        if 1 <= numero <= 10:
            print(f"¡Gracias! Has ingresado el número {numero}.")
            break  # Sale del bucle si el número es correcto
        else:
            print("El número debe estar entre 1 y 10. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
