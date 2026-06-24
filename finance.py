
children = input("Enter the number of children: ")

wage = input("Enter the hourly wage: ")

hours = input("Enter the number of hours worked: ")

if int(hours) < 40 or int(hours) > 240:
    print("Error: Hours worked must be between 40 and 240. If not then talk to your manager.")

elif 40<=int(hours)<=240:
    hourly_pay = int(wage) * int(hours)
    print("Gross pay: €" + str(hourly_pay))
    childcost = int(children) * 100
    print("Child cost: €" + str(childcost))
    grosspay = hourly_pay - childcost
    print("Gross pay after child cost: €" + str(grosspay))
    tax = grosspay * 0.2
    print("Tax: €" + str(tax))
    Netpay = grosspay - tax
    print("Net pay after tax: €" + str(Netpay))

    if 40 < int(hours) <= 240:
        overtime_hours = int(hours) - 40
        overtime_pay = overtime_hours * (int(wage) * 0.5)
        print("Overtime pay: €" + str(overtime_pay))
        total_pay = Netpay + overtime_pay
        print("Total pay after overtime: €" + str(total_pay))
    else:
        print("No overtime pay.")

else:
    print("Error: Invalid input. Please enter valid numbers for children, wage, and hours worked.")