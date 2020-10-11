print("Carmen Haworth    code date 09-12-2020")
print()
#get temperature in Fahrenheit
fahrenheit = float(input("Please enter a temperature in Fahrenheit:\t"))
#convert temperature into Celcius to 2 decimal places
celcius = (fahrenheit - 32) * 5/9
celcius = round(celcius, 1)
print()
print("The temperature in Celcius is:\t\t\t" + str(celcius))
print()
print()
