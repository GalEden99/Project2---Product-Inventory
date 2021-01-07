import Product
from Inventory import Inventory


class Store:
    def __init__(self, inventory: Inventory):
        self.__inventory = inventory

    def sell_product(self, product: Product):
        self.__inventory.products[product] -= 1

    def contain_product(self, product: Product):
        return self.__inventory

    def remove_product(self, orange):
        self.__inventory.remove_product(orange)
