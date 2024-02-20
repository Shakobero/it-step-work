def commission_deduction(func):
    def wrapper(balance, amount):
        commission = 1
        if balance >= amount + commission:
            return func(balance - amount - commission, amount)
        else:
            raise ValueError("Insufficient funds for the transaction")
    return wrapper

@commission_deduction
def transaction(balance, amount):
    return balance  

try:
    # Request for money for the customer
    balance = float(input("Enter your current balance: "))
    amount_to_pay = float(input("Enter the amount to be paid: "))

    # Display the transaction
    new_balance = transaction(balance, amount_to_pay)
    print("Transaction successful. New balance:", new_balance)
except ValueError as e:
    print("Error:", e)
