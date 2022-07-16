from nis import cat


class Ninja:
    def __init__(self,firstName,lastName,treats,petFood,pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def bathe(self):
        self.pet.noise()
    def feed(self):
        self.pet.eat()
        return self
    def addPet(self):
        pass

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        pass
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound
class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.type = "cat"
class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.type = "dog"

pet1 = Cat("frankie","dog","shake")
ninja1 = Ninja("jackie","chan","kibble","purina", pet1)

pet1.sleep()
print(pet1.energy)

ninja1.walk().feed()
print(pet1.energy)