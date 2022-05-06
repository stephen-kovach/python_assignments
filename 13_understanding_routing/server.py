from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

# 1
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# 2
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# IF WE'RE DEFINING A NEW FUNCTION ON LINE 10, WHERE/HOW IS IT BEING CALLED?  OR IS THAT AN ABSTRACTION?

# 3
# @app.route('/say/<word>')
# def hi_word(word):
#     return f'Hi, {word.capitalize()}!'  

# NINJA BONUS:  ENSURE THE NAMES IN THE THIRD TASK ARE STRINGS

@app.route('/say/<string:word>')
def hi_word(word):
    return f'Hi, {word.capitalize()}!'  


# @app.route('/say/<word>')
# def hi_word(word):
#     return 'Hi, ' + word + '!'  # Does this need to be an "f" statement?

# 4
# There are two ways to do the 4th question


@app.route('/repeat/<int:num>/<string:word2>')      # Is it a good idea to keep 3 and 4 with separate variables?
def repeat_another_word(num, word2):
    return f'{word2 * num}'
    


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

