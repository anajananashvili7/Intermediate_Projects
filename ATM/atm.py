class BankAccount:
    def __init__(self, pin, balance=0):
        self.pin = pin  # PIN code
        self.balance = balance  # initial balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

def atm_system():
    print("Welcome to the ATM")
    
    # Example pin and account balance
    user_account = BankAccount(pin="1234", balance=1000)
    
    # PIN verification
    pin_input = input("Please enter your PIN: ")
    if pin_input != user_account.pin:
        print("Incorrect PIN. Exiting...")
        return

    # Menu loop
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1/2/3/4): ")
        
        if choice == "1":
            print(f"Your balance is: ₾{user_account.check_balance()}")
        
        elif choice == "2":
            try:
                amount = float(input("Enter the amount to deposit: ₾"))
                if user_account.deposit(amount):
                    print(f"Deposited ₾{amount}. Your new balance is ₾{user_account.check_balance()}")
                else:
                    print("Invalid deposit amount!")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            try:
                amount = float(input("Enter the amount to withdraw: ₾"))
                if user_account.withdraw(amount):
                    print(f"Withdrew ₾{amount}. Your new balance is ₾{user_account.check_balance()}")
                else:
                    print("Insufficient balance or invalid amount!")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    atm_system()
