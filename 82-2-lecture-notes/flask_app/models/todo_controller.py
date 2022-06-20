
# 2022-60-19    19:50

# the server.py file we created for session 
    # would be an example of a controller 

from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.todo_model import Todo
from flask_app.models.user_model import User 

@app.route( "/todos" )
def get_all_todos():
    if User.validate_session() == False:
        return redirect ( "/login" )
    else:
        if "num_of_visits" in session:
            session[ "num_of_visits" ] += 1
        else:
            session[ "num_of_visits" ] = 1

        list_of_todos = Todo.get_all()
        return render_template( "index.html", list_of_todos = list_of_todos )

@app.route( "todo/new" )
def display_create_todo():
    return render_template( "todoForm.html" )

@app.route( "/todo/new", methods = [ 'POST' ] )
    def create_todo():
        Todo.create( request.form )
        return redirect( "/todos" )

app.route( "/todo/<int:id>/update" )
def get_todo_by_id(id):
    # the reason we are defining a parameter us because
                # -- (is it similar to self?)
    if User.validate_session() == False:
        return redirect ( "/login" )
    else:
        data = {
            "id" : id
        }
        current_todo = Todo.get_one(data)
        return render_template( "editTodoForm.html", current_todo = current_todo )

app.route( "/todo/<int:id>/upadate", methods = [ 'POST' ] )
def update_to_do_by_id():
    data = {
        "id" : id,
        "status" : request.form[ 'status' ]
        "todo" : request.form[ 'todo' ]
    }
    Todo.update_one(data)
    return redirect ( "/display/user" )

@app.route( "/todo/<int:id>/delete" )
def delete_todo_do(id):
    data = {
        "id" : id
    }
    Todo.delete_one(data)
    return redirect ( "/display/user" )