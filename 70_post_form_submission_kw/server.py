#  I AM 70_POST_FORM_SUBMISSION_KW SERVER.PY


# TA Question.  
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
        

# KW creates an instance utilizing the Flask framework and store it as 'app'
app = Flask(__name__)
# CD our index route will handle rendering our form

#KW this is the decorator or annotation for the following code chunk (the following method)  ME ===> define method?  which lines count as 'method'?
@app.route('/')   # is this line called 'the base route'?
def index():
    # KW Every route method should return something, in  this case we are rendering the given template
                # ME ====> (does 'pass' count?)
    print(request.form) # added 36:00 ish
    return render_template("index.html")

# AT FIRST ON THE LP, IT WAS UNCLEAR HOW THE CODE SNIPPET (OR APPROXMIATE) BELOW WORKED
# 22:14 handling processing of the form
# BELOW KWV 22:40  are users designed to post catch data?.  NCV Methods with an 's'
@app.route('/users', methods=["POST"]) # ====>WHY does it say "Method not found" in browser
def process_user():
    print("Cato the Elder")
    print(request.form)   #prints immutableMultiDict
    print(request.form["username"])
    print(request.form["email"])
    print("Yo!  This is the processing route")
    print("Cato the Younger")
    # print(f"{username} was here! 1")  --> this breaks the code
    username = request.form["username"] # what is this doing?
    print("Don't promise twice what you can do at once.")
    print(f"{username} was here! 2")

    # KW print form info
    # KWV 24:45 never render on a post route --on LP?  Where?

                # KWV 25:50 redirecting to base route, line 25--then 'returns' at line 29
    return redirect("/")
                # KWV 26:20 render_template renders an html
                #           redirect renders a url
    # return redirect("/", username=username) #37:18 noticed this line at 
@app.route('/nero')
def last_words_of_nero():
    return 'Too late!'

@app.route('/agrippina')
def last_words_of_agrippina():
    return 'Smite me here, where the monster was nurtured!'

# KW the following two lines are what allow the server to run
# KW these lins must ALWAYS be the last thing in your server files(s)
        #  BEGS THE QUESTION, is it possible to have more than one server file?
if __name__ == "__main__":
    app.run(debug=True)






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


# each mini-lecture, two types of text.  BEFORE and AFTER.  Let us choose (but not worry about breaking)