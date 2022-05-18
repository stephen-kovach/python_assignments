# I AM 20_dojo_survey server.py

# HEY! Post to GitHub Every Hour -->
# Last update at 10:36pm -->

# JSTOR====FLower and Hayes, Cognitive Process Model 1981

# The diachotomy of control.
    # Like restaurant work--you can only move so fast
        # the key is getting organized

# I can't control how fast I learn
# All I can control is the time I put in
    # Napoleon:  Space I can recover.  Time, never
    # Trade Space for Time

# Keep designing and evaluating mnmeonic strategies

# Below Code:  not sure what this is telling me
# from flask --try to define these terms later
# import Flask
# render_template  --got it
# redirect -got it
# session -got it
# request--what is it?  I don't think I need it
# why are we writing flask twice?
from flask import Flask, render_template, redirect, session, request


# Below Code:  not sure what this is telling me
# app 
# Flask different than flask and Flask on 12 .  
# what is the __name__ --is this similar to __init__?  
# Are there terms for these? 
app = Flask(__name__)

# Below Code: I know we need this.  What happends if we leave it out?
app.secret_key = "spaceicanrecovertimenever"
@app.route("/")
def index():

    return render_template('index.html') 


# STOP HEY!  -I was about to Copy Below Code.  One route per form

# CATCHing POST from form index.html
@app.route('/process_guess', methods=["POST"])
def processing():   
    # print("======================================Hey!") #Code Below Not running.  What was the problem?  Did I not save?
    print(request.form["user_guess"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip


    # Never render on a post
    return redirect("/")

# keeping this in.  I think I'll need it for the home link
# to reset on the show.html
@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)