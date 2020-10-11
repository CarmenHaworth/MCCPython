def append(string1, string2):
    print(string1 + string2)

def positiveNumber(number1):
    if number1 < 0:
       return 0
    else:
       return number1
              
def evenOdd(entry):
    if entry%2 == 1:
        return False
    else:
        return True

def inCenturyRange(number):
    if number < 0 or number > 100:
        return False
    else:
        return True
                
def repeater(text = "Something", number = 6):
    print(text * number)  

def main():
    print("Let's test my functions")
    
    print("\nappend")
    append("Hey everyone,"," how's it going?")

    print("\npositiveNumber")
    number1 = int(input("enter a number:  "))
    result = positiveNumber(number1)
    print("Your number (zero if below zero): ",result)

    print("\nevenOdd")
    entry = int(input("Is the number even?  Enter a number:  "))
    result = evenOdd(entry)
    print(result)

    print("\ninCenturyRange")
    number = int(input("Enter a number:  "))
    print(inCenturyRange(number))

    print("\nrepeater")
    repeater()

if __name__ == "__main__":
    main()
