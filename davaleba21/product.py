import json

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['price'], data['quantity'])

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

def serialize_products(products, filename):
    with open(filename, 'w') as file:
        json.dump([product.to_dict() for product in products], file, indent=4)

def deserialize_products(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return [Product.from_dict(product_data) for product_data in data]

# Creating some product objects
products = [
    Product("Laptop", 1000, 5),
    Product("Phone", 800, 10),
    Product("Headphones", 100, 20)
]

# Serialize products to a file
serialize_products(products, 'products.json')

# Deserialize products from the file
deserialized_products = deserialize_products('products.json')

# Print information of all products
for product in deserialized_products:
    print(product)
