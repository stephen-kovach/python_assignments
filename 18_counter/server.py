# I AM 18_counter server.py

# Start at 5-15 5:35pm End x:xxpm

from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe--from mordor mwahahaha' # set a secret key for security purposes
            # 72 2:21 above is like an encryption 

# /////////////////////////////////////////////////
# Form Route
# /////////////////////////////////////////////////

@app.route('/')  
def index():

    if "count" in session:
        session["count"] +=1 
    else:
        session["count"] = 1

    return render_template("z04_index.html", count = session["count"]) 
 
@app.route('/add2')  
def add_2():
    print("went through '/add2'")
    if "count" in session:
        session["count"] +=1 # this will increment by 1 (total after line 28 is 2)
        # I still don't know what session means
    return redirect("/") 


# /////////////////////////////////////////////////
# Show Form Info Route
# /////////////////////////////////////////////////



# /////////////////////////////////////////////////
# Reset Session to Empty
# /////////////////////////////////////////////////


@app.route("/destroy_session")
def destroy_session():
    print("went through '/destroy_session'")
    session.clear()
    return redirect("/") #==> to line 14 server.py?
    # SO    1.  username stays unless
    #       2.  unless "Reset Session" is clicked.
    #           2a TRK: <a> tag on line 25, 73-b_session_counter show.html
            # 73 3:41 this is like logging someone out

#  Me: Next two routes are mine
# /////////////////////////////////////////////////
# Nero and Agrippina
# /////////////////////////////////////////////////

@app.route('/nero')
def last_words_of_nero():
    print("Too late!")
    return render_template("z05_index.html")

@app.route('/agrippina')
def last_words_of_agrippina():
    return 'Smite me here, where the monster was nurtured!'


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
#     print("went through '/resetsesh'")
#     session.clear()
#     return redirect("/") #==> to line 14 server.py?

# /////////////////////////////////////////////////
# What is the below code?
# /////////////////////////////////////////////////




if __name__ == "__main__":
    app.run(debug=True)

# It's weird there is a solution for this one