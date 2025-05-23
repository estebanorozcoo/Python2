#1️ Sistema de recomendaciones de películas 
#Crea un programa que recomiende una película basada en la edad del usuario y sus preferencias (acción, comedia, terror, etc.).
#Si el usuario es menor de 13 años, evita películas con clasificación para adultos.

def recomendar_pelicula(edad, genero):
    if edad < 13:
        if genero in ['acción', 'terror']:
            return "Recomiendo una película de animación o aventura."
        else:
            return f"Te recomiendo una película de {genero} adecuada para tu edad."
    else:
        match genero:
            case 'acción':
                return "Recomiendo una película de acción emocionante."
            case 'comedia':
                return "Recomiendo una comedia divertida."
            case 'terror':
                return "Recomiendo una película de terror para adultos."
            case _:
                return "Recomiendo una película variada según tus gustos."







#2️ Asistente de productividad
#Diseña un asistente que, según la hora actual y si es un día laboral o fin de semana, sugiera actividades como:
# "trabajar"
# "descansar"
# "hacer ejercicio"
#Asegúrate de que los datos sean flexibles para futuras mejoras.

from datetime import datetime

def sugerir_actividad():
    hora_actual = datetime.now().hour
    dia_actual = datetime.now().weekday()  # 0 = lunes, 6 = domingo

    if dia_actual < 5:  # Día laboral
        if 9 <= hora_actual < 12:
            return "Es hora de trabajar."
        elif 12 <= hora_actual < 14:
            return "Es hora de descansar y almorzar."
        elif 14 <= hora_actual < 18:
            return "Es hora de seguir trabajando."
        else:
            return "Es hora de descansar."
    else:  # Fin de semana
        if 9 <= hora_actual < 12:
            return "Es hora de hacer ejercicio."
        else:
            return "Es hora de descansar y disfrutar."







#3️ Control de acceso con doble autenticación 
#Crea un sistema de inicio de sesión que solicite usuario y contraseña.
# Si la contraseña es correcta, debe solicitar un código de verificación (simulado).
# El acceso solo se concede si ambas verificaciones son correctas.

def acceso_sistema():
    usuario = input("Ingresa tu usuario: ")
    contraseña = input("Ingresa tu contraseña: ")
    
    if contraseña == "contraseña_correcta":
        codigo_verificacion = input("Ingresa el código de verificación: ")
        if codigo_verificacion == "123456":
            return "Acceso concedido"
        else:
            return "Código incorrecto"
    else:
        return "Contraseña incorrecta"







#4️ Calculadora de presupuesto mensual 
#Desarrolla un programa que pida ingresos y gastos fijos del usuario.
# Luego, evalúa si puede ahorrar dinero y cuánto, o si necesita reducir gastos.
# Aplica buenas prácticas como modularidad y validaciones.

def calculadora_presupuesto():
    ingresos = float(input("Ingresa tus ingresos mensuales: "))
    gastos_fijos = float(input("Ingresa tus gastos fijos mensuales: "))
    
    saldo = ingresos - gastos_fijos
    if saldo > 0:
        return f"Puedes ahorrar {saldo}."
    elif saldo == 0:
        return "No tienes ahorro, pero no tienes deuda."
    else:
        return f"Necesitas reducir tus gastos en {-saldo}."








#5️ Asistente de clima y vestimenta 
#Crea un programa que pida la temperatura y si está lloviendo o no.
#Según los datos, sugiere qué ropa usar: abrigo, paraguas, ropa ligera, etc.
#Hazlo reutilizable para futuras ampliaciones.

def sugerir_ropa(temperatura, lloviendo):
    if temperatura < 15:
        if lloviendo:
            return "Lleva un abrigo y paraguas."
        else:
            return "Lleva un abrigo."
    elif 15 <= temperatura <= 25:
        if lloviendo:
            return "Lleva ropa ligera y paraguas."
        else:
            return "Lleva ropa ligera."
    else:
        if lloviendo:
            return "Lleva ropa ligera y paraguas."
        else:
            return "Lleva ropa ligera y cómoda."







#6️ Sistema de registro de eventos con validación 
#Construye un programa que permita registrar asistentes a un evento.
#El sistema debe verificar que:
#La edad del usuario sea adecuada
#No se haya superado el límite de cupos disponibles

def registrar_evento():
    edad = int(input("Ingresa tu edad: "))
    cupos_disponibles = 100
    asistentes = 90

    if edad < 18:
        return "No puedes asistir, eres menor de edad."
    elif asistentes >= cupos_disponibles:
        return "El evento está lleno."
    else:
        return "Registrado exitosamente al evento."







#7️ Detector de spam en correos electrónicos 
#Simula un sistema que detecte si un mensaje es spam.
# Usa condiciones para verificar si el mensaje contiene palabras como:
#"gratis",
#"gana dinero",
#"descuento exclusivo", etc.
#Si hay coincidencias, márcalo como spam.

def detectar_spam(mensaje):
    spam_keywords = ["gratis", "gana dinero", "descuento exclusivo"]
    if any(keyword in mensaje.lower() for keyword in spam_keywords):
        return "Este mensaje es spam."
    else:
        return "Este mensaje no es spam."







#8️ Sistema de préstamos de biblioteca 
#Desarrolla un programa que permita a un usuario solicitar un libro.
#Solo puede hacerlo si:
#Tiene menos de 3 libros prestados
#No tiene sanciones pendientes

def prestamo_libro(libros_prestados, sanciones_pendientes):
    if libros_prestados < 3 and not sanciones_pendientes:
        return "Puedes solicitar el libro."
    elif libros_prestados >= 3:
        return "No puedes solicitar más libros, ya tienes 3 prestados."
    else:
        return "Tienes sanciones pendientes, no puedes solicitar el libro."








#9️ Asistente de compras inteligentes 
#Crea un sistema que ayude al usuario a decidir si comprar un producto.
#Pide:
#Precio del producto
#Si hay descuentos
#Presupuesto del usuario
#Luego indica si la compra es recomendable o no.

def compra_inteligente(precio, descuento, presupuesto):
    precio_final = precio - (precio * descuento)
    if precio_final <= presupuesto:
        return "La compra es recomendable."
    else:
        return "No tienes suficiente presupuesto para la compra."







#10 Evaluador de contraseñas seguras 
#Diseña un programa que verifique si una contraseña es segura.
#Debe cumplir con:

#Al menos 8 caracteres
#Incluir números y letras
#No contener espacios
#Dale retroalimentación al usuario sobre cómo mejorar su contraseña.

import re

def evaluar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    elif not re.search(r"\d", contraseña) or not re.search(r"[a-zA-Z]", contraseña):
        return "La contraseña debe contener números y letras."
    elif " " in contraseña:
        return "La contraseña no debe contener espacios."
    else:
        return "La contraseña es segura."
