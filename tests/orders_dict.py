## Adds user input to Orders.txt file in dictionary format.
## Each piece of data is added to a new line.

import json



customer = {}

for i in range(1):
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")
    customer_phone = input("Enter your phone number: ")
    
    courier = open("C:/vscode/Python/Projects/mini_project/tests/couriers.txt", 'r')
    courier_file = courier.readlines()
    
    for i in range(len(courier_file)):
        print(i, courier_file[i])
    
    courier_index = int(input("Enter a courier index number: "))
    customer_courier = courier_file[courier_index].strip()
    
    
    file = open("C:/vscode/Python/Projects/mini_project/tests/basket.txt", 'r')
    customer_order = file.readlines()
    customer_order_list = []
    for i in customer_order:
        customer_order_list.append(i.strip())
    
    

    customer["customer_name"] = customer_name
    customer["customer_address"] = customer_address
    customer["customer_phone"] = customer_phone
    customer["customer_order_list"] = customer_order_list
    customer["customer_courier"] = customer_courier  
    
    

    print(customer)

    with open('C:/vscode/Python/Projects/mini_project/tests/Orders.txt', 'a+') as file: 
            file.write(json.dumps(customer, indent=2))
    
    