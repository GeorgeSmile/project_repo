from operator import index
import sys

def main():
    menu = []
    basket = []
    
    while True:
        options = input('''
    
Choose an option:
[1] View Products
[2] View Basket
[3] Add to basket
[4] Remove from basket
[5] Create new product on menu
[6] Remove product on menu

[0] Exit

''')

        if options == "0":
            print("Exiting...")
            sys.exit()
        
        elif options == "1":
            file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'r')
            lines = file.readlines()
            for line in lines:
                menu.append(line.strip())
            for (i, item) in enumerate(menu, start=1):
                print(i,":", item)
        
        elif options == "2":
            for (i, item) in enumerate(basket, start=1):
                    print(i,":", item)

        elif options == "3":
            print("Type number of item to add to basket: ")
            item = int(input())
            basket.append(item)
            print("item added")
                

        elif options == "4":
            print("Type number item to remove from basket: ")
            item = int(input())
            basket.pop(item)
            print("Removed.")

        elif options == "5":
            file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'a+')
                     
            while True:
                product = str(input("Enter product name or type 'exit' to cancel: "))
                
                if product == "exit":
                    break
                else:
                    file.write(product + "\n")

                file.close()
                print("Product added!")
               
                
                
main()