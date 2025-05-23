# 1. Acceso exclusivo al evento
# Edad > 21 y número de invitación == 777

print("1. Acceso exclusivo al evento")
edad = int(input("Ingrese su edad: "))
invitacion = int(input("Ingrese su número de invitación: "))
acceso = edad > 21 and invitacion == 777
print("¿Puede ingresar al evento?:", acceso)

# 2. Descuento por edad o monto
# monto > 100 o edad > 60

print("\n2. Descuento por edad o monto")
monto = float(input("Ingrese el monto de la compra: "))
edad = int(input("Ingrese su edad: "))
descuento = monto > 100 or edad > 60
print("¿Obtiene descuento?:", descuento)

# 3. Verificación para participar en un concurso internacional
# edad entre 18 y 30, país distinto de Antártida y documento distinto de 0

print("\n3. Participación en concurso internacional")
edad = int(input("Edad: "))
pais = input("País: ")
documento = int(input("Número de documento: "))
puede_participar = (18 <= edad <= 30) and (pais.lower() != "antártida") and (documento != 0)
print("¿Cumple condiciones?:", puede_participar)

# 4. Evaluación académica de estudiante
# Ambas notas ≥ 6 y ninguna < 4

print("\n4. Evaluación académica")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
aprobo = (nota1 >= 6 and nota2 >= 6) and (nota1 >= 4 and nota2 >= 4)
print("¿Estudiante aprobado?:", aprobo)

# 5. Conexión segura en la red
# protocolo == "https" y puerto == 443

print("\n5. Conexión segura")
protocolo = input("Protocolo (http/https): ")
puerto = input("Puerto: ")
segura = protocolo == "https" and puerto == "443"
print("¿Conexión segura?:", segura)

# 6. Requisitos para obtener una beca
# promedio ≥ 8, materias < 3, ingresos ≤ 1500

print("\n6. Beca")
promedio = float(input("Promedio: "))
materias = int(input("Cantidad de materias: "))
ingresos = float(input("Ingresos mensuales: "))
beca = promedio >= 8 and materias < 3 and ingresos <= 1500
print("¿Aplica para beca?:", beca)

# 7. Acceso a atracción en parque temático
# estatura > 140 y edad entre 10 y 60

print("\n7. Acceso a atracción")
estatura = int(input("Estatura en cm: "))
edad = int(input("Edad: "))
puede_subir = estatura > 140 and 10 <= edad <= 60
print("¿Puede acceder a la atracción?:", puede_subir)

# 8. Validación de contraseña segura
# longitud ≥ 8 y no contiene "123"

print("\n8. Contraseña segura")
clave = input("Ingrese una contraseña: ")
segura = len(clave) >= 8 and "123" not in clave
print("¿Contraseña segura?:", segura)

# 9. Evaluación para tarjeta de crédito
# ingresos > 2500 o (ingresos > 1500 y sin deudas)

print("\n9. Evaluación para tarjeta de crédito")
ingresos = float(input("Ingresos mensuales: "))
deuda = input("¿Tiene deudas activas? (sí/no): ").lower()
aplica_tarjeta = ingresos > 2500 or (ingresos > 1500 and deuda != "sí")
print("¿Puede obtener tarjeta de crédito?:", aplica_tarjeta)

# 10. Horario permitido para clases
# hora entre 8 y 18, excepto 13

print("\n10. Horario permitido para clases")
hora = int(input("Ingrese la hora del día (0-23): "))
horario_valido = 8 <= hora <= 18 and hora != 13
print("¿Horario permitido?:", horario_valido)
