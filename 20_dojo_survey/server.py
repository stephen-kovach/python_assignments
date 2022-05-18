# I AM 20_dojo_survey server.py

# HEY! Post to GitHub Every Hour -->
# Last update at 8:37am -->

# JSTOR====FLower and Hayes, Cognitive Process Model 1981

# The diachotomy of control.
    # Like restaurant work--you can only move so fast
        # the key is getting organized

# I can't control how fast I learn
# All I can control is the time I put in
    # Napoleon:  Space I can recover.  Time, never
    # Trade Space for Time
    # Don't Race Against Time
    # Use Time To Learn

# ALSO I can control my strategies
#
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


# HEY!  9:38am The reason CITY, LANGUAGE and COMMENT wasn't working
        # was becuase you created a differnt @app.route for each question
        #only need one @app.route per form

# CATCHing POST from form TRK=> index.html line 29
@app.route('/answer_the_questions', methods=["POST"])
def and_i_will_read_them():   
    print("======================================FIRST NAME!") #Code Below Not running.  What was the problem?  Did I not save?
    print(request.form["first_name"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip


# HEY!  Below comment was why it was not working
# This is surprising  I expected Below Code work similarly to
# TRK=> server.py line 54 ---9:38am that's because you had
                    # an @app.route for each question
                    # should be one @app.route per form
# CATCHing POST from form TRK=> index.html line 29
    print("======================================CITY!") #not printing either
    print(request.form["city"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip



# CATCHing POST from form TRK=> index.html line 29
    print("======================================LANGUAGE!") #not printing
    print(request.form["language"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip

 
    print("======================================COMMENT!") #not printing
    print(request.form["comment"]) #diagnostic
    # Saw KW do print ""======"" this weekend.  Very good tip


    # Never render on a post
    return redirect("/")




# keeping this in.  I think I'll need it for the home link
# to reset on the show.html
@app.route("/reset")
def reset_session():
    session.clear()
    return redirect("/")

# what's going on in the code below?
# if is just a conditional
#  __name__ same as above --what is that doing again?
# == is just an operator
# "__main__"
# app. same as @app. --what is that doing again?
# run
# (degug=True)  #True is just a boolean
if __name__=="__main__":
    app.run(debug=True)