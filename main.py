from Inventory import Inventory
from Product import Product
from store import Store

inventory = Inventory()

orange = Product("Orange", 5, 1, True)
apple = Product("Apple", 4, 2, True)
shrimp = Product("Shrimp", 50, 3, False)
bread = Product("Bread", 10, 4, True)
eggs = Product("Eggs", 12, 5, True)

print(inventory.products)
inventory.add_product(orange)
inventory.add_product(apple)
inventory.add_product(apple)

store = Store(inventory)

if store.contain_product(orange):
    store.remove_product(orange)

print(inventory.products)

#
# print(orange.id)
# print(orange.getName())