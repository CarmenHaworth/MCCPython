#display a welcome message
print("The Miles Per Gallon program")
print()

#get input from user
choice = "y"
while choice.lower() == "y":

    miles_driven = float(input("Enter miles driven:           "))
    gallons_used = float(input("Enter gallons of gas used:    "))
    cost_pergallon = float(input("Enter cost per gallon:        "))


    if miles_driven <= 0:
        print("Miles driven must be greater than zero.   Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero.  Please try again.")
    elif cost_pergallon <= 0:
        print("Cost used must be greater than zero.  Please try again.")
    else:
        #calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used),2)
        total_cost = round((gallons_used * cost_pergallon),2)
        cost_permile = round((total_cost / miles_driven), 2)
        print()
        print("Miles per Gallon:           ", mpg)
        print("Total Gas Cost:             ", total_cost)
        print("Cost Per Mile:              ", cost_permile)
        print()
    choice = input("Get entries for another trip (y/n)?  ")

print()
print("Bye")
