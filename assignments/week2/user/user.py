# declare a class and give it name User
class User:		
    def __init__(self,first_name,last_name,age):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42

michael = User("Michael", "Clayton", 56)
anna = User("Anna", "Wintor", 69)

print(michael.age)

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
