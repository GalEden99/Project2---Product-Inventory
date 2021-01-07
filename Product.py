# Products attributes
class Product:
    # kashrut=boolean
    def __init__(self, name, price, id, kashrut):
        self.__name = name
        self.price = price
        self.id = id
        self.kashrut = kashrut


    def __str__(self):
        return f"{self.__name} costs {self.price} shekels, its id is {self.id}"

    def getName(self):
        return self.__name
# Products
