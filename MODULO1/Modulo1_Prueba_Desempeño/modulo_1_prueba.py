#Initial inventory with 5 products
inventory_store = [
    {"product_name": "milk", "price": 4.000, "quantity": 50},
    {"product_name": "rice", "price": 3.000, "quantity": 80},
    {"product_name": "apple", "price": 2.000, "quantity": 30},
    {"product_name": "orange", "price": 1.000, "quantity": 20},
    {"product_name": "potato", "price": 1.500, "quantity": 40}
]




#Function to add products to inventory
def add_products ():
        product_name_2 = input("Enter the name of the product you want to add: ")
        try:
            #We validate with float that it is a decimal number
            price = float(input("Enter the price of the product: "))

            #We validate with int that it is an integer
            quantity_2 = int(input("Enter the available quantity of the product"))

            #Validates if the entered number is positive
            if price <=0 or quantity_2 <=0: #Validates if the entered number is positive
                print("The number entered must be positive.")
                return
            else:
                inventory_store.append({"product_name": product_name_2, "price": price, "quantity": quantity_2})
                print(f"The product {product_name_2} has been added successfully")

        #If float or int are not met, then an error message will be displayed using except
        except ValueError:
            print("Error. The price must be a decimal number and the quantity a whole number.") 




#Function to consult products by name
def consult_products():
    product_name_2 = input("Enter the name of the product you wish to inquire about: ")

    
    #It validates that the consulted product is in the inventory and then displays its information with details.
    for product in inventory_store:
        if product["product_name"].lower() == product_name_2.lower():
            print(f"Product Name: {product ['product_name']}, Price: {product ['price']}, Quantity: {product['quantity']}")
            return
    print ("The product is not in the store's inventory.")




#Function to update the price of the products
def update_price():
    product_name_2 = input("Enter the name of the product you want to update: ")
    #It is validated that the consulted product is in the inventory and then the price is updated.
    for product in inventory_store:
        if product["product_name"].lower() == product_name_2.lower():
            try:
                new_price = float(input("Enter the new price: "))
                if new_price <=0:
                    print ("The price must be a positive number.")
                    return
                product["price"] = product_name_2
                print("Price updated successfully.")
                return
            except ValueError:
                print("Error. The price must be a decimal number.")
                return
            



#Function to remove products from inventory           
def delete_product():
    #It is validated that the product is in the inventory so that it can then be eliminated.
    product_name_2 = input("Enter the name of the product you want to delete: ")
    for product in inventory_store:
        if product["product_name"].lower() == product_name_2.lower():
            inventory_store.remove(product)
            print("product successfully removed")
            return
    print("The product is not in inventory.")




#Function to calculate the total value of the inventory
def total_inventory_value():
    #An arithmetic operation is performed on the inventory data to obtain the total value in the inventory.
    total_inventory = sum(product["price"] * product["quantity"] for product in inventory_store)
    print (f"Total inventory value: {total_inventory:.2f}")




#Start the program with the menu
while True:
    print("\nStore inventory management.")
    print("\n----MENU----")
    print("1. Add products.")
    print("2. Consult products.")
    print("3. Update product prices.")
    print("4. Delete products.")
    print("5. Total inventory value.")
    print("6. Exit program.")
    options = input("\nSelect one option (1-6): ")
    
    #The entered number is validated and then the corresponding function is executed.
    if options == "1":
        add_products()

    elif options == "2":
        consult_products()

    elif options == "3":
        update_price()

    elif options == "4":
        delete_product()

    elif options == "5":
            total_inventory_value()
    elif options == "6":
        print("Logging out. See you later!")
        break
    else:
        print("Invalid option. Please select a number from 1 to 6.")
