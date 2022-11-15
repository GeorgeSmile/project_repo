## Adds user input to Orders.txt file in dictionary format.
## Each piece of data is added to a new line.

import json



customer = {}

for i in range(1):
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")
    customer_phone = input("Enter your phone number: ")

    customer["customer_name"] = customer_name
    customer["customer_address"] = customer_address
    customer["customer_phone"] = customer_phone
        
    
    


    print(customer)

    with open('C:/vscode/Python/Projects/mini_project/tests/Orders.txt', 'a+') as file: 
            file.write(json.dumps(customer, indent=2))