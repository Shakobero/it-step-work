class CardHolder:
    def __init__(self, first_name, card_number, pin, id_number, balance):
        # Constructor method to initialize a CardHolder object with provided attributes
        self.first_name = first_name  
        self.card_number = card_number 
        self.pin = pin  
        self.id_number = id_number  
        self.balance = balance  

    def deposit(self, amount):
        try:
            deposit_amount = float(amount)  
            if deposit_amount > 0:  
                self.balance += deposit_amount  
                return True  
            else:
                return False  
        except ValueError:
            return False  

    def withdraw(self, amount):
        try:
            withdrawal_amount = float(amount)  # Convert withdrawal amount to float
            if withdrawal_amount > 0 and self.balance >= withdrawal_amount:
                # Check if withdrawal amount is positive and if there's enough balance
                self.balance -= withdrawal_amount 
                return True  
            else:
                return False  
        except ValueError:
            return False  

    def get_balance(self):
        return self.balance 

    def get_card_info(self):
        # Return formatted string containing card holder's information
        return f"Name: {self.first_name}\nCard number: {self.card_number}\nID number: {self.id_number}"
