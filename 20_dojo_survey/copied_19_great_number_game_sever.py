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
            # I get three notification across three devices
from flask import Flask, render_template, redirect, session, request

# HEY!  ERROR: Terminal displayed a no flask error
        # This is because I was not in pipenv shell
app = Flask(__name__)

app.secret_key = "marcusaureliusthebestrevengeisnotobelikethat"

# Why is below code above the "back-route?" => "/"
                    # what is term for the red word?
# [keyword import] [term to generate random number]
import random   # CD import the random module
# What's happening with code above?
# random is a module, and a model is like a library but smaller


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
        # CODE ABOVE--why are session and randint both pink?  red herring, not related 
        # are they different types of the same term?  What's the term?
        # In Q&A 19 18:43 "session box" metaphor
                # can I RbrDk someone through it?

        # CODE BELOW 19 30:33 creating another session variable -- 19 31:15 this will change
        session["message"] = "If you get it wrong, you owe me $1"
# HEY!  ABOVE is where I stopped!  19 30:00  <----remember to do this, leave first one in as a reminder
        # ALSO, KW video helped me realize that [session]/[terminal]/{both?} 
        # is temporary.  Earlier, this made me chase ghost problems
            # Clarify what is going on in comments two above.  Which is it?     

    # 19 40:32.  Making a COUNTER!
    # CODE BELOW SUGGESTED BY NICK. Not in KW video.  Toggle doesn't seem to affect browser  
    if "count" not in session:  #this creates a starting point, 
                                # to prevent errors when counting
                                # Need some sort of if statement
        session["count"] = 0 # TRK=> index.html line 30

                        # PYTHON: booleans must be captialized
        # session["loser"] = True #changed boolean value at 19 49:57
                    # 19 49:01 not &&  --that's JavaScript
    # RbrDk BELOW 4 CODE 
    if session["count"] == 5:
        loser = True
    else:
        loser = False


    # 19 32:45 TOGGLE OFF
    # return render_template('index.html')
    # return render_template('index.html', message = session["message"])
    # 19 42:28  TOGGLE AGAIN
    return render_template('index.html', message = session["message"], count = session["count"], loser = loser) 
    # render_template is a method
    # there are 4 arugment
    # there are index.html is the file, next three arugments are the data being sent to HTML through jinja
    # ABOVE CODE Is loser hooked up to jinja TRK=> index.html, lines 50 -64
# 19 32:45 SET UP FOR ERROR.  Will need to change things

# CATCHing POST from form on line 41 index.html
@app.route('/process_guess', methods=["POST"])
def processing():   # Is there a NMCV for process_guess and processing--should they be different?
    # what do we write in print to make user_guess TRK=> index.html line 56     
    # What is the term for request in request.form?
    # print("======================================Hey!") #Code Below Not running.  What was the problem?  Did I not save?
    print(request.form["user_guess"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip

    # CODE BELOW 41:44 adding count to our session.  TRK=> server.py lines 68 and 84
    session ["count"] += 1 

    # CODE 4 BELOW: 19 29:26 Used to redirect an empty string
             # 19 23:09 If you submit an empty guess, we will get an error
                    # we get an error here becasue there is no integer
                    # equivalent to an empty string, IOW "" != 0
    if len((request.form["user_guess"])) < 1:
        print("C'mon!  Make a guess!")
        session["message"] = "Ah C'mon!  Just guess already!" # added 19 31:35
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
        print("================================You low balled it!")
        session["message"] = "Haha!  You low balled it!" # added 19 31:35
    elif user_guess > comp_guess:
        print("================================Nope!  Too high!")
        session["message"] = "Haha!  Nope! Too high!" # added 19 31:35
    else: # 19 25:07 HEY!  Print needs to be on lower line!
        session["message"] = "Awesome!  Nailed it!" # added 19 31:35 
        print("================================Nailed it!")
        # CODE ABOVE session and print are flipped at 19 32:22  Does that matter?--No.
        session["loser"] = False

    # HEY!  I spent almost 15 mintutes trying to get above 7 lines to print
            # in the terminal.  I tried deleting "print" 
            # back to the : on above line.  It worked!  No idea why.

    # HEY!  Never render on a post!
    # redirects to TRK-> server.py line 33
    return redirect("/")

    # 19 23:09 If you submit an empty guess, we will get an error

# CODE BELOW 19 36:45 to fix the error message I never got in the first place.
    # What is it supposed to do?
    # OKAY I didn't get that error message, but code below
            # does not clear session.  What happened? 
# Fixed ME: 1:17!  Need to manually reset localhost:5000/reset

@app.route("/reset")
def reset_session():
    session.clear()
    # CODE 4 BELOW  How is this different than 
    # render_template on TRK => index.html line 66 
    #       Is it more flexible?  Why?  
    # redirects to TRK=> server.py line 33
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

# 19 39:44, skipping CSS
# 19 39:50, let know users how many times they have guessed 
        # MAKE A COUNTER!

# I like working with python because of the diagnostics in terminal
# And because comments are easier/more fluid

#