# I AM 73 session_counter_kw backup_server.py

# KW PYTHON APRIL 2022 Session 18:59 -->

    # I tried reading "Reditecting" and "Session" on the platform
    # Not clear at all
    # I'm betting the video would be better

# Start at 5-15 1:49pm End 5:09pm

# 71 I've seen all three instructors draw data flow diagrams
        # 71 is this on the LP?  Why not OR why hard to find?
        # 71 2:37 "wrap in bow"  the package is a great metaphor

#DO I NEED TO ASK THESE Question?  
# How do I get 39ish YO! to print in terminal 

# KW PYTHON APRIL 2022 INTRO TO FORMS AND POST DATA
# TIME: 1:23  KW DISPLAYS [pronouns -her?] COMMENTS ON VSCODE

#======>        # Do I have access to this on github?

# KW Flask -This pulls om the framework for our project ==> what is a framework?  NOT defined in search "framework" takes me to unrelated page
# KW render_template - this method allow us to hanle [sp? -handle?] actual files instead of just Http response, this is required to render HTML pages
# KW redirect - allows us to redirect to a URL that we have built out in our project
# KW session - a type of data storage that permeates throughout the program
    #session doesn't contain anything until you tell it to store that information!
# KW request - allows us to 'request' information like when we pull information from our form on the [can't see the word]

from flask import Flask, render_template, redirect, session, request
        # Can we diagram what's happening above?
        # KW VID 9:00 line 16 is gray now because: not called on them yet
                        #"eventually imported", what does that mean
        
# LP SESSION 0:52:  Use Session to Store variables and access them in any route
            # This is so unhelpful

# KW creates an instance utilizing the Flask framework and store it as 'app'
app = Flask(__name__)
# CD our index route will handle rendering our form
# 72 2:57 below added == HEY! ===>> 72 3:20 MAKE A DIFFENENT SECRET KEY PER ASSIGNMENT (even a key slap like: "sadfkjhasdkjlfh" is fine)
app.secret_key = 'keep it secret, keep it safe--from mordor mwahahaha' # set a secret key for security purposes
            # 72 2:21 above is like an encryption 

# 72 5:03 - 5:29 - ADDED "Form" and "Show Form" Below (watched it, that's 26 seconds to shave off)
# /////////////////////////////////////////////////
# Form Route
# /////////////////////////////////////////////////

# 73 16:32 When the base route is set
#KW this is the decorator or annotation for the following code chunk (the following method)  ME ===> define method?  which lines count as 'method'?
@app.route('/')   # [when?] is this line called 'the base route'?  Me 5:03 Yes!
def index():
    # KW Every route method should return something, in  this case we are rendering the given template
                # ME ====> (does 'pass' count?)
    print("========================Beginning") # Me 4:19 prints in terminal
# 73 5:35 substitutes COPIED code accounted for below
    if 'user' in session:
        print('user exists!')
    else:
        print("key 'user' does NOT exist")
        # Me 4:26 what input would trigger the above else statement to print?

    print("========================End") # Me 4:19 does not print in terminal 
    # print(request.form) # added [which video?]36:00 ish

    # 73 13:14 adds line below
    # session["Count"] = 0   #not sure what this counterexample is demonstrating
    # TOGGLE ABOVE AND BELOW
    # 73 13:14 comments out below 8 lines
    if "count" in session:
        # 73 8:19 KW note:  do something, count+1
        # 73 9:14 added below
        session["count"] +=1  # this will increment by 1
    else:
        session["count"] = 0
        # Me 4:31 could even a consistent "" or ' syntax could help?  overkill?
                # why not be on the same page?

# COPIED =====> below code pasted from:  flask-flask-fundamentals-counter
# if 'key_name' in session:
#     print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")
# COPIED =====> above code pasted from:  flask-flask-fundamentals-counter

    return render_template("index.html", count = session["count"])
    # 9:54 BELOW substitued for ABOVE  ===> TRK: line 83, 73_session_counter_kw index.html
    # return render_template("index.html")
    # 73 6:32 Me 4:16
    # "'Bobbothy' exists" does not print in terminal
            # Me 4:17 I will try to rebuild it 

# AT FIRST ON THE LP, IT WAS UNCLEAR HOW THE CODE SNIPPET (OR APPROXMIATE) BELOW WORKED
# 22:14 handling processing of the form
# BELOW KWV 22:40  are users designed to post catch data?.  NCV Methods with an 's'
@app.route('/users', methods=["POST"]) # ====>WHY does it say "Method not found" in browser
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

    # print("")
    # print("/////////////////////////////////")
    # print("")
    # print("Your videos have been super helpful!")
    # print("")
    # print("If it weren't for these videos, I'd be on AP")
    # print("")
    # print("lol")
    # print("")
    # print("A little feedback:")
    # print("")
    # print("on the video: Python April 2022 Form Dataflow")
    # print("")
    # print("at 11:30")
    # print("")
    # print("you said:")  
    # print("")
    # print("Flask is a toolbox.  A wrech is the only tool I can think of.")    
    # print("Corkscrew was the next thing that came to mind, but that is not a tool.")
    # print("")
    # print("--wrong--")
    # print("")
    # print("A corksrew is definitely a tool!")
    # print("")
    # print("(it's literaly a screw!)")
    # print("")
    # print("btw a corkscrew is really only one of the few tools I know how to use well")
    # print("")
    # print("Can't open a bottle without one")  
    # print("")
    # print("Not even with my teeth!")  
    # print("")  # why not in the terminal
    # print("Want to know a fun fact that's tangentially related to screws?")
    # print("")
    # print("Ask me!")
    # print("")
    # print("")


    # KW print form info
    # KWV 24:45 never render on a post route --on LP?  Where?

    # 72 6:00 Added BELOW,  External Processing: I want to change the label  -what does that mean?
    session["user"] = request.form["username"]
    
    
    # 72 8:42 new edit for 5ish below
    return redirect("/show")
    
    
    
                # KWV 25:50 redirecting to base route, line 25--then 'returns' at line 29
    # return redirect("/")
                # KWV 26:20 render_template renders an html
                #           redirect renders a url
    # return redirect("/", username=username) #37:18 noticed this line at 


# 72 5:03 - 5:29 - ADDED "Form" and "Show Form" Below (watched it, that's 26 seconds to shave off)
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


# 73 1:07 added below: Reset Session to Empty
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

# Me 2:55 What is the below code?
# /////////////////////////////////////////////////
# What is the below code?
# /////////////////////////////////////////////////

# KW the following two lines are what allow the server to run
# KW these lins must ALWAYS be the last thing in your server files(s)
        #  BEGS THE QUESTION, is it possible to have more than one server file?
if __name__ == "__main__":
    app.run(debug=True)




# ///////////////////////////////////////////

# 23:01  student asks tangental question about counter  
# 23:10 great pause recording!
# 27:07  Not case senstive, not a distraction

# 27:54 -29:13 
#       wrong code.  Not a problem in a classroom
#                       A teachable moment
#                       As a view it's inefficent and confusing
#                           AND MY BEST ALTERNATIVE 

    # IS IT FIXED WHAT DO I NEED TO DO?
    #       # My screen still says 'Method Not Allowed'
                # what got fixed?
                    # 29:29
                    # my termnial still does not say 
                        #    "YO!  This is the processing route"
    
    # TIME MAY 14 10:07 I'm going to keep pushing on
        # resuming at 30:23

        # 10:18!  Wait now my terminal works!  Why?  
        # Taking a screenshot and adding it to File/Pics
                # not effeicient 10:22
                    # WORKFLOW, HOW DO I REDIRECT AUTO FILES ON DESKTOP
        
        # How do I print Yo! etc in my terminal

                # does it autmoatically come after enter email?

    # TIME 10:29  I figured out the error!  Time to move on!
        # in terminal:
        # Cato the Elder 
        #  immutatable dictionary ([(username) yo (email) yo@mama.com  
        # (username) yo 
        # (email) yo@mama.com  
        # YO!  This is the processing route!
        # Cato the Younger

# 31:30 Good Circling Back  Never render on post route

        # 31:54 on scale at 1 - 10  I'm at an 8!

# 32:02 -34:21  not a tangent, but something I already figured out
# is that saquarra?  webfun cohort
    # didn't quite understand the question, not reviewing it


# Isn't there somewhere on the introduction part of the platform
# where they make suggestions on how to manage time lol?

# 35:41  "So when I do this"  do what?


# I'm considering the tangents a tax on my time
# the taxes need to be lowered


# how to read W3Schools  Try it yourself
#    how does it work?

# LP  Example Code Builds.  Don't worry about breaking it
    #    I'm noticing students reluctant to do it

# If there were shorter videos, students could watch them before the lectures


# each mini-lecture, two types of text.  BEFORE and AFTER.  
# Let us choose (but not worry about breaking)

# //////

# Point of pride
# instructor to making videos is as
# PST Line making dishes on the menu

# 71 5:09 - 6:00 Jason Question  No
# 71 6:00 - 6:28 Chat Question No
# 71 6:33 - 7:13  Asking if Diagrams here are clear
                    # on the LP this kind of feedback could be built in
# 71 7:40 oh I forgot, uneccarily recursive, on have been 
# structure on LP

# 71 8:35  - 8:50 Debug error, this wouldn't happen on a strcutured LP
# 71 9:50 NEVER RENDER ON A POST ROUTE
#               always redirect ing      Good Repetition

# 71 11:30  Flask is a toolbox  11:41 A corksrew is definitely a Tool!  It's literaly a screw!  Fun fact:  Achemdies Screw

# 71 12:45 -13:18 Jason Question OK,
                # ultimately distracted Kaysee from a more polished segue

# ////////////////////////////////////////////

# Ultimate room for improvment on the LP is 
        # Understanding the terrain  on-line, automated, instant-feedback
                # missed opportunities for user interactivity

                # AND ADAPT TEACHING METHODS OF THE TERRAIN
                    # IN ADDITION TO 
                    #       THE MANUALS AND VIDEOS
                    #          THAT ALREADY EXISTS
                    #           AND CAN CERTAINLY BE IMPROVED
# NAPOLEON MAPS AND THE CORP 



# I started creating the file folders > 70
# So I could easily have a way to post them to github
# I have a folder called demos with similar notes

# I'm still not comfortable creating github repositories
            # Ask for another demo 
            # take notes in VSCode
            # push it to github

# There should be a standardized way to divide the videos

        # consitency would encourage organization

# ALSO

# If I was able to watch an instructional video before a lecture
        # a.  I would have some of my questions answered already 
        # and b. I would bring better questions to the lecture

# Again.  a more dynamic, interactive and responsuve LP 
    # would empower us to learn

# Also on Zoom, how do I add an off picture and edit my name


# 72 0:23 do a good job of breaking down   -nope!
# This is more "technical, educational, more comprehensive"  --nope!  just bad writing
# more "application"  --this is the purpose of a leture
        # it must also be done on LP
        # no excuse not to

# 72 8:00 Took a Screen Shot of diagram
            # Is there something like this on the platform?
                # Why not?  OR  Why isn't it easy to find?
# 72 8:05   Chat a 1!  oh no!  oh good!  a 10!
            # could have shaved off 10 secs.  This adds up!

# 72 9:24 I'm typing this out myself, but hareder to do in chunks
        # come back to this

# 72 10:16  KW gets a key errror
        # I get a Template not found:
                # jinja2.exceptions.TemplateNotFound: show.html
        # above 2 answered at 72 10:50

# 72 13:10   ---"grab container up"
# Me 12:45
#             creates show.html very quickly
#             walks through what is probably a good habit
#             but it's almost an aside
#             I will probably use this technique

# Also Design a Short Cut Key Bank on platform (dynamlic)
    # much better than a link from some excelsheets

# SCREEN SHOT!
# 72 16:25
        # is there a disagram like this on the LP 
        # Why not OR why is it not easy to find?

# 73 0:09 How to clear our session
# 73 0:20 missed opportunity to have a clear LP
        # the reason KW doesn't use LP example
        # is because LP example isn't clear

# 73 0:40  Crtl shift R  What is that?
            # 73 0:45 ME 2:45 refreshes browser

# 73 1:42 Pulled Code from the platform, 
            # flask-flask-fundamentals-counter
            # couldn't see map on YouTube
            # stopped and checked 
            # flask-flask-fundamentals-session
            # could have shaved off time

# Me 3:05 -3:11 bathroom break
# I know this is silly lol, but I'm mangaing my time 
# by first tracking it
# hopefully I'll do less later

# 73 3:50 - 3:59
            # 1 - 10 Poll:  Great for lecture!
            # ineffcient for instruction
            # could have shaved off 0:09

# I quoted KW 'Elephant in Room' because it's an effecrive mnemonic device!
# 73 4:10  Elephant in the room:  Counting!
