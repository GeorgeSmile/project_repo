def main():
    mylist = []
    while True:
        operation = input('''
Menu:
[1] Add fizzy drink to the list
[2] Remove fizzy drink from the list
[3] Display list
[4] View product index numbers
[5] Exit programm

''')
        if operation == '1':
            print("Type the fizzy drink you would like to add to the list: ")
            fizzy_drink = str(input())
            mylist.append(fizzy_drink)

        elif operation == '2':
            print("Type position of the fizzy drink you like to remove from the list: ")
            fizzy_drink = int(input())
            mylist.pop(fizzy_drink)

        elif operation == '3':
            print(mylist)

        elif operation == '4':
            for (i, item) in enumerate(mylist, start=1):
                print(i, ":", item)

        elif operation == '5':
            break

        else:
            print("Invalid choice. Please try again.")

main()