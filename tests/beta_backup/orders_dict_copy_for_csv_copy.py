## Adds user input to Orders.csv file in dictionary format.
## Each piece of data is added to a new line.


import json
import csv
import pandas as pd

# customer = {}

# for i in range(1):
#     customer_name = input("Enter your name: ")
#     customer_address = input("Enter your address: ")
#     customer_phone = input("Enter your phone number: ")
    
#     courier = open("C:/vscode/Python/Projects/mini_project/tests/couriers_dict.csv", 'r')
#     reader = csv.DictReader(courier)
#     for row in reader:
#         print(row)
#     customer_row = int(input("Enter a courier id number: "))

    
#     customer["customer_name"] = customer_name
#     customer["customer_address"] = customer_address
#     customer["customer_phone"] = customer_phone
#     customer["customer_courier"] = customer_row
    
    
    
# with open('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', 'a+', newline='') as file:
#     fieldnames = ["customer_name", "customer_address", "customer_phone", "customer_courier"]
#     csvwriter = csv.DictWriter(file, fieldnames=fieldnames)
#     csvwriter.writerow(customer)
    
# def update_order_status():
#     df = pd.read_csv('orders.csv')
#     print(df)
#     update_status = input("Please select the index number of the order you would like to update: ")
#     order_statuses = ["PREPARING", "SHIPPED", "DELIVERED", "CANCELLED"]
#     for i, status in enumerate(order_statuses):
#         print(i, status)
#     new_status = input("Select the new status by typing the index value above: ")
#     df.loc[int(update_status), "Status"] = order_statuses[int(new_status)]
#     df.to_csv('orders.csv', index = False)
#     input("Press enter to return to orders menu.")
#     order_menu()

def add_product_menu():
    df = pd.read_csv("products.csv")
    print(df)
    new_pname = input("Please enter the new product name or type exit to return to previous menu: ")
    if new_pname == "exit":
        product_menu()
    else:
        new_pprice = input("Please enter the new product price: ")
        new_product = [new_pname, float(new_pprice)]
        print(new_product)
        df.loc[-1] = new_product
        df = df.reset_index(drop = True) # resets index
        df.to_csv("products.csv", index=False)
        print(df)
        input("Press enter to return to products menu.")
    main()