from Product import Product


class Customer:

    def __init__(self, id, name, money):
        self.id = id
        self.name = name
        self.money = money
        self.cart = []

    def buy_product(self, product: Product):
        if product.price < self.money:
            self.cart.append(product)
            self.money -= product.price
        else:
            print(f"{self.name} do not have enough money")
