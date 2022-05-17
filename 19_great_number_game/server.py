# I AM 19_great_number_game server.py

# I'm using comments as a rubber duck
# Helps me define the patterns
# I'm building mnemoic devives
# This is the Linda Flowers Cognitize Process Model
# These comments are my memory maps

# This Commenting System seems like it is more work
        # But it's helping me stay task orientated 
        # By reminding me what I am doing as I skip around
        # It's like training wheels.
        # Hopefully I'll be doing it less and less AND maybe not at all

# ALSO, I did not text on the job at work.  But on my mac I get
# every irrelevant update etc.  I need to turn that off.  How?

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
        # What is the term for [label]?
        # 2. the [label?] comp_guess  <--1. Assigning a random number to 
        session["comp_guess"] = random.randint(1, 100)
        # CODE ABOVE--why are session and randint both pink?
        # are they different types of the same term?  What's the term?
        # In Q&A 19 18:43 "session box" metaphor
                # can I RbrDk someone through it?

        # CODE BELOW 19 30:33 creating another session variable 
        session["message"] = "You better not get it wrong!  Mwahahahaa!"
# HEY!  ABOVE is where I stopped!  19 30:00  <----remember to do this, leave first one in as a reminder
        # ALSO, KW video helped me realize that [session]/[terminal]/{both?} 
        # is temporary.  Earlier, this made me chase ghost problems
            # Clarify what is going on in comments two above.  Which is it?     
    return render_template('index.html')



# CATCHing POST from form on line 41 index.html
@app.route('/process_guess', methods=["POST"])
def processing():   # Is there a NMCV for process_guess and processing--should they be different?
    # what do we write in print to make user_guess line 45 index.html
    # What is the term for request in request.form?
    # print("======================================Hey!") #Code Below Not running.  What was the problem?  Did I not save?
    print(request.form["user_guess"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip

    # CODE 4 BELOW: 19 29:26 Used to redirect an empty string
             # 19 23:09 If you submit an empty guess, we will get an error
                    # we get an error here becasue there is no integer
                    # equivalent to an empty string, IOW "" != 0
    if len((request.form["user_guess"])) < 1:
        print("C'mon!  Make a guess!")
        return redirect("/")
            # ABOVE I'm guessing we can redirect to any page we want, right?

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

    else: # 19 25:07 HEY!  Print needs to be on lower line!
        print("================================Nailed it!") 
    
    # HEY!  I spent almost 15 mintutes trying to get above 7 lines to print
            # in the terminal.  I tried deleting "print" 
            # back to the : on above line.  It worked!  No idea why.

    # HEY!  Never render on a post!
    # redirects to 19_great_number_game server.py line 24 
    return redirect("/")

    # 19 23:09 If you submit an empty guess, we will get an error


if __name__=="__main__":
    app.run(debug=True)


#