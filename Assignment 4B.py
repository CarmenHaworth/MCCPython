
def main():
    name_list = []
    spent_list = []
    total_amount = get_lists(name_list, spent_list)
    print_lists(name_list, spent_list, total_amount)

def get_lists(name_list, spent_list):
    total_amount = 0
        
    for n in range(10): 
       name = str(input("Please Enter The Customer Name: "))
       name_list.append(name)
       amount = float(input("Please Enter The Amount Spent: "))
       spent_list.append(amount)
       total_amount += amount
    return total_amount
    
def print_lists(name_list, spent_list, total_amount):
    average_amount = round(total_amount / 10,2)
    maximum_amount = max(spent_list)
    minimum_amount = min(spent_list)
    print("\n---------------------------------------\n")
    print("Customer Name           Amount Spent\n")
    for i in range(10):
        print(name_list[i] + "\t\t\t" + "$" + str(spent_list[i]))
    print("\nTotal Amount Spent:       $", round(total_amount,2))
    print("\nAverage Amount Spent:     $", average_amount)
    print("\nLargest Amount Spent:     $", maximum_amount)
    print("\nSmallest Amount Spent:    $", minimum_amount)
            
if __name__ == "__main__":
    main()
