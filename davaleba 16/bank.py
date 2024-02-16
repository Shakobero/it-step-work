class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Method to deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Invalid deposit amount. Please enter a positive number.")
            return False

    def withdraw(self, amount):
        """Method to withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            return False

# Create multiple bank accounts
account1 = BankAccount("001", "Alice")
account2 = BankAccount("002", "Bob", 1000)

# Perform transactions
account1.deposit(500)
account2.withdraw(200)
account2.deposit(300)
account1.withdraw(100)

# Print final balances
print(f"Account {account1.account_number} balance: ${account1.balance}")
print(f"Account {account2.account_number} balance: ${account2.balance}")
