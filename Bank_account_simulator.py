class Bank_account():

    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposit{amount}. New_balance : {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn{amount}. New_balance : {self.balance}")
        else:
            print("Insufficient balance")  

my_account = Bank_account("6769", 15000)
print(f"Account Number : {my_account.account_no}")
print(f"Current Balance : {my_account.balance}")    

while True:
    print("\n1. Check Balance\n2. Deposit\n3 Withdraw\n4. Exit")

    choice = (input("Enter an option :"))

    if choice == "1":
        print(f"Balance: {my_account.balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit :"))
        my_account.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw :"))
        my_account.withdraw(amount)
    elif choice == "4":
        print("Thank you for coming...")
        break
    else:
        print("Invalid choice, try again")