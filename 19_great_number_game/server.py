# I AM 19_great_number_game server.py

# I'm using comments as a rubber duck
# Helps me define the patterns
# I'm building mnemoic devives
# This is the Linda Flowers Cognitize Process Model
# These comments are my memory maps

# ALSO, I did not text on the job at work.  Now I get
# every update etc.  I need to turn that off

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "marcusaureliusthebestrevengeisnotobelikethat"

# Why is below code above the "back-route?" => "/"
                    # what is term for the red word?
# [keyword import] [term to generate random number]
import random   # CD import the random module
# What's happening with code above?


@app.route("/")
def index():
    # 19 14:35 Me: walk me though why "not in" sesssion instead of "in"
    # I think I get it, maybe I should RbrDk through with it TA
    # 19 18:35 We are only generating random number if nothing in session box
            # RbrDk
            # Me:  besides the browser, is there another way 
            # to display session information? 
    if "comp_guess" not in session:
        # [what term is session?]
        session["comp_guess"] = random.randint(1, 100)
        # --why are session and randint both pink?
        # are they different types of the same term?
        # In Q&A 19 18:43 "session box" metaphor
                # can I RbrDk someone through it?

    return render_template('index.html')

# Catches post from form on line 39 index.html
@app.route('/process_guess', methods=["POST"])
def processing():   # Is there a NCV for process_guess and processing--should they be different?
    # what do we write in print to make user_guess line 44 index.html
    # What is the term for request in request.form?
    # print("======================================Hey!") #Code Below Not running.  What was the problem?  Did I not save?
    print(request.form["user_guess"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip

#===> 23:25 TECHNIQUE FOR SHORTENING CODE
    # BELOW COMMENT WRITTEN TO REMIND ME HOW TO ASSIGN VARIABLES.  This is how I will remember
    #2.  to a shorter one  1.  Assign longer variable <-
    user_guess = int(request.form["user_guess"])
            # above code int [term -- "translates"?] user_guess into an integer
            # Two Above: Part 2 no int  Part 1 int because  to a shorter one  1.  Assign longer variable <-
    print(user_guess)
    # Do the same for session["comp_guess"]
    comp_guess = session["comp_guess"]
    print(comp_guess)
    # 19 22:50 Comparing our Computer Number with User Guess
    if user_guess < comp_guess:
        print("================================You low balled it.")
    elif user_guess > comp_guess:
        print("================================Nope!  Too high!")  
    # 19 23:09 If you submit an empty guess, we will get an error
    else: # 19 25:07 HEY!  Print needs to be on lower line!
        print("================================Nailed it!") 
    # HEY!  Never render on a post!
    
    # redirects to line 24 19_great_number_game server.py
    return redirect("/")




if __name__=="__main__":
    app.run(debug=True)


