biblioteca = [
    {"title": "Book 1", "price": 10.0, "quantity": 100},
    {"title": "Book 2", "price": 15.0, "quantity": 50},
    {"title": "Book 3", "price": 20.0, "quantity": 30},
    {"title": "Book 4", "price": 25.0, "quantity": 10},
    {"title": "Book 5", "price": 30.0, "quantity": 5}
]


while True:
    print ("""
         1. Añadir libros al inventario.
         2. Consultar libros en inventario.
         3. Actualizar precios de libros.
         4. Eliminar libros del inventario
         5. Calcular el valor total del inventario.""")
    
    menu = input("Selecciona una opción (1-5): ")
    if menu == "1":
        while True:
            titulo = input("Ingresa el nombre del libro que deseas agregar: ")
            precio = float(input("Ingresa el precio del libro registrado: "))
            cantidad = int(input ("Ingresa la cantidad de libros disponibles: "))

            if (precio and cantidad) > 0:
                biblioteca.append({"title": titulo, "price": precio, "quantity": cantidad})
            else:
                print ("El numero ingresado no es valido porque debe ser positivo")
    elif menu =="2":
        libro = input ("Que libro deseas consultar: ")
        for buscar in biblioteca:
            if libro == buscar["title"]:
                print(buscar)
    elif menu == "3":
        nom_libro = input("Ingrese el nombre del producto el cual deseas modificar el precio: ")
        for buscarr in biblioteca:
                if nom_libro == buscarr["title"]: 
                    while True:
                        precio = float(input ("Ingresa el nuevo precio del producto: "))
                    
                        if precio > 0:
                            buscarr["price"] = precio
                            break
                        else:
                            print("Digite un numero mayor a 0")
    elif menu == "4":
        nombre_libr = input ("Ingresa el nombre del libro que deseas eliminar que ya no esta disponible: ")
        for buscarrr in biblioteca:
            if nombre_libr == buscarrr["title"]:
                biblioteca.remove(buscarrr)
        else:
            print ("El nombre del libro ingresado no se encuentra en la biblioteca")
            


    

            
        

