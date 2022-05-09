# from curses import KEY_COMMAND
# from multiprocessing.shared_memory import ShareableList
# from pyexpat.errors import codes

# from setuptools import Command

# HEY!!!!!!!
        # What's up with these codes above?
        # They keep showing up and I don't know why?

from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# ////NEED CODE BLOCK BELOW TO HOOK UP ORIGINAL PAGE
# from flask import Flask # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'  # Return the string 'Hello World!' as a response


# CODE SNIPPET BELOW DIDN'T WORK.  WHY NOT?
# CODE SNIPPET BELOW IS FROM DEMOS_10
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="marcus", times=6)	# notice the 2 new named arguments!

# @app.route('/play')
# def level_one():
#     return render_template("index.html", num=3, color="blue")

# DOESN'T WORK???
@app.route('/play')
def level_one():
    return render_template("index.html", times=6, phrase="marcus")	# CD notice the 2 new named arguments!

# [it did work with] WORKS WITH HTML 2
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="marcus", times=6)	# CD notice the 2 new named arguments!

# ---------------THIS IS WHERE I STOPPED------------

# TERMINAL:  GO BACK AND CHECK TO SEE HOW DEMO_10 HOOKS server.py to index.html
                    # also localhost:5000/ isn't hooked up either
# ---------------THIS IS WHERE I STOPPED------------


#  still WORKS WITH HTML 2 b
# @app.route('/play')
# def level_one():
#     return render_template("index.html", times=6, phrase="marcus")	# CD notice the 2 new named arguments!

#  still WORKS WITH [HTML 2] c AND [HTML 3]
# @app.route('/play')
# def level_one():
#     return render_template("index.html", times=6, phrase="marcus")	# CD notice the 2 new named arguments!



@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/nero')
def nero():
    return 'What an artist dies in me!'

@app.route('/nero2')
def nero_b():
    return 'Too late!'

@app.route('/nero3')
def nero_aggripina():
    return 'Have I neither friend nor foe?'

@app.route('/say/<string:word>')
def hi_word(word):
    return f'Hi, {word.capitalize()}!'  

@app.route('/repeat/<int:num>/<string:word2>')      # Is it a good idea to keep 3 and 4 with separate variables?
def repeat_another_word(num, word2):
    return f'{word2 * num}'
    
if __name__=="__main__":   # CD Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # CD Run the app in debug mode.

# //////////////////
# COUNTER EXAMPLE WORD TO YO MAMA
# //////////////////

# from flask import Flask, render_template
# app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template("index.html", phrase="word to yo mama", times=8)	# notice the 2 new named arguments!


# if __name__=="__main__":
#     app.run(debug=True)

# TERMINAL CODES

# type

# pipenv shell 
# pipenv install flask
# exit
# python server.py

# key command

# cnt C










