Numerol=int(input("Ingresa el numero "))

if Numerol % 30 and Numerol % 5 == 0:
 print ("FizzBuzz")
elif Numerol % 3 == 0:
 print ("Fizz")
elif Numerol % 5 == 0:
 print ("Buzz")
else:
 print(Numerol)