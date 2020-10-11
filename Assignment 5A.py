# Student: Carmen Haworth   Assignment 5A

def writeToTextFile(filepath,line_to_write):
    with open(filepath, "a") as file:
       file.write(line_to_write)

def readFromTextFile(filepath):
    with open(filepath, "r") as file:
        return file.read()

def readListFromTextFile(filepath):
    with open(filepath, "r") as file:
        return file.readlines()

def display_menu():
    print()
    print(" ** The List of Candy **")
    print()
    print("COMMAND MENU")
    print("------------------")
    print("add   - Add to the List")
    print("file  - Show contents")
    print("list  - View as List")
    print("exit  - Exit program")
    print("------------------")
    print()
    
def main():
    
    filepath = "chocolate.txt"

    while True:
        display_menu()
        command = input("ENTER COMMAND:   ")
        if command.lower() == "add":
            writeToTextFile(filepath, input("Name of candy:  ") + "\n")
        elif command.lower() == "file":
            print(readFromTextFile(filepath))
        elif command.lower() == "list":
            candylist = readListFromTextFile(filepath)
            for i in range(len(candylist)):
                print(str(i+1) + ". " + candylist[i], end="")
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")
        

if __name__ == "__main__":
    main()

