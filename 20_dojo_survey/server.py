# I AM 20_dojo_survey server.py

# HEY! Post to GitHub Every Hour (at least)-->
# Last update at 5:20pm -->

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

        # Writing this out is helping me stay focused
        # it's liking revising a RbrDK that gets saved
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

    # TOGGLE
    # Below Code DOES Work
    return render_template('index.html') 
    # Code Below DOES NOT work.  It's in the wrong place, needs to be on server.py line 117 
    # return render_template('show.html', first_name = session["first_name"]) 
    
    # ALSO Will I need to incorporate Code Below into CODE 4 ABOVE
                    # No.  This rendering can be done on server.py line 117



# HEY!  9:38am The reason CITY, LANGUAGE and COMMENT wasn't working
        # was becuase you created a differnt @app.route for each question
        #only need one @app.route per form

# CATCHing POST from form TRK=> index.html line 37
@app.route('/answer_the_questions', methods=["POST"])
def and_i_will_read_them():   
    print("======================================FIRST NAME!")
    print(request.form["first_name"]) #diagnostic

# HEY!  "session of" means session[], "something of" something[]  KW
# HEY!  "session at" means session[], "something at" something[]  RM

# QUESTION:  Explain why session is definied in this route
            # and not on @app.route("/") at server.py line 46
# QUESTION:  What does Below Code do?
            # Does it assign request.form variable to session variable?        
    session["first_name_doesnotneedtomatch"] = request.form["first_name"]
    session["city"] = request.form["city"]  #TRK=>  flow from index.html, like cause and effect
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]


            #HEY!  Below comment was why it was not working
                # This is surprising  I expected Below Code work similarly to
            # 9:38am that's because you had an @app.route for each question
                # should be one @app.route per form

    print("======================================CITY!") #not printing either
    print(request.form["city"]) #diagnostic

    print("======================================LANGUAGE!") #not printing
    print(request.form["language"]) #diagnostic
 
    print("======================================COMMENT!") #not printing
    print(request.form["comment"]) #diagnostic
 
    # Never render on a post
    return redirect("/questions_answered")
    # I can redirect anywhere I want
# QUESTION:  Terminology:  Code 2 Above [REDIRECTS?] to server.py line 109
                # which, in turn, [REDIRECTS] to second template at server.py line 117

    # so if we never render on a post, how would I send the data
    # from index.html to show.html.  

# |||||
# QUESTION:  Below Code:  I don't need a method because this is not a post, right?
# TOGGLE
# @app.route('/questions_answered', methods=["POST"])
@app.route('/questions_answered')
def ill_read_them(): 
    # TOGGLE
    # return "I'll read them"
    print("===============================Question Answered")# diagnoistic
    
    # TOGGLE
    # # return redirect("/agrippina")   first_name parameter  session key["first_name"]
    return render_template('show.html', first_name = session["first_name"]) 
# QUESTION:  Code Above DOES work BUT works differently that I expected
                # why do I only need to define one session on CODE 2 ABOVE
                    # but I need to define 4 sessions [is "sessions" the appropriate term?]
                    # on TRK=> server.py lines 76 - 79
# HEY!  SESSION is DEFINED at TRK=> server.py lines 76 -79
    # # Above Code redirects to second template, show.html

    # TOGGLE
    # Below Code DOES NOT work
    # return render_template('show.html', first_name = session["first_name"], city = session["city"]) 
    # return render_template('show.html', first_name = session["first_name"], comment = session["comment"]) 
    
    
    # FIXED:  Recopied and edited nero code from 73_server.py
                # I don't know what I did differntlly
    # QUESTION Above Code:  my terminal doesn't like either one.  Why not?
        #  Getting two different Error message
        #  How do I read errors in the terminal?

# #     # TOGGLE
#     return redirect("/")
    # return render_template('index.html') 
    # return render_template('show.html') 

# ||||| end # @app.route('/questions_answered')


@app.route('/nero')
def last_words_of_nero():
    print('======================================Too late!')
    return 'Too late!'

@app.route('/agrippina')
def last_words_of_agrippina():
    print("======================================Smite Me Here!")
    return 'Smite me here, where the monster was nurtured!'


# keeping Code Below.  I think I'll need it for the home link
# to reset on the show.html
@app.route("/reset") # TRK => show.py line 44
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