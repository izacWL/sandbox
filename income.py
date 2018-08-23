def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_num = int(input("How many months? "))

    for month in range(1, month_num + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)
    return income_print(incomes, month_num)



def income_print (incomes, month_num):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_num + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))
main()