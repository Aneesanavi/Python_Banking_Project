class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.display_balance()
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.display_balance()
        else:
            print("Invalid withdrawal amount or insufficient balance.")

def main():
    print("Welcome to the Banking System")
    account_number = input("Enter your account number: ")
    account_holder = input("Enter your account holder name: ")

    
    current_account = BankAccount(account_number, account_holder)

    while True:
        print("\nMenu:")
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option (1/2/3/4): ")

        if choice == "1":
            current_account.display_balance()
        elif choice == "2":
            amount = float(input("Enter the deposit amount: $"))
            current_account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: $"))
            current_account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
