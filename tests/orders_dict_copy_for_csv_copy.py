## Adds user input to Orders.csv file in dictionary format.
## Each piece of data is added to a new line.


import json
import csv


customer = {}

for i in range(1):
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")
    customer_phone = input("Enter your phone number: ")
    
    courier = open("C:/vscode/Python/Projects/mini_project/tests/couriers_dict.csv", 'r')
    reader = csv.DictReader(courier)
    for row in reader:
        print(row)
    customer_row = int(input("Enter a courier id number: "))

    
    customer["customer_name"] = customer_name
    customer["customer_address"] = customer_address
    customer["customer_phone"] = customer_phone
    customer["customer_courier"] = customer_row
    
    
    
with open('C:/vscode/Python/Projects/mini_project/tests/orders_dict.csv', 'a+', newline='') as file:
    fieldnames = ["customer_name", "customer_address", "customer_phone", "customer_courier"]
    csvwriter = csv.DictWriter(file, fieldnames=fieldnames)
    csvwriter.writerow(customer)