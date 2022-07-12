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
        return self

    def enroll(self):
        self.is_rewards_member = self.is_rewards_member = True
        return self

    def spend_points(self,amount):
        if self.gold_card_points <= amount:
            print("Don't have enough points")
        else: 
            self.gold_card_points = self.gold_card_points - amount
        return self

michael = User("Michael", "Clayton", "michael@gmail.com", 56)
anna = User("Anna", "Wintor","anna@gmail.com", 69)
joey = User("Joey", "Joey", "joey@gmail.com", 34)

michael.display_info().enroll().spend_points(50).spend_points(25).display_info()
anna.spend_points(25).display_info()