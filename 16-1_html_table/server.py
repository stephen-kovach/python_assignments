
# 16-1_html_table/server.py


# importing flask from templates folder, why render_template here again?
# what's the difference betweem lowercase and uppercase flask/Flask?
from flask import Flask, render_template

app = Flask(__name__)

# I like starting out with two "@decorators?" that "call?" the "routing function?"
# Is staring out with two a common practice?
@app.route('/')
@app.route('/tables')
def render_table():
    # defining a variable called "head_honcho" 
    # assigning it the value of a [list?] 
    # that contains a "dictionary" as its datatype [review: define object]
    head_honcho = [  

        # This list contains three dictionaries, 
            # each dictionary [contains?] two key-pair values

        # curly braces means this is a dictionary
        # 'first_name' and 'Michael' is a/are a key-pair value
        # 'last_name' and 'Choi' is a/are a key-pair value
        {'first_name' : 'Michael', 'last_name' : "Choi"},
        {'first_name' : 'John', 'last_name' : "Supsupin"},
        {'first_name' : 'Mark', 'last_name' : "Guillen"},
        {'first_name' : 'Monty', 'last_name' : "Burns"},
        # ask about the colons and the commas, how do I talk about these?
    ]
                                    # what is the term for egos?  variable head honcho
    return render_template("index.html", egos = head_honcho)

# creating a decorator called an "app route"
@app.route('/nero2')
# NMCV for the function below?  What are the related NMCV?
def create_nero2():
    # below is returning the string [is this related to templates?]
    return 'Sorry Mom!'

# define
if __name__=="__main__":
    app.run(debug=True, port=5001)
