"""
Rewriting lab 2A so that it incorporates add, subtract, multiply
and divide functions.  Each function takes 2 arguments and returns the
appropriate value based on those arguements.
"""

def makeChoice():
    print("Let's do some Math!\n")
    choice = input("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n\nWhich one do you want to do? (1,2,3,4):   ")
    while  choice.lower() != "1" and choice.lower() != "2" and choice.lower() != "3" and choice.lower() != "4":   
         print()
         choice = input("Please try again.  Enter 1, 2, 3 or 4:   ")
         print()
    return choice
  
def doMath(choice, firstNumber, secondNumber):
    if choice.lower() == "1":
       return addNumbers(firstNumber, secondNumber)
    elif choice.lower() == "2":
       return subtractNumbers(firstNumber, secondNumber)   
    elif choice.lower() == "3":
        return multiplyNumbers(firstNumber, secondNumber)     
    elif choice.lower() == "4":
        return divideNumbers(firstNumber, secondNumber)
        
def addNumbers(firstNumber,secondNumber):
    return firstNumber + secondNumber
    
def subtractNumbers(firstNumber,secondNumber):
    return firstNumber - secondNumber
    
def multiplyNumbers(firstNumber,secondNumber):
    return firstNumber * secondNumber
    
def divideNumbers(firstNumber,secondNumber):
    return firstNumber / secondNumber
    
def results(result):
    print("Results:  ", round(result,2))
        
def main():
    keepGoing = "Y"
    while keepGoing.lower() == "y":
        choice = makeChoice()
        #get numbers from user
        firstNumber = float(input("\nPlease enter the first number:\t"))
        secondNumber = float(input("\nPlease enter the second number:\t"))
        result = doMath(choice,firstNumber,secondNumber)
        results(result)
        keepGoing = input("\nDo you want to try this again? Y/N   ")
    print("\nIt was a pleasure doing math with you!!")

if __name__ == "__main__":
    main()
    

#print("Let's do some Math!\n")
#doMath = "Y"
#while doMath.lower() == "y":

 #   choice = input("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n\nWhich one do you want to do? (1,2,3,4):   ")

  #  while  choice.lower() != "1" and choice.lower() != "2" and choice.lower() != "3" and choice.lower() != "4":   
   #      print()
    #     choice = input("Please try again.  Enter 1, 2, 3 or 4:   ")
     #    print() 
#
 #   numberOne = float(input("\nPlease enter the first number:\t"))
  #  numberTwo = float(input("\nPlease enter the second number:\t"))

   # if choice.lower() == "1":
    #    answer = float(numberOne + numberTwo)
#    elif choice.lower() == "2":
 #       answer = float(numberOne - numberTwo)
  #  elif choice.lower() == "3":
#        answer = float(numberOne * numberTwo)
 #   elif choice.lower() == "4":
  #      answer = float(numberOne / numberTwo)

#    print()
    
#    print("Results:  ", round(answer,2))

 #   doMath = input("\nDo you want to try this again? Y/N   ")

#print("\nIt was a pleasure doing math with you!!")





