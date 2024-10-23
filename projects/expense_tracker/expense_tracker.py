from expense import Expense
import datetime
import calendar

def main():
    print(f"{'*'*5} Welcome to the Expense Tracker! {'*'*5}")
    expense_file_path="projects/expense_tracker/expense.csv"
    budget=10000
    while True:
        #get user input
        expense=get_user_expense()
        #save expenses to a csv file
        save_expense_to_file(expense,expense_file_path)
        choice=input("Enter [Y/y] to add more ")
        if(choice=='y' or choice=='Y'):
            continue
        else:
            break

    #summarize and calculate expenses
    summarize_expense(expense_file_path,budget)


def get_user_expense():
    print(f"{'*'*5}Give expenses Here...{'*'*5}")
    expense_name=input("Enter name of expense: ")
    expense_amount=float(input("Enter expense Amount: "))
    expense_categories=[
        "food",
        "home",
        "work",
        "fun",
        "misc",
    ]
    while True:
        print(f"{'*'*5}Please select a Category >>>")
        for index,category in enumerate(expense_categories):
            print(f"  {index+1}. {category}")


        value_range=f"[1 - {len(expense_categories)}]"
        selected_index=int(input(f"select an index for category {value_range}: "))-1

        
        if selected_index in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
            return new_expense
        else:
            print(f"{'*'*5}invalid category. Please try again{'*'*5}")
    

def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"saving user expenses:{expense} to {expense_file_path}")
    with open(expense_file_path,'a') as file:
        file.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path,budget):
    print(f"{'*'*5}Summarizing user expenses: ...{'*'*5}")
    expenses: list[Expense] = []
    with open(expense_file_path,'r') as file:
        lines=file.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(',')
            line_expense=Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)
        
        amount_for_category={}

        for expense in expenses:
            key=expense.category
            if key in amount_for_category:
                amount_for_category[key] +=expense.amount
            else:
                amount_for_category[key] = expense.amount
        
        print(f"{'*'*5}Expenses By Category {'*'*5}")
        for key,amount in amount_for_category.items():
            print(f"{key} : {amount:.2f}")
        
        total_spent= sum([x.amount for x in expenses])
        print(f"Total_spent: Rs.{total_spent:.2f}")

        remaining_budget=budget-total_spent
        print(f"Budget Remaining: Rs.{redText(remaining_budget)}")

        now=datetime.datetime.now()
        days_in_month=calendar.monthrange(now.year,now.month)[1]
        remaining_days=days_in_month-now.day

        daily_budget=remaining_budget/remaining_days
        print(f"You can spend Rs.{redText(daily_budget)} per day")
        # print(f"{redText(daily_budget)}")
        
def redText(text):
    return f"\033[31m{text}\033[0m"

if __name__ == "__main__":
    main()

