# I AM 19_great_number_game server.py

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

#
# app 
# Flask different than flask and Flask on 12 .  
# what is the name --is this similar to __init__?  
# Are there terms for these? 
app = Flask(__name__)

# Below Code: I know we need this.  What happends if we leave it out?
app.secret_key = "machiavellihewhodesiresorattemptstoreforemthegovernmentofastateandwishestohaveitacceptedmustatleastretainthesemblenceofoldforms"

@app.route("/")
def index():

    return render_template('index.html') 


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