from pet import Pet
from pet import Cat

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet=None):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

zeek = Pet("Zeek", "Dog", "fetch")

muffy = Cat("Muffy", "Cat", "plop trick")

shane = Ninja("Shane", "Nosack", treats=5, pet_food=10, pet=zeek)
brianna = Ninja("Brianna", "Nosack", treats=5, pet_food=10, pet=muffy)

shane.walk().feed().bathe()

print(zeek.health)
print(zeek.energy)

brianna.walk().feed().bathe()

print(muffy.health)
print(muffy.energy)