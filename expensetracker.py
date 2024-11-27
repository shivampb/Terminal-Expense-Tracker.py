from main import Expense
from datetime import datetime, timedelta


def main(): 
   def green(text):
    GREEN = '\033[92m'  
    RESET = '\033[0m'  
    return f"{GREEN}{text}{RESET}"
   file_path = "expense.csv"
   budget = 5000
   while True:
      try:
         print("Enter Operation Number [1. Enter New Expense, 2. See Passbook]")
         user_input = int(input("Enter NUmber Here:- "))
         if user_input == 1:
            expense  = expenseInfoFromUser()
            savingToCsv(expense ,file_path)
            print(green(f"(youre {expense} Saved Successfully"))
         elif user_input == 2:
            summerize(budget,file_path)
         elif user_input == 3:
            break
      except:
         print("Invalid Input Try Again Later :(")



def expenseInfoFromUser():
    print(":) Enter Expense Info")
    categories = ["work","education","entertainment","food","miscellaneous"]
    expense_amount = int(input("Enter expense Amount: "))
    expense_name = input("Enter expense name:")
    print(" ")
    print("Select Categories")

    for i, value in enumerate(categories):
      print(f"{i +1}. {value}")

    categories_no = int(input("Enter Category corresponding number: ")) - 1

    if categories_no in range(0, len(categories)):
        expense_category = categories[categories_no]
        new_expense = Expense(amount=expense_amount,name=expense_name,category=expense_category)
        return new_expense
    else:
       print("Invalid category. Please try again!")

def savingToCsv(expense:Expense, file_path):
   with open(file_path,"a") as f:
      f.write(f"{expense.amount},{expense.name},{expense.category}\n")

def summerize(budget,file_path):
   def green(text):
    GREEN = '\033[92m'  
    RESET = '\033[0m'  
    return f"{GREEN}{text}{RESET}"
 
   print("🎯Summerized Expenses ")
   expense = []
   with open(file_path, "r") as f:
      lines = f.readlines()
      for line in lines:
         expense_amount,expense_name,expense_categories = line.strip().split(",")
         line_expense = Expense(amount=int(expense_amount),name=expense_name,category=expense_categories)
         expense.append(line_expense)
         # print(line_expense)
         
      amount_by_category={}
      for expenses in expense:
         key = expenses.category
         if key in amount_by_category:
            amount_by_category[key] += expenses.amount
         else:
            amount_by_category[key]= expenses.amount

      print("Expense By Categories:")
      for key,amount in amount_by_category.items():
        print(f"{key:<20} ${amount}")



      total_spent = sum([x.amount for x in expense])
      remaning_budget = budget-total_spent 
      print(f"Your remaning budget is: {green(f'${remaning_budget:.2f}')}")

      today = datetime.now()
      # Calculate the first day of the next month
      if today.month == 12:
         first_day_next_month = datetime(today.year + 1, 1, 1)
      else:
         first_day_next_month = datetime(today.year, today.month + 1, 1)
      
      # Calculate the remaining days in the current month
      remaining_days = (first_day_next_month - today).days
      daily_budget = remaning_budget / remaining_days
      print(f"Your Daily Budget for This Month is:{green(f' ${daily_budget:.2f}')}")

if __name__ == "__main__":
    main()
