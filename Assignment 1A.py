print("Carmen Haworth     code date: 09-12-2020")
print()
#get the length and width input
length = float(input("Enter the length of a rectangle:\t"))
width = float(input("Enter the width of a rectangle:\t\t"))
#convert to area and perimeter values, rounding to 2 decimals
area = length * width
perimeter = (length * 2) + (width * 2)
area = round(area, 2)
perimeter = round(perimeter, 2)
print("\nThe area of the rectangle is:\t\t" + str(area) +
      "\nThe perimeter of the rectangle is:\t" + str(perimeter))

