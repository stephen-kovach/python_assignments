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

    print("========================Beginning") # Me 4:19 prints in terminal
    # ME 5:55pm where is below code hooked up?  line 18-47-72, 18-a_counter index.html
    if 'user_a' in session:  # Me 6:41pm changed 19 and 22 to user_a--still works
        print('user_b exists!')
    else:
        print("key 'user_c' does NOT exist")
        # Me 4:26pm what input would trigger the above else statement to print?
    print("========================End") # Me 5:57pm track when prints in terminal 


    if "count" in session:
        session["count"] +=1  # this will increment by 1
    else:
        session["count"] = 0

    return render_template("index.html", count = session["count"]) 
    # is ABOVE code hooked up to line 17, 18-a_counter index.html?

# BELOW KWV 22:40  are users designed to post catch data?.  NCV Methods with an 's'
@app.route('/users', methods=["post"]) 
            # ====>WHY does it say "Method not found" in browser
            # ====> Me 6:00pm is it because it's what prints in terminal?
def process_user():
    print("Cato the Elder")
    print(request.form)   #prints immutableMultiDict
    print(request.form["username"])
    # print(request.form["email"])  #---this doesn't work.  why not?
    print("Yo!  This is the processing route")
    print("Cato the Younger")
    # print(f"{username} was here! 1")  --> this breaks the code
    username = request.form["username"] # not in terminal.  what is this doing?
    # email = request.form["email"] # Nope 12:27 So does this add [term] to the [term --terminal?] 
    print("Don't promise twice what you can do at once.")
    print(f"{username} was here! 2")
    # print(f"I swear {email} is somewhere around here...")

    # KWV 24:45 never render on a post route --on LP?  Where?

    # 72 6:00 Added BELOW,  External Processing: I want to change the label  -what does that mean?
    session["user"] = request.form["username"]
    # What does above code do?
    
    # 72 8:42 new edit for 5ish below
    return redirect("/show")
    

# /////////////////////////////////////////////////
# Show Form Info Route
# /////////////////////////////////////////////////

# 72 9:15 added below -Don't forget, delibrately making errors
@app.route("/show")
def show_user_info():
    print("?+?+?+?+?+?+?+?+?+?+?+?+?+?+?+?+?+?+?+?" + session["user"]) #10:00 forgot to put user in ""
    # return render_template("show.html") #commented out at 72 15:17
# 72 11:50 Session is empty by default.  12:15  Session is a big empty box,  it only stores something if we tell it to
# 72 15:48 substitued 2 above for 1 below:
    return render_template("show.html", user_name = session["user"]) 


# /////////////////////////////////////////////////
# Reset Session to Empty
# /////////////////////////////////////////////////

# 73 2:12 added below
@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")
    # SO    1.  username stays unless
    #       2.  unless "Reset Session" is clicked.
    #           2a TRK: <a> tag on line 25, 73-b_session_counter show.html
            # 73 3:41 this is like logging someone out

# COPIED =====> below code pasted from:  flask-flask-fundamentals-counter
# session.clear()		# clears all keys
# session.pop('key_name')		# clears a specific key
# COPIED =====> above code pasted from:  flask-flask-fundamentals-counter
#
#  Me: Next two routes are mine
# /////////////////////////////////////////////////
# Nero and Agrippina
# /////////////////////////////////////////////////

@app.route('/nero')
def last_words_of_nero():
    return 'Too late!'

@app.route('/agrippina')
def last_words_of_agrippina():
    return 'Smite me here, where the monster was nurtured!'

# /////////////////////////////////////////////////
# What is the below code?
# /////////////////////////////////////////////////

if __name__ == "__main__":
    app.run(debug=True)

