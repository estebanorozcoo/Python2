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