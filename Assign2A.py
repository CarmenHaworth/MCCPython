#display the program title 
print("Student: Carmen Haworth   Assignment 2A\n") 
print("Let's do some Math!\n")
doMath = "Y"
while doMath.lower() == "y":

    choice = input("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n\nWhich one do you want to do? (1,2,3,4):   ")

    while  choice.lower() != "1" and choice.lower() != "2" and choice.lower() != "3" and choice.lower() != "4":   
         print()
         choice = input("Please try again.  Enter 1, 2, 3 or 4:   ")
         print() 

    numberOne = float(input("\nPlease enter the first number:\t"))
    numberTwo = float(input("\nPlease enter the second number:\t"))

    if choice.lower() == "1":
        answer = float(numberOne + numberTwo)
    elif choice.lower() == "2":
        answer = float(numberOne - numberTwo)
    elif choice.lower() == "3":
        answer = float(numberOne * numberTwo)
    elif choice.lower() == "4":
        answer = float(numberOne / numberTwo)

    print()
    
    print("Results:  ", round(answer,2))

    doMath = input("\nDo you want to try this again? Y/N   ")

print("\nIt was a pleasure doing math with you!!")





