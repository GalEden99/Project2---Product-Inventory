from Inventory import Inventory
from Product import Product
from customer import Customer
from store import Store



def get_products():
    return [Product("Orange", 5, 1, True),
            Product("Apple", 4, 2, True),
            Product("Shrimp", 50, 3, False),
            Product("Bread", 10, 4, True),
            Product("Eggs", 12, 5, True)]


def build_inventory(inventory: Inventory, products):
    for product in products:
        inventory.add_product(product)


def buy_and_sell_product(product):
    store.sell_product(products[0])
    customer.buy_product(products[0])




if __name__ == '__main__':
    products = get_products()  # [Product("Orange", 5, 1, True), Product("Apple", 4, 2, True),...]
    inventory = Inventory()
    build_inventory(inventory, products)
    # print(inventory.get_quantity())
    store = Store(inventory)
    customer = Customer(1, "Gil", 100)
    print(customer.money)
    buy_and_sell_product(products[0])
    print(customer.money)
