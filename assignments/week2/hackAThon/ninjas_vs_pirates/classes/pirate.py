class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.stamina = 5

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nStamina: {self.stamina}")

    def attack(self,ninja):
        if self.stamina != 0:
            ninja.health -= self.strength
            self.stamina -= 5
            return self
        else:
            return self

