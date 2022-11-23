import json
import csv
from operator import index
import pandas as pd
from sys import exit


def main():    
    
    while True:
        options = input('''
    
    Main menu:
    [1] Products menu
    [2] Add new product
    [3] Remove product
    [4] Place order menu
    [0] Exit
    
    ''')

        if options == "0":
            print("Exiting...")
            exit()
        
        elif options == "1":
            print("\nList of products:")
            df = pd.read_csv("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv")
            print(df)
            input("\nPress enter to return to main menu.")
            main()
            
        elif options == "2":
            df = pd.read_csv("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv")
            print(df)
            new_pname = input("Please enter the new product name or type exit to return to previous menu: ")
            if new_pname == "exit":
                main()
            else:
                new_pprice = input("Please enter the new product price: ")
                new_product = [new_pname, float(new_pprice)]
                print(new_product)
                df.loc[-1] = new_product  # type: ignore
                df = df.reset_index(drop = True) # resets index
                df.to_csv("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv", index=False)
                print(df)
                input("Press enter to return to main menu.")
                main()

        elif options == "3":
            while True:
                print("\nList of products")
                df = pd.read_csv("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv")
                df.drop(df.filter(regex="Unname"),axis=1, inplace=True)  # type: ignore
                print(df)
                delete_product = input("Please enter the index number of the product you want to delete or type 'exit' to return to the previous menu: ")
                if delete_product == "exit":
                    main()
                else:
                    df = df.drop(labels=int(delete_product), axis = 0)
                    df.to_csv("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv", index=False) # need index=False to see index numbers properly
                print(df)
                input("Press enter to return to main menu.")
                main()
        
        elif options == "4":
            order_menu()

def order_menu():
    while True:
        order_options = input('''
    Order menu:
    [1] View couriers 
    [2] View orders
    [3] Place order
    [4] Update order
    [0] Return to main menu                        
                            ''')
        
        if order_options == "1":
            file = open("C:/vscode/Python/Projects/mini_project/tests/couriers_dict.csv", 'r')
            view_couriers = csv.DictReader(file)
            for row in view_couriers:
                print(dict(row))
                
        elif order_options == "2":
            print("\nList of orders:")
            df = pd.read_csv("C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv")
            print(df)
            input("\nPress enter to return to order menu.")
            order_menu()
                
        
        elif order_options == "3":
            customer = {}

            for i in range(1):
                customer_name = input("Enter your name, 0 to cancel: ")
                if customer_name == "0":
                    break
                customer_address = input("Enter your address, 0 to cancel: ")
                if customer_address == "0":
                    break
                customer_phone = input("Enter your phone number, 0 to cancel: ")
                if customer_phone == "0":
                    break
                
                courier = open("C:/vscode/Python/Projects/mini_project/tests/couriers_dict.csv", 'r')
                reader = csv.DictReader(courier)
                for row in reader:
                    print(row)
                customer_courier = int(input("Enter a courier index number, type 'exit' to cancel: "))
                if customer_courier == "exit":
                    break
    
                file = open("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv", 'r')
                customer_order = []
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                while True:
                    customer_order.append(input("Enter product index number, 'n' to cancel: "))
                    customer["customer_name"] = customer_name
                    customer["customer_address"] = customer_address
                    customer["customer_phone"] = customer_phone
                    customer["customer_order"] = customer_order
                    customer["customer_courier"] = customer_courier
                    if customer_order[-1] == "n":
                        customer_order.pop() # Removing 'n' from customer_order
                        with open('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', 'a+', newline='') as file:
                            fieldnames = ["customer_name", "customer_address", "customer_phone", "customer_courier","customer_order"]
                            csvwriter = csv.DictWriter(file, fieldnames=fieldnames)
                            csvwriter.writerow(customer)
                        break
                        
                    
                    print(customer)
                    
                    
        elif order_options == "4":
            update_order_status()
                
        elif order_options == "0":
            print('Returning...')
            main()
        
def update_order_status():
    df = pd.read_csv('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv')
    print(df)
    update_status = input("Please select the index number of the order you would like to update: ")
    order_statuses = ["PREPARING", "SHIPPED", "DELIVERED", "CANCELLED"]
    for i, status in enumerate(order_statuses):
        print(i, status)
    new_status = input("Select the new status by typing the index value above: ")
    df.loc[int(update_status), "status"] = order_statuses[int(new_status)]
    df.to_csv('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', index = False)
    input("Press enter to return to orders menu.")
    order_menu()
                        
main()