import json
import csv
from operator import index


def main():    
    
    while True:
        options = input('''
    
    Main menu:
    [1] Products menu
    [2] Create new product
    [3] Remove product
    [4] Basket
    [5] Place order menu
    [0] Exit
    
    ''')

        if options == "0":
            print("Exiting...")
            break
        
        elif options == "1":
            file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'r')
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                print(f"{i}  {line.strip()}")
            
                
        elif options == "2":
            file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'a+')
            while True:
                new_product = input("Enter new product name, or type 'exit' to return to menu: ")
                if new_product == "exit":
                    break
                file.write(new_product + "\n")

        elif options == "3":
            while True:
                print("Enter the product name to delete, or type 0 to return to menu: ")
                line_text = input()
                file_handle = open('C:/vscode/Python/Projects/mini_project/tests/drinks.txt', "r")
                lines = file_handle.readlines()
                file_handle.close()
                file_handle = open('C:/vscode/Python/Projects/mini_project/tests/drinks.txt', "w")
                for line in lines:
                    if line.strip("\n") != line_text:
                        file_handle.write(line)
                file_handle.close()
                print("\nThe Line Deleted Successfully!")
                if line_text == "0":
                    break
        
        elif options == "4":
            basket()

        elif options == "5":
            order_menu()
        
        
def basket():
    while True:
        basket_options = input('''
    
    Basket options:
    [1] Basket contents
    [2] Products menu
    [3] Add product to basket
    [4] Remove from basket
    [0] Return to main menu
    
    ''')

        if basket_options == "1":
            file = open("C:/vscode/Python/Projects/mini_project/tests/basket.txt", 'r')
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                print(f"{i}  {line.strip()}")

        elif basket_options == "2":
            file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'r')
            lines = file.readlines()
            for i, line in enumerate(lines, start=1):
                print(f"{i}  {line.strip()}")
        
        elif basket_options == "3":
            file = open("C:/vscode/Python/Projects/mini_project/tests/basket.txt", 'a+')
            while True:
                new_product = input("Enter product name, or type 'exit' to return: ")
                if new_product == "exit":
                    break
                file.write(new_product + "\n")

        elif basket_options == "4":
            while True:
                print("Enter the product name to delete, or type 0 to return to basket: ")
                line_text = input()
                file_handle = open('C:/vscode/Python/Projects/mini_project/tests/basket.txt', "r")
                lines = file_handle.readlines()
                file_handle.close()
                file_handle = open('C:/vscode/Python/Projects/mini_project/tests/basket.txt', "w")
                for line in lines:
                    if line.strip("\n") != line_text:
                        file_handle.write(line)
                file_handle.close()
                print("\nThe Line Deleted Successfully!")
                if line_text == "0":
                    basket()
        
        elif basket_options == "0":
            break
        
def order_menu():
    while True:
        order_options = input('''
    Order menu:
    [1] View couriers 
    [2] View basket
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
            file = open("C:/vscode/Python/Projects/mini_project/tests/basket_dict.csv", 'r')
            view_basket = csv.DictReader(file)
            for row in view_basket:
                print(dict(row))
                
        
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
                customer_courier = int(input("Enter a courier id number, type 'exit' to cancel: "))
                if customer_courier == "exit":
                    break
    
                file = open("C:/vscode/Python/Projects/mini_project/tests/drinks_dict.csv", 'r')
                customer_order = []
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                while True:
                    customer_order.append(input("Enter product index number: "))
                    choice = input("Add another product?: ")
                    if choice == "n":
                        break

                                    
                status = ["Delivered", "Confirmed and pending", "Declined", "Out for Delivery"]

                if not customer_courier:
                    status = status[2]
                else:
                    status = status[1]
            
                customer["customer_name"] = customer_name
                customer["customer_address"] = customer_address
                customer["customer_phone"] = customer_phone
                customer["customer_order"] = customer_order
                customer["customer_courier"] = customer_courier
                customer["order_status"] = status
                
                    
                print(customer)

                with open('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', 'a+', newline='') as file:
                    fieldnames = ["customer_name", "customer_address", "customer_phone", "customer_courier","product_index", "order_status"]
                    csvwriter = csv.DictWriter(file, fieldnames=fieldnames)
                    csvwriter.writerow(customer)
                    break
                
        elif order_options == "0":
            break
                        
        
            
main()
    

    
                