file = open("C:/vscode/Python/Projects/mini_project/tests/drinks.txt", 'r')


print("Enter the Line to Delete: ")
lineText = input()
fileHandle = open('C:/vscode/Python/Projects/mini_project/tests/drinks.txt', "r")
lines = fileHandle.readlines()
fileHandle.close()
fileHandle = open('C:/vscode/Python/Projects/mini_project/tests/drinks.txt', "w")
for line in lines:
  if line.strip("\n") != lineText:
    fileHandle.write(line)
fileHandle.close()
print("\nThe Line Deleted Successfully!")