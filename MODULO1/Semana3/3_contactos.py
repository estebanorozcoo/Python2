# Diccionario para almacenar los contactos
contactos = {}

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if nombre in contactos:
        print(f"El contacto '{nombre}' ya existe.")
    else:
        telefono = input("Ingrese el número de teléfono: ").strip()
        contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")

def mostrar_contactos():
    if not contactos:
        print("No hay contactos guardados.")
    else:
        print("\nLista de contactos:")
        for nombre, telefono in contactos.items():
            print(f"{nombre}: {telefono}")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encontró.")

def menu():
    while True:
        print("\n--- Menú de Contactos ---")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            buscar_contacto()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
menu()
