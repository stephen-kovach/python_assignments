# # declare a class and give it name User
# # class User:		
# #     def __init__(self):
# #         self.name = "Michael"
# #         self.email = "michael@codingdojo.com"
# #         self.account_balance = 0

# # User()
# # guido = User()
# # monty = User()
# # # Accessing the instance's attributes
# # print(guido.name)	# output: Michael
# # print(monty.name)	# output: Michael

# # guido.name = "Guido"
# # print(guido.name) # output: Guido
# # monty.name = "Monty"
# # print(monty.name) # output: Monty

# class User:
# # declaring a class attribute
# bank_name = "First National Dojo"		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# guido = User()
# monty = User()
# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union 
# print(monty.bank_name) # output: First National Dojo


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

guido = User("vc", "d@aol.com")
monty = User("vcd", "dd@aol.com")

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50


