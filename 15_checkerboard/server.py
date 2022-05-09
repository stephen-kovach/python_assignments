
# I AM 15_CHECKERBOARD/SERVER.PY



from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def showtime():
    return 'Amor Fati!'

# I'M EXPECTING A LINE 28 TO ACT LIKE LINE 14
@app.route('/<int:x>/<int:y>')
def display_grid_variable(x, y):
    return f"x is {x} and y is {y}!"


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/play')
def level_one():
    return render_template("index.html", times=4, phrase="nero")	# CD notice the 2 new named arguments!

# I'M EXPECTING A LINE 27 TO ACT LIKE LINE 14,
# @app.route('play/<int:x>')
# def level_two(x):
#     return render_template("index.html", times=4, phrase="nero")	# CD notice the 2 new named arguments!
# -------ALSO:  WHY does changing above code block keep breaking my terminal

@app.route('/nero')
def nero():
    return 'What an artist dies in me!'

@app.route('/nero2')
def nero_b():
    return 'Too late!'

@app.route('/say/<string:word>')
def hi_word(word):
    return f'Hi, {word.capitalize()}!'  

@app.route('/repeat/<int:num>/<string:word2>')      # Is it a good idea to keep 3 and 4 with separate variables?
def repeat_another_word(num, word2):
    return f'{word2 * num}'

if __name__=="__main__":
    app.run(debug=True)



# ///////////////////////// old code from demos_10 and 14_playground

# @app.route('/')
# def index():

#     # WATCH HOW CODE BELOW CHANGES THE HTML

#     # return render_template("index.html", phrase="hello", times=6)	# CD notice the 2 new named arguments!
    
#     # return render_template("index.html", phrase="nero", times=3)	
    
#     return render_template("index.html", phrase="marcus", times=10)	

# DOESN'T WORK
# @app.route('/play')
# def level_one():
#     return render_template("index.html", num=3, color="blue")

# WORKS WITH HTML 2
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="marcus", times=6)	# CD notice the 2 new named arguments!

# WORKS WITH HTML 2
# @app.route('/')
# def index():
#     return render_template("index.html", phrase="marcus", times=6)	# CD notice the 2 new named arguments!

#  still WORKS WITH HTML 2 b
# @app.route('/play')
# def level_one():
#     return render_template("index.html", times=6, phrase="marcus")	# CD notice the 2 new named arguments!

#  still WORKS WITH [HTML 2] c AND [HTML 3]
# @app.route('/play')
# def level_one():
#     return render_template("index.html", times=6, phrase="marcus")	# CD notice the 2 new named arguments!



# CODE BELOW WORKS
# @app.route('/dojo')
# def dojo():
#     return 'Dojo!'

# @app.route('/nero')
# def nero():
#     return 'What an artist dies in me!'

# @app.route('/nero2')
# def nero_b():
#     return 'Too late!'

# @app.route('/say/<string:word>')
# def hi_word(word):
#     return f'Hi, {word.capitalize()}!'  

# @app.route('/repeat/<int:num>/<string:word2>')      # Is it a good idea to keep 3 and 4 with separate variables?
# def repeat_another_word(num, word2):
#     return f'{word2 * num}'
    

# ///////////////DON'T FORGET BELOW CODE

# if __name__=="__main__":
#     app.run(debug=True)

# //////////
# <!-- START BACKWARDS?  Do that for 14_PLAYGROUND -->