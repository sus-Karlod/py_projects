class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.load_expenses()
        
    def add_expenses(self):
        items = input("Enter expenses to add : ")
        amount = float(input("Enter the amount of items : "))
        expense =  {"Item" : items, "Price" : amount}

        self.expenses.append(expense)
        print(f"Expense : {items}. Price : {amount}" )
        self.save_expenses()

    def view_expenses(self):
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. {expense}")

    def total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense["Price"]
        print(f"Total expenses : {total}")

    def save_expenses(self):
        with open("expenses.txt", "w") as file:
            for expense in self.expenses:
                file.write(f"{expense['Item']}, {expense['Price']}\n")

    def load_expenses(self):
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    item, price = line.strip().split(",")
                    self.expenses.append({"Item": item, "Price": float(price)})
        except FileNotFoundError:
            self.expenses = []

tracker = ExpenseTracker()
while True:
    print("\n1. Add Expense\n2. View Expense\n3. Total Expense\n4. Exit")
    choice = input("Choose an option : ")

    if choice == "1":
        tracker.add_expenses()
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        tracker.total_expenses()
    elif choice == "4":
        print("Thanks for visiting...!")
        break
    else:
        print("Invalid option, try again")