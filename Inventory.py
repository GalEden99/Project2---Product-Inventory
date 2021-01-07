from Product import Product


class Inventory:

    def __init__(self, products=None, quantity=0):
        if products is None:
            products = {}
        self.products = products
        self.quantity = quantity

    def add_product(self, product: Product):

        if product in self.products:
            self.products[product] += 1
        else:
            self.products[product] = 1
            # self.product.quantity += 1

    def remove_product(self, product: Product):
        if self.contain_product(product):
            self.products[product] -= 1

    def contain_product(self, product: Product):
        return product in self.products



    # def sellings(self):
    #     selling = int(input(f"How mach {self.name} do you want to sell?"))
    #     self.quanity -= selling
    #
    # def purchase(self):
    #     purchase = int(input(f"How mach {self.name} do you want to purchase?"))
    #     self.quanity += purchase
