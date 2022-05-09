# AM I USING THE RIGHT TERMS?  STILL NOT IDENTIFYING INSTANCES

class BankAccount:

    # class_attribute = [term -value or number or both?]
    population = 0
    # CD don't forget to add some default values for these parameters!
    
    # funcion __magicfunction__(self, [parameter?1], [parameter?2]) -or is it arugment1 and arguement2
    def __init__(self, int_rate, balance): 
        # self.variable = variable
        # self.name = name  INITIALLY TRIED, BUT IT WAS WRONG, NOT ENOUGH ARGUMENTS
        self.int_rate = int_rate
        # self.variable = value - INITIALLY SET SELF.BALANCE TO 0 BUT THAT WAS WRONG
        # HOW IS LINE BELOW DIFFERENT THAN LINE 8?
        self.balance = balance
        # 2 LINES BELOW:  WHY DOES THIS INDENTATION WORK?
        # ClassName.[term- class_attribute?] [op] [term -value or number or both?]
        BankAccount.population += 1

        # CD your code here! (remember, instance attributes go here)
        # CD don't worry about user info here; we'll involve the User class soon
    
    #  [keyword] [term -method or function_name or both] (self, argument2)
    def deposit(self, nero_amount):

        # function(self.variable) 
        # print(self.balance)

        # self.variable operator argument2
        self.balance += nero_amount

        # function(self.variable)
        # print(self.balance) 

        return self  # CODE NECESSARY FOR CHAINING


    #  [keyword] [method or function_name](self, argument2)
    def withdrawal(self, amount):

        # print(self.balance)

        # self.variable [op] argument2
        self.balance -= amount

        # print(self.balance) 

        return self  # CODE NECESSARY FOR CHAINING

# CODE BLOCK BELOW WORKED ON 5/7 & 5/8 WHY NOT NOW?
    
    # [keyword] [method or function name](self): dtf colon
    def display_account_info(self):
        # [function](f"string text{self.variable -is this an instance?}")
        # print(f"Balance: ${self.balance}!")
        print(self.balance)

        return self  # CODE NECESSARY FOR CHAINING
    
    #  [keyword] [method or function_name](self): dtf colon
    def display_interest_rate(self):

        # [function](f"string text{self.variable -is this an instance?}string")
        # print(f"The intrest rate is: {self.int_rate}%")
        print(self.int_rate)

        return self  # CODE NECESSARY FOR CHAINING

    # [keyword] [method or function_name](self): dtf colon
    def yield_interest(self):

        print(self.balance)

        # I NEED TO DO WRITE AN IF STATEMENT HERE.  HOW DO I DO THAT?  
        # IS 2 LINES BELOW AN EXAMPLE OF INSTANCES?  
        # self.variable [op] self.variable [op] self.variable [ so is line below an instance1 += instance2 * instance1]
        self.balance += self.balance * self.int_rate
        
        print(self.balance)

        # # is the line below necessary?  If so, what is it doing?
        # return self.balance
    
        return self  # CODE NECESSARY FOR CHAINING

    # TERM?  BLOCK BELOW IS FOR DIAGNOSTICS
    # is the line below "declaring a class method"?
    @classmethod
    # [keyword] [method or function_name](cls): dtf colon
    def user_population(cls):
        # function_name(f"{cls.class_attribute} text in a string.")
        # print(f"{cls.population} users in the program.")
        print(cls.population)

# ///////////////WHAT DO WE CALL THE CODE SECTION ABOVE?

# /////////////////WHAT DO WE CALL THE CODE SECTION BELOW?
            # BACK UP COPY OF LOWER PART COMMENTED OUT UNDERNEATH

# [term -variable?] =ClassName(argument1?, arugment2?)
medici =BankAccount(0.03, 0)
j_morgan =BankAccount(0.05, 1000)
buffet =BankAccount(0.02, 2000)
guido =BankAccount(0.03, 0)
# # [term -variable?].function_name(argument2? -what is the parentheis?)
# j_morgan.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_intrest().display_account_info() 

# FIRST ACCOUNT


medici.display_account_info()
medici.display_interest_rate()

# what works

# medici.deposit(100)
# medici.deposit(100)
# medici.deposit(100)
# medici.withdrawal(50)
# medici.yield_interest()
# medici.display_account_info()

# below is an attempt at chaining--Why is this not working? BECAUSE DIDN'T RETURN SELF

medici.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()

# SECOND ACCOUNT


buffet.display_account_info()
buffet.display_interest_rate()

# what works

# buffet.deposit(100)
# buffet.deposit(100)
# buffet.deposit(100)
# buffet.withdrawal(50)
# buffet.yield_interest()
# buffet.display_account_info()

# below is an attempt at chaining--Why is this not working? BECAUSE DIDN'T RETURN SELF

buffet.deposit(1000).deposit(1000).withdrawal(25).withdrawal(50).withdrawal(1).withdrawal(1).yield_interest().display_account_info()

# # THIRD ACCOUNT

# j_morgan.display_account_info()
# j_morgan.display_interest_rate()

# # what works

# # j_morgan.deposit(100)
# # j_morgan.deposit(100)
# # j_morgan.withdrawal(1)
# # j_morgan.withdrawal(1)
# # j_morgan.withdrawal(1)
# # j_morgan.withdrawal(1)
# # j_morgan.yield_interest()
# # j_morgan.display_account_info()

# # below is an attempt at chaining--Why is this not working?

# j_morgan.deposit(100).withdrawal(1).withdrawal(1).withdrawal(1).yield_interest().display_account_info()

# NINJA BONUS:  What is it asking me to do?  How would I do it?  


# CODE BELOW IS FOR DIAGNOSTICS
# ClassName.[method or function_name](empty)
BankAccount.user_population()




# ////////

# BELOW:  COMPARE THIS CODE TO 07_chaining_methods line 31
# what's the difference?

# guido.deposit(100)
# guido.deposit(100)
# guido.display_account_info()

# guido.withdrawal(25)
# guido.withdrawal(25)
# guido.display_account_info()

# guido.deposit(100).display_account_info()
# # [term -variable?].function_name(empty)
# phormio.display_account_info()

# # [term -variable?].function_name(empty)
# phormio.yield_interest()
# buffet.yield_interest()

# # [term -variable?].function_name(empty)
# phormio.display_account_info()
# buffet.display_account_info()


# # [term -variable?].function_name(empty)
# phormio.display_interest_rate()
# buffet.display_interest_rate()







# //////////////////////////
# FIRST BACK UP CODE

# # [term -variable?] =ClassName(argument1?, arugment2?)
# j_morgan =BankAccount(0.03, 10000)
# medici =BankAccount(0.01, 300)
# phormio =BankAccount(0.03, 100)
# buffet =BankAccount(0.50, 1000)
#         # line 54 is printing on line 77 UNEXPECTED

# # # [term -variable?].function_name(argument2? -what is the parentheis?)
# buffet.deposit(800)
# phormio.deposit(300)

# # # [term -variable?].function_name(empty)
# phormio.display_account_info()

# # # [term -variable?].function_name(empty)
# phormio.yield_interest()
# buffet.yield_interest()

# # ClassName.[method or function_name](empty)
# BankAccount.user_population()

# # # [term -variable?].function_name(empty)
# phormio.display_account_info()
# buffet.display_account_info()


# # # [term -variable?].function_name(empty)
# phormio.display_interest_rate()
# buffet.display_interest_rate()

# # ClassName.[method or function_name](empty)
# BankAccount.user_population()