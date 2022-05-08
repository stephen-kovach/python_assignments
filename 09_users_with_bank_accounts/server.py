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


    #  [keyword] [method or function_name](self, argument2)
    def withdrawal(self, amount):

        # print(self.balance)

        # self.variable [op] argument2
        self.balance -= amount

        # print(self.balance) 

    #  [keyword] [method or function_name](self, argument1)
    def set_interest(self, amount):

        # print(self.balance)

        # self.variable [op] argument2
        self.int_rate = amount

        # print(self.balance) 
    
    
    # [keyword] [method or function name](self): dtf colon
    def display_account_info(self):
        # [function](f"string text{self.variable -is this an instance?}")
        print(f"Balance: ${self.balance}")

    
    #  [keyword] [method or function_name](self): dtf colon
    def display_interest_rate(self):

        # [function](f"string text{self.variable -is this an instance?}string")
        print(f"The intrest rate is: {self.int_rate}%")

    # [keyword] [method or function_name](self): dtf colon
    def yield_interest(self):

        print(self.balance)

        # I NEED TO DO WRITE AN IF STATEMENT HERE.  HOW DO I DO THAT?  
        # IS 2 LINES BELOW AN EXAMPLE OF INSTANCES?  
        # self.variable [op] self.variable [op] self.variable [ so is line below an instance1 += instance2 * instance1]
        self.balance += self.balance * self.int_rate
        
        print(self.balance)

        # is the line below necessary?  If so, what is it doing?
        return self.balance
    
    # TERM?  BLOCK BELOW IS FOR DIAGNOSTICS
    # is the line below "declaring a class method"?
    @classmethod
    # [keyword] [method or function_name](cls): dtf colon
    def user_population(cls):
        # function_name(f"{cls.class_attribute} text in a string.")
        print(f"{cls.population} users in the program.")

# ///////////////WHAT DO WE CALL THE CODE SECTION ABOVE?

class User:
    # CD ! Class Attribute
    population_nero = 0

    #  CD CONSTRCUTOR FUNCTION!!!  CREATES THE INSTANCE OF AN OBJECT
        # funcion __magicfunction__(self, [parameter?1], [parameter?2]) -or is it arugment1 and arguement2
    def __init__(self, first_name, last_name, age): 
        # self.variable = variable
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # NEW self.[term -what is 'account'] = ClassName(argument1=valuenumber, argument2=valuenumber)  
        self.account = BankAccount(int_rate=0.05, balance =0)  # CD added this line

        # Lines TWO BELOW, DIAGNOSITIC TOOL.  NOT WORKING AS EXPECTED
        # ClassName.[term- class_attribute?] [op] [term -value or number or both?]
        User.population_nero += 1

    #  [keyword] [term -method or function_name or both] (self): dtf colon
    def greeting(self):
        # (f"string text{self.variable -is this an instance?}string")
        print(f"Hello my name is {self.first_name} {self.last_name}!")

#  [keyword] [term -method or function_name or both] (self): dtf colon
    def gimme_the_411(self):
        # (f"string text{self.variable -is this an instance?}string")
        print(f"Hello my first name is {self.first_name}! "
              f"My last name is {self.last_name}! " 
              f"I am {self.age} years old! " 
               # (f"string text{self.[term-variable].[term-argument1], self.[term-variable].[term-argument2]}string")
              f"My account info is {self.account.int_rate, self.account.balance,}!")

    # TERM?  BLOCK BELOW IS FOR DIAGNOSTICS
    # is @term below "declaring a class method"?
    @classmethod
     # [keyword] [method or function_name](cls): dtf colon
    def user_population_nero(cls):
        # function_name(f"{cls.class_attribute} text in a string.")
        print(f"{cls.population_nero} users in the program.")

        # CD your code here! (remember, instance attributes go here)
        # CD don't worry about user info here; we'll involve the User class soon
    



# /////////////////WHAT DO WE CALL THE CODE SECTION BELOW?
            # BACK UP COPY OF LOWER PART COMMENTED OUT UNDERNEATH

# IS THE BELOW CODE NO LONGER NECESSARY?  I LEFT IT IN ANYWAY
# [term -variable?] =ClassName(argument1?, arugment2?)
medici =BankAccount(0.03, 0)
j_morgan =BankAccount(0.05, 1000)
kovach =BankAccount(0.03, 0)

# [term -variable?] = ClassName ("second_argument","third_argument","fourth_argument")
kovach =User ("Stephen", "Kovach", 41)
medici =User ("Lorenzo", "de' Medici", 530)
buffet =User ("Warren", "Buffet", 92)

# FIRST ACCOUNT

# what works:  

# medici.gimme_the_411()

medici.account.deposit(100)
medici.account.deposit(100)
medici.account.deposit(100)
medici.account.withdrawal(50)
medici.account.yield_interest()
medici.account.display_account_info()

# # below are two attempts at chaining--Why are they not working?

#----------------------first attempt at chaining

# medici.account.deposit(100).account.deposit(100).account.deposit(100).account.withdrawal(50).account.yield_interest().account.display_account_info()

#----------------------second attempt at chaining

# medici.account.deposit(100).deposit(100).deposit(100).withdrawal(50).yield_interest().display_account_info()

# SECOND ACCOUNT

# what works

# kovach.gimme_the_411()

kovach.account.deposit(1000)
kovach.account.deposit(1000)
kovach.account.withdrawal(1)
kovach.account.withdrawal(1)
kovach.account.withdrawal(1)
kovach.account.withdrawal(1)
kovach.account.yield_interest()
kovach.account.display_account_info()

# # below are two attempts at chaining--Why are they not working?

#----------------------first attempt at chaining

# kovach.account.deposit(1000).account.deposit(1000).account.withdrawal(1).account.withdrawal(1).account.withdrawal(1).account.withdrawal(1).account.yield_interest().account.display_account_info()

#----------------------second attempt at chaining

# kovach.account.deposit(1000).deposit(1000).withdrawal(1).withdrawal(1).withdrawal(1).withdrawal(1).yield_interest().display_account_info()

# //////////////////
# SENSI BONUS--HOW WOULD I DO IT?
# //////////////////

# COUNTER EXAMPLE j_morgan 

# works:

# j_morgan.display_account_info()
# j_morgan.display_interest_rate()

# doesn't work
# j_morgan.gimme_the_411()

# what works

# j_morgan.deposit(100)
# j_morgan.deposit(100)
# j_morgan.withdrawal(1)
# j_morgan.withdrawal(1)
# j_morgan.withdrawal(1)
# j_morgan.withdrawal(1)
# j_morgan.yield_interest()
# j_morgan.display_account_info()

# below is an attempt at chaining--Why is this not working?

# j_morgan.deposit(100).deposit(100).withdrawal(1).withdrawal(1).withdrawal(1).withdrawal(1).yield_interest().display_account_info()



# # COUNTER EXAMPLE buffet

# buffet.gimme_the_411()

# buffet.account.deposit(1000)
# buffet.account.deposit(1000)
# buffet.account.withdrawal(1)
# buffet.account.withdrawal(1)
# buffet.account.withdrawal(1)
# buffet.account.withdrawal(1)
# buffet.account.yield_interest()
# buffet.account.display_account_info()

# CODE BELOW IS FOR DIAGNOSTICS
# ClassName.[method or function_name](empty)

# BankAccount.user_population()
# User.user_population_nero()

# WHY???  Adds to population_titus and population_nero.  Why Both?
# BankAccount.user_population()

# # ADDS TO population_nero
# User.user_population_nero()

# ALSO SOMETIMES I GET THIS MESSAGE, I THINK IT'S RELATED TO SPACING:
# Traceback (most recent call last):
#   File "/Users/stephenkovach/Desktop/coding_dojo/python/python_assignments/09_users_with_bank_accounts/server.py", line 187, in <module>
#     BankAccount.user_population_titus()
# AttributeError: type object 'BankAccount' has no attribute 'user_population_titus'. Did you mean: 'user_population'?


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