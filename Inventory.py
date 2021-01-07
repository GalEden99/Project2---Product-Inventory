from Product import Product


class Inventory:

    def __init__(self, products=None):
        if products is None:
            products = {}
        self.products = products

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

    def get_quantity(self):
        count = 0
        for key in self.products.keys():
            count += self.products[key]
        return count
