
# 2022-06-21 19:24
    # i'm teaching myself to think in military time!

# this is code is from Johnathan Cisneros

    # HUGE shoutout for the code, could never have made this manual without it!

    # who is your favorite comedian?
    # 
    # 
 
#  so i have an mfa in poetry.  here is a metaphor:

# i am wriring a user manual in the style of WW CKW, WCW, e.e.c and --
            # (without the readAnEssayCalledPoliticsOfTheEnglishLanguage)

# I am expecting to have syntax errors, 
    # i am carefully copying, but mistakes happen
    # let's point out my syntax errors 
    #   
    #   AND
        
    # answer the questions we're creating in this guide

# also

    # i will be rephrasing code as i go in different ways

        # i cannot understand the code if i can't talk about it 

# btw, i like alfredo's way of spacing because it makes the syntax more legible

# //////////////////////////////////////////////////////////////////////////////////////////////
# LATER ////////////////////////////////////////////////////////////////////////////////////////

# let's make a list of all the errors!:

    # 1. TypeError
    # 2. KeyError
    # 3. ---
    # 4. ---

# //////////////////////////////////////////////////////////////////////////////////////////////
# LATER //////////////////////////////////////////////////////////////////////////////////////// 

# help me read the code from github, am I copying everything in the right place?

# am i modularizing correctly so far?

# //////////////////////////////////////////////////////////////////////////////////////////////
# FIRST THING'S FIRST //////////////////////////////////////////////////////////////////////////

# the purpose of the server.py file is to

    # -- depending on the context, user cr it's app routes
        # it's where we use flask the most
            # create an app
            # it
            # 
# so let's talk about line first line of code!

# /f this line of code has a name
            # we are just importing flask

# t-- we are importing from the package called (lower-case) flask       

        # t/f the first line of code is importing functions --only--

                # Flask is toolbox, and the screenshot hammer wrench etc
        # t/f we are importing these functions from the package called flask
                
                # the difference between flask and Flask is 

                        # flask (with a lowercase letter) is the package we downloaded at the beginning of the course

                            # and 

                        # flask is the module from which we are importing the functions

                    # on the other hand, 

                    # a concise summary of Flask (with a capital letter) is

                        # web framework to produce web applications with python
                            # we can call module a library, a library of functions

        # We are importing four functions

                # 1 session, which is a function BUT it operates as a dictionary, it takes key-value pairs
                    # t-- the purpose of session is to: 
                        # keep track of quasi-temporary data
                            # a better way to say quasi-temporary data is:
                                # it is a global variable

                                    # once you load something in session it can be used

                                        # it is cached information made during the session 

                                            # and the reason this is important is the is lost after we're logged out
                                                # like cookie, just tracking variables
                                            # that why we uyse session in validation 
                # 2 render_template, which is a function
                        # t  the purpose of render_template is to:
                            # display the template in the browser
                                # define parse
                                    # parse verb

                                        # analyzing reading lines and words

                                            # translating 
                                                # jinja and html
                                                # so python can read the jinja and html that the browser can understands 

                                                    # connect to database kinda like a bridge
                                    # running through the lines of code and
                                        # jinja
                                        # html
                                            # reading the code into lanugage the browser 

                        # t a template is the same thing as an html file 
                        # t/f one of the four --functions-- we are importing is render_template
                        # t/f we need to write render_template in the first line of code in order to use it later in the code
                                    # t/f and that's the whole point of the first line of code  

                # 3 a request object, is an instance of a Request
                    
                    # a concise summary of request is:  
                    
                        # will redirect to a route we provide 

                # 4 redirect, which is a function
                
                    # t/f the purpose of redirect is to channel the browser to the appropriate url 
                    # t/f a url, routes and address all mean the same thing
                            # if not
                                # url -- 
                                # routes --
                                # address --

from flask import session, render_template, request, redirect 

    # session is doing some heavy-lifting
        # like a function, but not

        # it is an instance 


# second line!

# t/f we importing flask_app from the library called app

    # t/f term for flask_app is package
    # t/f flask_app is in snake_case AND it is not a function
from flask_app import app

# t/f we are importing the package called flask_app.models.todo_model
# t/f we are importing frp, the library in Python called Todo from the python library
from flask_app.models.todo_model import Todo

                                        # Todo is capitalized because:
                                            # 
# summary: 

# the reason we need to 4 lines of code starting with from xx import xx is because:

    # 

# we are done importing and we are about to start coding our routes

        # t/f the section of code above has a term
                # if true, it is called a --

        # t/f the section of code below has a term
                # if true, it is called a --

# t/f the route, url, and address are synonyms 

# t/f the code block below is called a decorator
@app.route( "/" )
@app.route( "/todo/new" )
# we are defining a function called get_todos, 
    # t/f in python, all functions end with parentheses and a colon ():
def get_all_todos():
    # t/f the code below is a conditional statement
            # it says
                # if the value of the string called "num_of_visits" 
                    # a better way to say that is 

                    # -- 
        
                # help me decribe the "in session" part of the for loop
                # 'in' means --
                # 'session' means-- 

                # the reason we import session on the first line is because
                    
                    # --
 
    if "num_of_visits" in session:
        
    # t/f the session of [ the value of the [string] called "num_of_visits"] 
            # will increment by one
            # a good way to say += is "increment by 1" or "plus equals" or both
        session[ "num_of_visits" ] += 1
    
    # t/f the code snippet below is an else statment and syntactically
            # session will always be --term/declared?-- as an if/else statement
            # t/f, a sessions statement will never contain an elif statement
    # t/f  if the value of string called "num_of_visits" is not in session
        # the value of the --term/idk-- will not be incremented by 1

        # --    

    else:
        session[ "num_of_visits" ] = 1

        # a concise defintion of session is 

            # --
    
    
    # t/f in the code below, the variable [which is also a --] is assigned the value of the --method/function/both?

                                                        # t/f methods always have parentheses
    list_of_todos = Todo.get_all()

    # t/f we are returning the value/template called "index.html" to the browser
        # help me say the following:
                # --the?-- first_name is a function/term? that is assigned the value of "Alexander"
                    # this is important because --
                # --the?-- list_of_todods is a function/term? that is assigned the variable todo_of_todos
                    # this is important because --
                    # the difference between list of todos on the left and on the right is
                        # the left is a function
                            # this is what it is doing --
                        # the right is variable
                            # this is what it is doing --

    return render_template( "index.html", first_name = "Alexander", list_of_todos = list_of_todos )

@app.route( "/todo/new" )
# the reason we can repeat the url in different -decorators?- without an error is because:
                                                    # 
                                                    # 
def display_create_todo():          
    # we are returning the output of the fucntion called render_template
                        # the value of the function is a strong called "todoForm.html"
                        # the name of the template is "todoForm.html"
                        # this is dot notation
                                    # the syntax of dot.notion is --
    return render_template( "todoForm.html" )

# this is a decorator 
    # it --term/'directs'?-- us to a url, and has an action called post
        # the purpose of a post is to catch data the user inputs through the .html
                # a better way to say "has an action called post" is --
                # a better way to say "catch information" is --
                # t/f a method is always defined inside square brackets
@app.route( "todo/new", methods = [ 'POST' ] )
def create_todo():

    # we are [not calling, what the's verb] the method/library called request.form
       # request.form is related to the "request" 
                                # there's a relationship, right? what is it?
                                # --
    Todo.create(request.form)
        # t/f the above code is NOT dot notation! mwahahaha!

    # we are returning the output of the string/template/both
        # a quick definition of redirect is --
        
    return redirect( "/todos" )
    # # --toggle--
    # # do this when you want to plan, but not finish your functions
    # pass


# what should I notice about this url?:  

# http://127.0.0.1:5000

# this url is significant because --

        # the value of our port is not 5000, it is 5001
            # this is important to know because it is not the default
                                            # which is 5000
                                            # our port number is different because
                                                # --
# is this a condtional statement or something_else?
# if the constructor function called __name__ is equal to the value 
                # of the string called "__main__"
                # "__main__" looks like a constructor function because --
                # this line ends with a colon because:
                        # t/f all functions in python end in colons
if __name__ == "__main__":
    app.run(debug = True, port =5001)

# the reason there are aren't any decorators in server.py
        # is related to modularization
                # AND 

# ---

