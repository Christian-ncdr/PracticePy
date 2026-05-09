#budget_tracker

monthly_income = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total expenses: "))
savings = float(input("Enter your savings goal: "))

money_surplus = monthly_income - total_expenses

if total_expenses > monthly_income:
    print("Warning! you are spending more than you earn")
elif money_surplus == 0:
    print("Warning! you are breakeven, you wont save anything")
else:
    months_takes = savings / money_surplus

    print("\nResult\n")
    print(f"you are saving: {money_surplus:.2f} a month,\nyou will reach your goal in {months_takes:.2f} months! ")