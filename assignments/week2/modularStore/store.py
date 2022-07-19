class Products:
    listProducts = []
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Products.listProducts.append(self)
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = float(self.price) * float(percent_change)
            return self
        elif is_increased == False:
            self.price = float(self.price) * float(percent_change)
            return self
        else:
            return self
    def print_info(self):
        print(f"I am a", self.name, "I cost", self.price, "and I'm a", self.category)
        return self
@classmethod
def print_list(cls):
    print(f"All products: {cls.listProducts}")

class Store:
    def __init__(self, name) -> None:
        self.name = name
        # self.product = Products(name,price,category)
    def add_product(self, new_product):
        listProducts.append(new_product)
        return self
    def sell_product(self, id):
        listProducts.pop[id]
        return self
    def inflation(self, percent_increase):
        self.price = float(self.price) * float(percent_increase)
        return self
    def set_clearance(self, category, percent_discount):
        if category == self.product.category:
            self.price = float(self.price) * float(percent_discount)
            return self
        else:
            return self

product1 = Products("Slime", 12.99, "toys")
# store1 = Store('hyVee')

product1.update_price(.9, False)
product1.print_info()
product1.print_list()
