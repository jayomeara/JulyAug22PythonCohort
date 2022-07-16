class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.stamina = 25
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\nStamina: {self.stamina}")

    def attack(self,pirate):
        if self.stamina != 0:
            pirate.health -= self.strength
            self.stamina -= 5
            return self
        else:
            return self