class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 20
        self.energy = 20

    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health += 5
    def noise(self):
        print("Woof Woof!")

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
    def noise(self):
        print("Meow Meow!")