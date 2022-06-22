from flask import Flask
from flask_app import app 
from flask_app.controllers import todo_controller, user_controller


# http://127.0.0.1:5000

if __name__== "__main__":
    app.run( dubug = True )

    # 2022-06-21 18:22
    