print ("Bienvenido a la plataforma para la gestion de tu mascota")

nombre_animal = []
edades = []
estado_salud = []



def agregar_animal(): 
    nombre_animal.append (nombre)
    edades.append (edad)
    estado_salud.append (salud)
    print (f"{nombre_animal} ha sido agregado.")

def eliminar_animal(edad,salud):
    nom = input ("Ingresa el nombre del animal que desea eliminar: ")
    if nom in nombre_animal:
        indice = nombre_animal.index(nom)
        nombre_animal.pop(indice)
        print (f"{nom} ha sido eliminado de la lista")
    else:
        print ("El nombre del animal no ha sido encontrado")

def listar_animales():
    if len(nombre_animal) == 0:
        print ("No hay animales registrado con ese nombre.")
    else:
        print("\nLista de animales registrados:")
        for i in range (len(nombre_animal)):
            print(f"{i +1}. Nombre: {nombre_animal[i]}, Edad: {edades[i]}, Salud: {"Enfermo" if estado_salud[i] == "si" else "Sano"}")


#main
while True:
    print ("""
           1. Agregar un animal
           2. Eliminar un animal por su nombre 
           3. Listar todos los animales registrados
           4. Salir""")
    opciones = input ("Ingresa una opcion: ")
    if opciones == "1":
        nombre = input ("Ingrese el nombre del animal: ")
        edad =  int(input ("Ingrese la edad del animal: "))
        salud = input ("¿El animal esta enfermo? (si/no)").lower()
        agregar_animal()
    elif opciones == "2":
        eliminar_animal(edad,salud)
    elif opciones == "3":
        listar_animales()
    else:
        break



