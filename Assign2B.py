print("Student Carmen Haworth  program date 9/20/2020")
print("\nWeekly Pay Calculator and Total Pay of Employees\n")

totalPay = 0
enterData = "Y"

while enterData.lower()=="y":
    # obtain pay rate and number of hours worked 
    rate = float(input("\nPlease enter employee's pay rate(more than $9.25): "))
    hours = float(input("\nPlease enter total hours this week (zero or positive number): "))
    if hours > 40:
        #calculate overtime pay and add to first 40 hours
        hoursOt = float(hours - 40)
        payOt = float(hoursOt *(rate * 1.5))
        pay = float((rate * 40) + payOt)
    elif hours <= 40:
        pay = float(rate * hours)
    print("\nTheir weekly total pay =", round(pay,2))
    totalPay = totalPay + pay
    enterData = input("\nDo you want to continue entering data? (Y/N):   ")
print("\nThe total pay of all employees equals", round(totalPay,2))
    
