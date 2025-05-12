
# diccionario = {"Esteban": {"telefono":1231233213, "nota":4}, "Daniel":{"telefono":1231233213, "nota":4}"
# diccionario = {"Esteban": {"telefono":1231233213, "notas":{"p":1,"f":5,"s":3,"q":4}}, "Daniel":{"telefono":1231233213, "nota":4}"
# diccionario ["Esteban"] ["notas"] ["q"] = 5 

estudiantes = {} 

while True:
    print ("""
           1.   Agregar estudiante.
           2.   Modificar la calificación de un estudiante.
           3.   Mostrar la información de todos los estudiantes.
           4.   Eliminar un estudiante por su nombre.
           5.   Salir
           """)
    opciones = input ("Ingresa una opcion: ")
    if opciones == "1":
        while True:
            nombre_estudiante = input ("Ingresa el nombre del estudiante: ")
            edad = input ("ingresa la edad del estudiante: ")
            calificacion = input ("Ingresa la calificacion del estudiante: ")

            estudiantes[nombre_estudiante]={"edad":edad, "calificacion": calificacion}
            
            respuesta = input ("Quieres seguir ingresando estudiantes si/no: ")
            if respuesta.lower() == "no":
                break
            elif respuesta.lower() == "si":
                continue
            else:
                print ("Datos incorrectos")
    
    elif opciones == "2":
        nombre = input ("Ingresa el nombre del estudiante que deseas modificar la calificacion.")
        if nombre in estudiantes:
            estudiantes[nombre]["calificacion"] = input("Ingresa nueva calificacion")
        else:
            print ("No hay ningun estudiante con ese nombre")
    elif opciones == "3":
        if len(estudiantes) == 0:
            print ("No se han agregado estudiantes")
        else:
            for clave, valor in estudiantes.items(): print(f"{clave}: {valor}")
    elif opciones == "4":
        verifica = input ("Ingresa el nombre del estudiante")
        if verifica in estudiantes:
            estudiantes.pop(verifica)
        else:
            print ("No hay estudiantes con ese nombre en la lista")
    elif opciones == "5":
        break
    else:
        print ("Valor no valido")



#for clave, valor in estudiantes.items(): print(f"{clave}: {valor}")
