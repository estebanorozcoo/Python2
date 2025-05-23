print("Try Progamiz.pro")

print("Pareja Ideal")
puntaje = 0

pregunta1 = input("¿Tienes más de 20 años? ")
if pregunta1 == "si":
    puntaje = puntaje + 10
else: puntaje = puntaje


pregunta2 = input("¿Mides más de 1.75cm? ")
if pregunta2 == "si":
    puntaje = puntaje + 10
else: puntaje = puntaje

pregunta3 =input("¿Haces ejercicio? ")
if pregunta3 == "si":
    puntaje = puntaje + 10
else: puntaje = puntaje

pregunta4 = input("¿Cuidas tu alimentación? ")
if pregunta4 =="si":
    puntaje = puntaje + 10
else:puntaje = puntaje
            
pregunta5 = input("¿Cuidas de tu espiritualidad? ")
if pregunta5 == "si":
    puntaje = puntaje +10
else:puntaje = puntaje
print (f"Entre 10 y 50 estas en un promedio de {puntaje}")
