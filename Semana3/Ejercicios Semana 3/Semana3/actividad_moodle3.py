productos = {}

while True:
    print (""" 
            1. Añadir productos.
            2. Consultar productos.
            3. Actualizar precios.
            4. Eliminar productos.
            5. Calcular el valor total del inventario.
           """)
    opciones = input ("Ingresa una opcion: ")
    if opciones == "1":
        while True:
            nombre_producto = input("Ingresa el nombre del producto que deseas añadir: ")
            precio = float(input("Ingresa el precio del producto: "))
            cantidad = int(input("Ingresa la cantidad disponible del producto: "))

