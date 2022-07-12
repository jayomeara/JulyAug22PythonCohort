class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 50
    # Can't have default vales for required conditionals
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_rewards_member, self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = self.is_rewards_member = True

    def spend_points(self,amount):
        if self.gold_card_points <= amount:
            print("Don't have enough points")
        else: 
            self.gold_card_points = self.gold_card_points - amount

michael = User("Michael", "Clayton", "michael@gmail.com", 56)
anna = User("Anna", "Wintor","anna@gmail.com", 69)
joey = User("Joey", "Joey", "joey@gmail.com", 34)

michael.display_info()
michael.enroll()
michael.spend_points(50)
anna.spend_points(25)
michael.display_info()
anna.display_info()

# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
#     	# we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         # the status is set to True by default
#         self.in_stock = True
    
#     # Takes a float/percent as an argument and reduces the
#     # price of the item by that percentage.
#     def on_sale_by_percent(self, percent_off):
#         self.price = self.price * (1-percent_off)
