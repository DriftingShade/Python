class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f" First Name: {self.first_name}\n Last Name: {self.last_name}\n Email: {self.email}\n Age: {self.age}\n Rewards Member: {self.is_rewards_member}\n Point Balance: {self.gold_card_points}")
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self, amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("Sorry, you don't have enough points!")

shane = User("Shane", "Nosack", "sarus333@yahoo.com", 32)
user2 = User("Bob", "Evans", "someemail@email.com", 45)
user3 = User("Michael", "Jordan", "mike23@bulls.net", 52)
