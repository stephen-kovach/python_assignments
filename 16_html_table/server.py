
# I AM 16_HTML_TABLES/SERVER.PY



from flask import Flask, render_template
# app = Flask(__name__) COULD be in a different place
app = Flask(__name__)

@app.route('/')
def showtime():
    return 'Momento Mori!'

@app.route('/tables')
def render_table():
    # [term for below--it connects to line 23 where else?  also on HTML?] =[]
    # Also the bracket underneath: is it creating a list, a dictionary? an object?  all three?
    head_honcho = [  
       {'first_name' : 'Michael', 'last_name' : "Choi"},
       {'first_name' : 'John', 'last_name' : "Supsupin"},
       {'first_name' : 'Mark', 'last_name' : "Guillen"},
    ]
# TRACK IT:  egos on .html line 30, head_honcho on server.py line18 -where else?
    return render_template("index.html", egos = head_honcho)

@app.route('/nero')
def nero():
    return 'Too late!'

@app.route('/nero2')
def nero_b():
    return 'Sorry Mom!'
3
# @app.route('/<int:x>/<int:y>')
# def display_grid_variable(x, y):
#     return f"x is {x} and y is {y}!"

# what does app mean?
# @app.route('/tables')
# # am I 'declaring a function?'
# # [keyword? def] name_of_function():  dtf colon
# def render_tables():
#     pass
    # is 'student_info' declaring varible?  Are lines beneath an object, a dictionary, or both 
    # variable = []  <---is this a list or an object or both?
    # users = [
    #     # 'key'  [:] 'value', 'key' : value (no quotes, not a string), ALSO why a comma?
    #    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    #    {'first_name' : 'John', 'last_name' : 'Susupin' },
    #    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    # ]
    # # FOR THE ASSIGNEMENT SHOULD FIRST NAME AND LAST NAME BE COMBINED?  OR SHOULD I ADD A THIRD CATEGORY LIKE THIS:  --CONCATINATE?
    # # [keyword] function_name("filename.html"),
    # return render_template("index.html", random_numbers = [3, 1,5, 8, 10], students = users)



#/////////////////////////  ISSUE SOLVED //////////////////
# #    If I change index.html, it doesn't break.  Why not?  What is it refering to?
#     # ALSO:  I DON'T THINK THIS IS HOOKED UP TO I AM 16_HTML_TABLES/TEMPLATES/INDEX.HTML
#     # return render_template("banana.html", students = student_info)
# # BELOW TWO LINES ARE FROM 13_VID_MORE TEMPLATE RENDERING SERVER.PY
# # #    If I change index.html, it doesn't break.  Why not?  What is it refering to?
#     return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
# //////////////////////////////////////////

# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     owner_info = [
#        {'first_name' : 'Michael', 'last_name' : 'Choi'},
#        {'first_name' : 'John', 'last_name': 'Sususpin' },
#        {'first_name' : 'Mark', 'last_name': 'Guillen'}
#     ]
#     return render_template("index.html", big_wigs = owner_info)

# FUNCTION BELOW WORKS WITH 16_HTML_TABLES/TEMPLATES/INDEX.HTML
# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     student_info = [
#        {'name' : 'Michael', 'age' : 35},
#        {'name' : 'John', 'age' : 30 },
#        {'name' : 'Mark', 'age' : 25},
#        {'name' : 'KB', 'age' : 27}
#     ]
#     return render_template("index.html", random_numbers = [3,1,5], students = student_info)

# BELOW IS A connected to lower jina on I AM 16_HTML_TABLES/TEMPLATES/INDEX.HTML
    # lines 66 -91 
# @app.route('/lists')
# def render_lists():
#     # Soon enough, we'll get data from a database, but for now, we're hard coding data
#     student_info = [
#        {'name' : 'Michael', 'age' : 35},
#        {'name' : 'John', 'age' : 30 },
#        {'name' : 'Mark', 'age' : 25},
#        {'name' : 'KB', 'age' : 27}
#     ]
#     return render_template("index.html", random_numbers = [3,1,5], students = student_info)


if __name__=="__main__":
    app.run(debug=True)
