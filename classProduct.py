# Products attributes 
class Product:
    # kashrut=boolean
    def __init__(self, name, price, id, kashrut, quantity):
        self.name = name
        self.price = price
        self.id = id
        self.kashrut = kashrut
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} costs {self.price} shekels, its id is {self.id}"

# Products
orange = Product("Orange", 5, 1, True, 20)
apple = Product("Apple", 4, 2, True, 20)
shrimp = Product("Shrimp", 50, 3, False, 20)
bread = Product("Bread", 10, 4, True, 20)
eggs = Product("Eggs", 12, 5, True, 20)
