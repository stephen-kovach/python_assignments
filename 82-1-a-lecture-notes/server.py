
# yo!  so i have an mfa in poetry.  here is a metaphor:

# i am wriring a user manual in the style of WW CKW, WCW, e.e.c and --
            # (without the g.o.)

# I am expecting to have syntax errors, 
    # i am carefully copying, but mistakes happen
    # let's point out those AND
        # answer the questions we're creating in this guide

# i like alfredo's way of spacing because it makes the syntax more legible

# //////////////////////////////////////////////////////////////////////////////////////////////
# LATER ////////////////////////////////////////////////////////////////////////////////////////

# let's make a list of all the errors!

# //////////////////////////////////////////////////////////////////////////////////////////////


# importing from the package called flask
# the following [term?]
        # we can import objects, such as dictionaries
                # and we can import functions 
                # from the python library
                # called flask (with a lower-case)
                    # the difference between flask and Flask is
                        # flask is the package we downloaded --
                            # from which we are importing our [term?]
                        # is Flask the name of the python library? --

        # we are importing:
                # 1 session, which is a dictionart
                    # the purpose of session is to 
                        # keep track of quasi-temporary data
                            # a better word for quasi-temporary data is:
                                # --

                # 2 render_template, which is a function
                        # the purpose of render_template is to
                            # display the template in the browser
                                # a template is an html file that our server.py file directs us to  

                # 3 request, which is a dictionary?
                    # the purpose of request is to:  i don't know

                # 4 redirect, which is a function
                    # the purpose of redirect is to channel the browser to the appropriate url 
                        # a url is the same thing as an address

from flask import session, render_template, request, redirect 

# are we importing flask_app from the library called app?
    # what is the term for flask_app  --is it package?
from flask_app import app

# we are importing the package 
    # called flask_app.models.todo_model
    # and we are importing the library called Todo from the python library
from flask_app.models.todo_model import Todo

                                        # Todo is capitalized because:
                                            # 

# the code block [two words?] below is called a decorator
@app.route( "/" )
@app.route( "/todo/new" )
# we are defining a function called get_todos, 
    # t/f in python, all functions end with parentheses and a colon
def get_all_todos():
    # a conditional statement
    # if the value of the string called "num_of_visits" 
        # help me decribe "in session"
            # in --
            # session -- the function dictionary
    if "num_of_visits" in session:
        
        # the session of [ the value of the [string] called "num_of_visits"] 
            # will increment by one
            # a good way to say += is "increment by 1"
        session[ "num_of_visits" ] += 1
    
    # can I say the else statement this way?: 
    # if the variable/[term?] "num_of_visits" is not in session
        # the value of the variable/term is not incremented by 1
    else:
        session[ "num_of_visits" ] = 1
    
    # I don't understand the following code:  this is my best guess
    # the variable [which is also a --] is assigned the value of the --method/function/both?

                                                        # t/f methods always have parentheses
    list_of_todos = Todo.get_all()

    # we are returning the value/template called "index.html" to the browser
        # help me say the following:
                # first_name is a function/term? that is assigned the value of "Alexander"
                    # this is important because --
                # first_name is a function/term? that is assigned the variable todo_of_todos
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
                                    # the syntax of dotnotion is --
    return render_template( "todoForm.html" )

# this is a decorator 
    # it --directs?-- us to a url, and has an action called post
        # the purpose of a post is to catch data the user inputs through the .html
                # a better way to say "has an action called post" is --
                # a better way to say "catch information" is --
                # t/f a method is always defined inside square brackets
@app.route( "todo/new", methods = [ 'POST' ] )
def create_todo():


    # # toggle
    # # do this when you want to plan, but not finish your functions
    # pass





