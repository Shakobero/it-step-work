class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def apartment_sale(self, buyer, loan=None):
        if loan is None:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
            print(f"The apartment {self.ID} has been sold to {buyer.name}.")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold on loan"
            buyer.loan += loan
            print(f"The apartment {self.ID} has been sold to {buyer.name} with a loan of {loan}.")

# Creating two Person objects
owner = Person("DATO")
buyer = Person("NIKA")

house = House("123456", 200000, owner)

print("Before sale:")
print(owner)
print(buyer)
print(house.owner)
print()

house.apartment_sale(buyer)

print("\nAfter sale:")
print(owner)
print(buyer)
print(house.owner)
