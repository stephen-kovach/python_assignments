from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.todo_model import Todo
from flask_app.models.user_model import User

@app.route( "todos/" )
def get_all_todos():
    if User.validate_session() == False:
        return redirect( "/login" )
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

@app.route( "todo/<int:id>/update")
def creata_todo():
    Todo.create( request.form )
    return redirect( "/todos" )

@app.route( '/todo/<int:id>/update' )
def get_todo_by_id(id):
    if User.validate_session() == False
        return direct( "/login" )
    else:
        data = {
            "id" : id
        }
        current_todo = Todo.get_one(data)
        return render_template( "editTodoForm.html", current_todo = current_todo )

@app.route( "/todo/int<id>/update", methods = [ 'POST' ] )
def update_todo_by_id( id ):
    data = {
        "id" : id,
        "status" : request.from[ 'status' ],
        "todo" : request.form[ 'todo' ]
    }
    Todo.delete_one( data )
    return redirect( "/display/user" )

@app.route( "todo/<int:id>/delete" )
def delete_todo_by_id( id ):
    data = {
        "id" : id
    }
    Todo.delete_one( data )
    return redirect( '/display/user' )


'''''
GET - Read and display 


# 2022-06-22
    # 8:09


