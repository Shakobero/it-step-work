from CardHolder import CardHolder  # Importing the CardHolder class from CardHolder.py file

class ATMManager:
    def __init__(self):
        self.cardholder = None  # Initializing the cardholder attribute as None initially

    def create_cardholder(self):
        # Method to create a new cardholder by taking input for personal information
        first_name = input("Enter your first name: ")
        card_number = input("Enter your card number: ")
        pin = input("Set your PIN: ")
        id_number = input("Enter your ID number: ")
        balance = float(input("Enter your initial balance: "))
        self.cardholder = CardHolder(first_name, card_number, pin, id_number, balance)  #
        self.write_to_file()  # Writing the cardholder information to a file

    def write_to_file(self):
        # Method to write cardholder information to a file named "info.txt"
        with open("info.txt", "w") as file:
            file.write(self.cardholder.get_card_info() + f"\nBalance: {self.cardholder.get_balance()}\n")  

    def load_cardholder_from_file(self):
        # Method to load cardholder information from the file "info.txt"
        try:
            with open("info.txt", "r") as file:
                lines = file.readlines()
                if len(lines) == 6:  # Checking if file contains all required information
                    first_name = lines[0].split(": ")[1].strip()  
                    card_number = lines[1].split(": ")[1].strip()  
                    pin = lines[2].split(": ")[1].strip()  
                    id_number = lines[3].split(": ")[1].strip()  
                    balance = float(lines[5].split(": ")[1].strip())  
                    self.cardholder = CardHolder(first_name, card_number, pin, id_number, balance) #creating card holder object information
        except FileNotFoundError:
            pass  # If file is not found, do nothing

    def print_menu(self):
        # Method to print the ATM menu options
        print("Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Exit")

    def deposit(self):
        # Method to handle deposit operation
        try:
            deposit_amount = float(input("How much money do you want to deposit: "))  
            if self.cardholder.deposit(deposit_amount):  # Deposit money into cardholder's account
                print("Deposit successful. New balance:", self.cardholder.get_balance()) 
                self.write_to_file()  
            else:
                print("Invalid input. Please enter a valid amount.")  
        except ValueError:
            print("Invalid input. Please enter a valid amount.")  

    def withdraw(self):
        # Method to handle withdrawal operation
        try:
            withdrawal_amount = float(input("How much money do you want to withdraw: "))  
            if self.cardholder.withdraw(withdrawal_amount):  
                print("Withdrawal successful. New balance:", self.cardholder.get_balance())  
                self.write_to_file()  # Write updated balance to file
            else:
                print("Not enough balance.")  # If withdrawal amount is greater than balance, print error message
        except ValueError:
            print("Invalid input. Please enter a valid amount.")  # If input cannot be converted to float, print error message

    def check_balance(self):
        # Method to check and print the current balance of the cardholder's account
        print("Your current balance is:", self.cardholder.get_balance())

    def validate_pin(self, entered_pin):
        # Method to validate the entered PIN against the cardholder's PIN
        return entered_pin == self.cardholder.pin

    def main(self):
        print("Hello ATM!")
        self.load_cardholder_from_file()  # Load cardholder information from file

        if self.cardholder is None:
            print("No account found. Let's create one.")
            self.create_cardholder()  # If no account found, create a new cardholder

        while True:
            pin = input("Enter your PIN: ")  # Prompt user to enter PIN
            if self.validate_pin(pin):  
                print("Welcome back,", self.cardholder.first_name) 
                break  # Exit PIN validation loop
            else:
                print("Incorrect PIN. Please try again.")  # If PIN is incorrect, print error message

        while True:
            self.print_menu()  # Print ATM menu
            choice = input("Enter your choice: ")  
            if choice == '1':
                self.deposit()  
            elif choice == '2':
                self.withdraw()  
            elif choice == '3':
                self.check_balance()  
            elif choice == '4':
                print("Exiting...")  
                break  
            else:
                print("Invalid choice. Please try again.")  

if __name__ == "__main__":
    manager = ATMManager()
    manager.main()  # Run the ATM program if the script is executed as the main program
