from operator import index

def main():    
    
    while True:
        options = input('''
    
    Choose an option:
    [1] Products menu
    [2] Create new product
    [3] Remove product
    [4] Basket
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



main()
                
              
                


               


    