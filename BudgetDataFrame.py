# Calculates budgets using excel
# Budget is only for 12 month period (NO months can be repeated)
import pandas as pd
import numpy as np


# Timeline
def timeline():
    period = input("Enter budget timeline eg(August-April) for August to April: ").split("-")
    months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5,
              "june": 6, "july": 7, "august": 8, "september": 9, "october": 10,
              "november": 11, "december": 12}
    timeline = []
    if months[period[0].lower()] > months[period[1].lower()]:
        c = months[(period[0]).lower()]-1
        for _ in range(12 - c):
            timeline.append(list(months)[c])
            c += 1
        r = 0
        while r < months[(period[1]).lower()]:
            timeline.append(list(months)[r])
            r += 1
    else:
        timeline += (list(months))[months[period[0].lower()] - 1: months[period[1].lower()]]
    timeline = [m.capitalize() for m in timeline]
    return timeline


# Expenses
def expenses(timeline):
    expense_cost = {}
    expense_input = input("Enter expenses eg(rent, groceries, netflix): ").split(", ")
    for expense in expense_input:
        expense_cost[expense.capitalize()] = []
        fixed_input = input(f'Type "all" for fixed {expense} expense (press enter for variable expense): ')
        if fixed_input == 'all':
            monthly_expense_cost = float(input(f"Expense for {expense}:"))
            fixed_cst = [monthly_expense_cost for _ in range(len(timeline))]
            expense_cost[expense.capitalize()] = fixed_cst
        else:
            for month in timeline:
                monthly_expense_cost = float(input(f'{expense} expense for the month of {month}:'))
                expense_cost[expense.capitalize()].append(monthly_expense_cost)
    return expense_cost


# Income & Savings
def income(timeline, expense_cost):
    income_revenue = {}
    income_input = input("Enter income eg(allowance, part-time): ").split(", ")
    for income in income_input:
        income_revenue[income.capitalize()] = []
        fixed_input = input(f'Type "all" for fixed {income} income (press enter for variable expense): ')
        if fixed_input == 'all':
            monthly_income_revenue = float(input(f"Amount from {income}: "))
            fixed_revenue = [monthly_income_revenue for _ in range(len(timeline))]
            income_revenue[income.capitalize()] = fixed_revenue
        else:
            for month in timeline:
                monthly_income_revenue = float(input(f'{income} income for the month of {month}:'))
                income_revenue[income.capitalize()].append(monthly_income_revenue)
    saving_boolean = input("Do you wish to account for your savings [yes/no]: ")
    if saving_boolean == "yes":
        savings = float(input(f"Savings to be hold for the month of {timeline[0]} "))
        statement_savings = """
        * Surplus amounts will be credited to the savings account. Similarly, any monthly overdrafts will be met
        from the savings account.
        """
        print(statement_savings)
        total_exp = np.zeros((len(timeline),))
        for expense in expense_cost:
            total_exp += np.array(expense_cost[expense])
        total_rev = np.zeros((len(timeline),))
        for rev in income_revenue:
            total_rev += np.array(income_revenue[rev])
        np_savings = total_rev - total_exp
        saving_lst = []
        for month in np_savings:
            savings += month
            saving_lst.append(savings)

        income_revenue["Savings"] = saving_lst
        return income_revenue


# main
timeline_ds = timeline()
expense_ds = expenses(timeline_ds)
income_ds = income(timeline_ds,expense_ds)
data_frame = pd.DataFrame(expense_ds, index=timeline_ds)
data_frame2 = pd.DataFrame(income_ds, index=timeline_ds)
master_ds = pd.concat([data_frame, data_frame2], axis=1)
print(master_ds)













