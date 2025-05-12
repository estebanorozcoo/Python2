# Inventario como diccionario: {'producto': (precio, cantidad)}
inventario = {}

# Validar entrada numérica
def solicitar_numero(mensaje, tipo=float):
    while True:
        entrada = input(mensaje)
        try:
            valor = tipo(entrada)
            if valor < 0:
                print("Por favor ingresa un número positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

# Añadir producto
def agregar_producto(nombre, precio, cantidad):
    if nombre in inventario:
        print(f"El producto '{nombre}' ya existe. Se actualizará su cantidad.")
        precio_actual, cantidad_actual = inventario[nombre]
        inventario[nombre] = (precio, cantidad_actual + cantidad)
    else:
        inventario[nombre] = (precio, cantidad)
    print(f"Producto '{nombre}' agregado/actualizado correctamente.")

# Consultar producto
def consultar_producto(nombre):
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto: {nombre}\nPrecio: ${precio:.2f}\nCantidad: {cantidad}")
    else:
        print(f"El producto '{nombre}' no está en el inventario.")

# Actualizar precio
def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        _, cantidad = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad)
        print(f"Precio de '{nombre}' actualizado correctamente.")
    else:
        print(f"No se puede actualizar. El producto '{nombre}' no existe.")

# Eliminar producto
def eliminar_producto(nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"El producto '{nombre}' no existe.")

# Calcular valor total del inventario usando lambda
def calcular_valor_total():
    total = sum(map(lambda item: item[1][0] * item[1][1], inventario.items()))
    print(f"\nValor total del inventario: ${total:.2f}")

# Menú interactivo
def menu():
    while True:
        print("\n----- MENÚ DE INVENTARIO -----")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Mostrar todo el inventario")
        print("7. Salir")

        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = solicitar_numero("Precio del producto: $")
            cantidad = solicitar_numero("Cantidad disponible: ", int)
            agregar_producto(nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ").strip()
            consultar_producto(nombre)

        elif opcion == "3":
            nombre = input("Nombre del producto a actualizar: ").strip()
            nuevo_precio = solicitar_numero("Nuevo precio: $")
            actualizar_precio(nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)

        elif opcion == "5":
            calcular_valor_total()

        elif opcion == "6":
            if inventario:
                print("\nInventario completo:")
                for nombre, (precio, cantidad) in inventario.items():
                    print(f"- {nombre}: Precio ${precio:.2f}, Cantidad {cantidad}")
            else:
                print("El inventario está vacío.")

        elif opcion == "7":
            print("Saliendo del programa. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida. Por favor elige una opción del 1 al 7.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
