class CardHolder:
    def __init__(self, FirstName, CardNumber, pin, IdNumber, balance):
        self.FirstName = FirstName
        self.CardNumber = CardNumber
        self.pin = pin
        self.IdNumber = IdNumber
        self.balance = balance

# Function to create a new CardHolder instance
def create_cardholder():
    FirstName = input("Enter your first name: ")
    CardNumber = input("Enter your card number: ")
    pin = input("Set your PIN: ")
    IdNumber = input("Enter your ID number: ")
    balance = float(input("Enter your initial balance: "))
    return CardHolder(FirstName, CardNumber, pin, IdNumber, balance)

# Function to write cardholder information to file
def write_to_file(cardholder):
    with open("info.txt", "w") as file:
        file.write(f"Name: {cardholder.FirstName}\n")
        file.write(f"Card number: {cardholder.CardNumber}\n")
        file.write(f"PIN: {cardholder.pin}\n")
        file.write(f"ID number: {cardholder.IdNumber}\n")
        file.write(f"Balance: {cardholder.balance}\n")

# Function to load CardHolder data from file
def load_cardholder_from_file():
    try:
        with open("info.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 5:
                FirstName = lines[0].split(": ")[1].strip()
                CardNumber = lines[1].split(": ")[1].strip()
                pin = lines[2].split(": ")[1].strip()
                IdNumber = lines[3].split(": ")[1].strip()
                balance = float(lines[4].split(": ")[1].strip())
                return CardHolder(FirstName, CardNumber, pin, IdNumber, balance)
    except FileNotFoundError:
        pass
    return None

# Function to print menu
def print_menu():
    print("Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")

# Function for deposit
def deposit(cardholder):
    try:
        deposit_amount = float(input("How much money do you want to deposit: "))
        cardholder.balance += deposit_amount
        print("Deposit successful. New balance:", cardholder.balance)
        write_to_file(cardholder)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Function for withdrawal
def withdraw(cardholder):
    try:
        withdrawal_amount = float(input("How much money do you want to withdraw: "))
        if cardholder.balance < withdrawal_amount:
            print("Not enough balance.")
        else:
            cardholder.balance -= withdrawal_amount
            print("Withdrawal successful. New balance:", cardholder.balance)
            write_to_file(cardholder)
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Function for checking balance
def check_balance(cardholder):
    print("Your current balance is:", cardholder.balance)

# Main function
def main():
    print("Hello ATM!")
    cardholder = load_cardholder_from_file()
    if cardholder is None:
        print("No account found. Let's create one.")
        cardholder = create_cardholder()
        write_to_file(cardholder)
    pin = input("Enter your PIN: ")
    while pin != cardholder.pin:
        print("Incorrect PIN. Please try again.")
        pin = input("Enter your PIN: ")

    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            deposit(cardholder)
        elif choice == '2':
            withdraw(cardholder)
        elif choice == '3':
            check_balance(cardholder)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
