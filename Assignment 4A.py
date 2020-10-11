def main():
    number_list = []
    size = int(input("Please enter an integer value the size of your list:  "))
    gather(number_list, size)
    listing(number_list)
    
def gather(number_list, size):
    for counter in range(size):
        number = int(input("Enter an integer between 1 and 10(inclusive):  "))
        if number > 10:
            number = 10
        elif number < 1:
            number = 1
        number_list.append(number)   

def listing(number_list):
    print("Printing your entries as a chart")
    for entry in number_list:
        for count in range(entry):
            print("*", end ="")
        print()
      
if __name__ == "__main__":
    main()
    
