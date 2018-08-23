sales = float(input("Enter sales: $"))
if sales >=1000:
    bonus = sales*0.15
    print(bonus)
else:
    bonus = sales * 0.10
    print(bonus)