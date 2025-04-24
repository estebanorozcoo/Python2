Edad = int (input ("Ingresa tu edad "))
if Edad < 18:
 print ("No puedes entrar porque tienes menos de 18 años")
else:
    Pase = input ("Tienes pase dorado")
    if Edad >= 18 and Pase=="si":
      print("Puedes entrar")
    elif Pase=="no" and Edad >= 18 and Edad <= 25:
      print ("Puedes entrar")
    elif Edad > 25 and Pase == "no":
     print ("No puedes entrar")