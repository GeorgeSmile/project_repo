## Adds user input to Orders.txt file in dictionary format.
## Each piece of data is added to a new line.

import json
import csv


customer = {}

for i in range(1):
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")
    customer_phone = input("Enter your phone number: ")
    
    courier = open("C:/vscode/Python/Projects/mini_project/tests/couriers_dict.csv", 'r')
    courier_file = csv.DictReader(courier)
    for row in courier_file:
        print(dict(row))
    courier_index = int(input("Enter a courier index number: "))
    customer_courier = courier_file
    
    
    
    file = open("C:/vscode/Python/Projects/mini_project/tests/basket_dict.csv", 'r')
    customer_order = file.readlines()
    customer_order_list = []
    for i in customer_order:
        customer_order_list.append(i.strip())
        
    status = ["Delivered", "Confirmed and pending", "Declined", "Out for Delivery"]

    if not customer_courier:
        status = status[2]
    else:
        status = status[1]

        
    

    customer["customer_name"] = customer_name
    customer["customer_address"] = customer_address
    customer["customer_phone"] = customer_phone
    customer["customer_order_list"] = customer_order_list
    customer["customer_courier"] = customer_courier
    customer["order_status"] = status 
    
    

    print(customer)

    with open('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', 'a+') as file: 
            file.write(json.dumps(customer, indent=2))
    
    