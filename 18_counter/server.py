# I AM 18_counter server.py

# What is the number above and to the side.
# It seems to rise and lower as I write

# Start at 5-15 5:35pm End x:xxpm

# Not using 'request' from below, what would it be doing?
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe--from mordor mwahahaha' # set a secret key for security purposes
            # 72 2:21 above is like an encryption 

# /////////////////////////////////////////////////
# Form Route
# /////////////////////////////////////////////////

@app.route('/')  
def index():
    print("==================================beginning index")
    # I need a diagram of how this is counting, and what session is
    if "count" in session:
        session["count"] +=1 
    else:
        session["count"] = 1
    print("==================================end index")

                                # is count and session created below
    return render_template("z04_index.html", count = session["count"]) 


# This works
@app.route('/add2')  
def add_2():
    print("==================================beginning add2'")
    # why a conditional here?
    if "count" in session:
        session["count"] +=1 # this will increment by 1 (total after line 20 is 2)
        # I still don't know what session means
    print("==================================end add2'")
    return redirect("/") 

# This works redirects, but doesn't add
@app.route('/seneca-add5')  
def add_5():
    print("==================================beginning Seneca Add 5'")
    # why a conditional here?
    if "count" in session:
        session["count"] +=4 # this will increment by 4 (total after line 20 is 5)
        # I still don't know what session means
    print("==================================end Senecs Add 5'")

# TOGGLE BELOW
    return redirect("/") 
    # return render_template("z07_index.html", count = session["count"]) 


# This works
@app.route('/subtract10')  
def subtact_10():
    print("==================================beginning subtract10'")
    if "count" in session:
        session["count"] -=11 #compensating for line 23
                        #is there a way to avoid this?
    print("==================================end subtract10'")
    return redirect("/") 


# This adds 1 count on index page
@app.route('/multiply5')  
def multiply_5():
    print("==================================beginning multiply5'")
    if "count" in session:
        session["count"]*5 #compensating for line 23
                        #is there a way to avoid this?
    print("==================================end multiply5'")
    return redirect("/") 

# This adds 1 count on index page
@app.route('/divide2')  
def divide_2():
    print("==================================beginning divide2'")
    if "count" in session:
        session["count"] / 2 #compensating for line 23
                        #is there a way to avoid this?
    print("==================================end divide2'")
    return redirect("/") 
# /////////////////////////////////////////////////
# Show Form Info Route
# /////////////////////////////////////////////////



# /////////////////////////////////////////////////
# Reset Session to Empty
# /////////////////////////////////////////////////


@app.route("/destroy_session")
def destroy_session():
    print("==================================beginning_session")
    session.clear()
    print("==================================end destory_session")
    return redirect("/") #==> to line 14 server.py?
    # SO    1.  username stays unless
    #       2.  unless "Reset Session" is clicked.
    #           2a TRK: <a> tag on line 25, 73-b_session_counter show.html
            # 73 3:41 this is like logging someone out

@app.route("/destroy_session_seneca")
def destroy_session_seneca():
    print("==================================/seneca_destroys")
    session.clear()
    print("==================================/seneca_destroys")
    return render_template("z07_seneca.html")

#  Me: Next two routes are mine
# /////////////////////////////////////////////////
# Nero and Agrippina
# /////////////////////////////////////////////////

# What is below line called?
@app.route('/nero')
# Why are we defining a function below?
# Would we ever use function like one below
# for anything else besides directing the route?
def nero_just_being_a_jerk():
    print("==================================Too late!")
    return render_template("z05_nero.html")

@app.route('/agrippina')
def last_words_of_agrippina():
    print("==================================Smite me here!")
    return 'Smite me here, where the monster was nurtured!'
    # This won't print ABOVE ends the statement
    print("==================================Smite me here!")

@app.route('/seneca')
def seneca_the_stoic():
    print("==================================All cruelty springs from weakness.")
    return render_template("z06_seneca.html")

@app.route('/seneca-adds')
def seneca_the_mathematician():
    # This adds to the count on index page, but does not display in either
    # seneca page
    print("==================================beginning Seneca adds 1")
    if "count" in session:
        session["count"] +=1 
    else:
        session["count"] = 1
    print("==================================end Seneca adds 1")
    return render_template("z07_seneca.html")

@app.route('/galba')
def galba():
    print("==================================Thanks, Otho")
    return 'Thanks, Otho...'
    # This won't print ABOVE ends the statement
# /////////////////////////////////////////////////
# LP Solutions
# /////////////////////////////////////////////////

# @app.route('/')
# def index():
#     if "count" not in session:
#         session["count"] = 0
#     else:
#         session["count"] += 1

#     return render_template("z04_index.html") 

# @app.route('/resetsesh')
# def reset_route():
#     print("beginning '/resetsesh'")
#     session.clear()
#     return redirect("/") #==> to line 14 server.py?



# /////////////////////////////////////////////////
# What is the below code?
# /////////////////////////////////////////////////

if __name__ == "__main__":
    app.run(debug=True)



# LP:  It's weird there is a solution for "Counter" assignment, incnstnt