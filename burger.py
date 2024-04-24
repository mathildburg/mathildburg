stock_burger = 10

while stock_burger > 0:
    quantity_burger_client = int(input("cuantas hamburguesas quiere el cliente ? : "))
    if stock_burger >= quantity_burger_client:
       stock_burger -= quantity_burger_client
    
    if stock_burger < quantity_burger_client:
        print("no hay hamburguesas suficientes")

    if stock_burger <= 3:
        print("Hay que llamar al proveedor")
        
    print("Quedan", stock_burger, "Hamburguesas")

print(" No hay stock de hamburguesas, hay que hacer un pedido")
