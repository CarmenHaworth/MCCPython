#display a welcome message
print("The Miles Per Gallon program")
print()

#get input from user
miles_driven = float(input("Enter miles driven:      "))
gallons_used = float(input("Enter gallons used:      "))

if miles_driven <= 0:
    print("Miles driven must be greater than zero.   Please try again.")
elif gallons_used <= 0:
    print("Gallons used must be greater than zero.  Please try again.")
else:
    #calculate and display miles per gallon
    mpg = round((miles_driven / gallons_used),2)
    print("Miles per Gallon:           ", mpg)

print()
print("Bye")
