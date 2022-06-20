
# 2022-06-29 8:21   use military time
# 
# from the package called flask, import the python library called Flask
                            # Flask is captialied because --
                            # Flask on line 8 is pink, but Flask on line 12 is not.  Why?
                                # --
                                # 
from flask import Flask

# the variable called flask is assigned th value of the function called flask
                    # Flask is capitalized because --
                    # Flask on line 13 is pink, but Flask on line 8 is not.  Why?
app = Flask(__name__)
    
    # app.secret_key is a variable.  it is also called a --
    # we are assigning the variable app.secret_key to the string "secret"

            # setting up the secret_key is important because it is need for -- to work

app.secret_key = "secret"

# the variavle called DATABASE is assigned the value of the string "todos_sceme"

    # DATABASE is in call caps because --
    # DATABASE is pink because --
DATABASE = "todos_sceme"