
# 81-_6-10_lecture_html_table/server.py


# RECAP:

# lines 66-69, different error message

# Next Goals:

# importing flask from templates folder, why render_template here again?
# what's the difference betweem lowercase and uppercase flask/Flask?

                        # we are importing a [template?] is that differnet than "rendering the template"
                        # are we importing request and direct from flask?
                            # what does that mean?
                        # are request and a redirect functions?, if not, what are they called?
                                                    # are they "action routes?"
                                        
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# can we summarize what is going on here?
list_todos = [
    {
        "todo" : "Learn templates in flask",
        "status" : "Complete"
    # close curly brace, comma
    },
    {
        "todo" : "Learn Object Orientened Programming",
        "status" : "Complete"
    # close curly brace, comma
    },
        {
        "todo" : "Learn Deployment",
        "status" : "Complete"
    # close curly brace, comma
    }
]

@app.route('/hello')
def hello_from_flask():
    return "Hello class!  This message is coming from your server in flask"

@app.route( '/goodbye/class' )
def goodbye_from_flask():
    return "<h1>Cancel Elvis</h1><h3>Chaplin</h3><h3>But not the Ramones</h3>"
    # why does the string in the return statement have an h1, 
        # is that creating html in python?   like a reverse jinja?

# why are we converting the number into the string?
@app.route('/number/<string:num>')
        # we are defining a function and we are [defining?] the parameter [num]
def print_number(num):
        # code below is a diagnostic tool.  
            # it is printing [arguments?] in our terminial 
            # it is printing a the string and the variable [inputs from the url?]
                # into the terminal 
    print( "=====Number sent from url:", num )
    # we are returning a string and [term for curly braces?]
    return f"Your number is {num}"
    # Can we summarize how the variable num is dynamic? 

# why would we place this at the bottom?  
# and why is it not working?---because I forgot the = 
@app.route('/')
@app.route('/home')
def home():
    # first_name is called what?  it is sending the string "Marcus"
    return render_template ( "index.html", first_name = "Marcus", list_todos = list_todos )

                    # Methods are actions
                    #  GET is always the Default, hard coding is fine but it's implied 
                    # The definition of GET is: Display route?
                    # get doesn't need to be capitalized, is it a NMCV?


@app.route( "/todo/new" )
def display_create_todo():
    return render_template( "todoform.html" )

# can a url be reused if it has a different method?  If yes, why would we do that?
@app.route( "/todo/new", methods = [ 'POST' ] ) 
def create_todo():
    pass

@app.route( "/todo/new" )
def display_create_todo():
    return render_template( "todoForm.html" )




@app.route('/nero', methods = [ 'GET' ])
def create_nero2():
    return 'Sorry Mom!'

if __name__=="__main__":
    app.run(debug=True, port=5001)


# --------
# ASK ALFREDO
    # why the spaces in parantheticals?
        # visual clarity 
        # easier to edit
