# Inventario inicial con 5 libros
inventario = [
    {"titulo": "Libro 1", "precio": 10.0, "cantidad": 100},
    {"titulo": "Libro 2", "precio": 15.0, "cantidad": 50},
    {"titulo": "Libro 3", "precio": 20.0, "cantidad": 30},
    {"titulo": "Libro 4", "precio": 25.0, "cantidad": 10},
    {"titulo": "Libro 5", "precio": 30.0, "cantidad": 5}
]

# Función para añadir un libro al inventario
def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    try:
        precio = float(input("Ingrese el precio del libro: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if precio <= 0 or cantidad <= 0:
            print("El precio y la cantidad deben ser números positivos.")
            return
        inventario.append({"titulo": titulo, "precio": precio, "cantidad": cantidad})
        print("Libro agregado exitosamente.")
    except ValueError:
        print("Entrada inválida. El precio debe ser un número decimal y la cantidad un número entero.")

# Función para consultar un libro por título
def consultar_libro():
    titulo = input("Ingrese el título del libro a consultar: ")
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            print(f"Título: {libro['titulo']}, Precio: {libro['precio']}, Cantidad: {libro['cantidad']}")
            return
    print("El libro no se encuentra en el inventario.")

# Función para actualizar el precio de un libro
def actualizar_precio():
    titulo = input("Ingrese el título del libro a actualizar: ")
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            try:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                if nuevo_precio <= 0:
                    print("El precio debe ser un número positivo.")
                    return
                libro["precio"] = nuevo_precio
                print("Precio actualizado exitosamente.")
                return
            except ValueError:
                print("Entrada inválida. El precio debe ser un número decimal.")
                return
    print("El libro no se encuentra en el inventario.")

# Función para eliminar un libro del inventario
def eliminar_libro():
    titulo = input("Ingrese el título del libro a eliminar: ")
    for libro in inventario:
        if libro["titulo"].lower() == titulo.lower():
            inventario.remove(libro)
            print("Libro eliminado exitosamente.")
            return
    print("El libro no se encuentra en el inventario.")

# Función para calcular el valor total del inventario
def calcular_valor_total():
    total = sum(libro["precio"] * libro["cantidad"] for libro in inventario)
    print(f"Valor total del inventario: ${total:.2f}")

# Menú interactivo
def mostrar_menu():
    while True:
        print("\nSistema de Gestión de Inventario de Librería")
        print("1. Agregar libro")
        print("2. Consultar libro")
        print("3. Actualizar precio de libro")
        print("4. Eliminar libro")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            consultar_libro()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            calcular_valor_total()
        elif opcion == "6":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione un número del 1 al 6.")

# Iniciar el programa
mostrar_menu()
