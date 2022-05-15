#  I AM 70_POST_FORM_SUBMISSION_KW SERVER.PY

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
                        #eventually imported, what does that mean
        

# KW creates an instance utilizing the Flask framework and store it as 'app'
app = Flask(__name__)
# CD our index route will handle rendering our form

#KW this is the decorator or annotation for the following code chunk (the following method)  ME ===> define method?  which lines count as 'method'?
@app.route('/')
def index():
    # KW Every route method should return something, in  this case we are rendering the given template
                # ME ====> (does 'pass' count?)
    return render_template("index.html")


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

