class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


emir = User("Emir")
kenny = User("Kenny")
sam = User("Sam")
bema = User("Ms Bema")

emir.make_deposit(20000).make_deposit(1500).make_deposit(500).make_withdrawl(300).display_user_balance()

kenny.make_deposit(10000).make_deposit(2550).make_withdrawl(500).make_withdrawl(800).display_user_balance()

bema.make_deposit(15000).make_withdrawl(2000).make_withdrawl(5000).make_withdrawl(3000).display_user_balance()
sam.make_deposit(18000).make_withdrawl(1500).make_withdrawl(2000).make_withdrawl(500).display_user_balance()


sam.transfer_money(6000, emir)
emir.transfer_money(12000, bema)