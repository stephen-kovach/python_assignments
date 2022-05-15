
class User:		# CD here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # CD adding the deposit method

    # [keyword] function_name(self, arguement1)
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, nero_other_user, amount):
        self.account_balance -= amount
        nero_other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
monty.make_deposit(100)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

monty.make_withdrawal(50)
print(guido.account_balance)	
print(monty.account_balance)	

monty.display_user_balance()
guido.display_user_balance()

guido.transfer_money(monty, 50)


monty.display_user_balance()
guido.display_user_balance()

francis = User('Ajax', 'ajax@supervillian.org')
print(francis.name)
print(francis.account_balance)
francis.make_deposit(500)
print(francis.account_balance)
francis.make_deposit(-300)
print(francis.account_balance)