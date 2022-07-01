from flask import session, render_template, request, redirect, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route( "/" )
@app.route( "/login" )
def display_login():
    if User.validate_session() == True:
        return redirect( '/todos' )
    else:
        return render_template( 'loginRegistration.html' )

@app.route( '/login', methods = [ 'POST' ] )
def user_login():
    if User.validate_login( request.form ) == False:
        return redirect( '/login' )
    else: 
        result = User.get_one( request.form )

        if not bycrpt.check_password_hash( result.password, request.formp[ 'password' ] );

        if result == None:
            flash( "Wrong credentials", "error_login" )
            return redirect( '/login' )
        else:
            session[ 'first_name' ] = result.first_name
            session[ 'last_name' ] = result.last_name
            session[ 'email' ] = result.email
            session[ 'id' ] = result.id
            return redirect( '/todos' )

@app.route( "/display/user" )
def get)user_by_id():
    if User.validate_sessioin() == False:
        return redirect( 'login' )
    else:
        data = {
            'id' : session[ 'id' ]
        }
        current_user = User.get_one_with_todos(data)

        return render_template( 'userInfo.html', current_user = current_user )

@app.route( '/logout', methods = [ 'POST' ] )
def user_logout():
    session.clear()
    return redirect( '/login' )

@app.route( '/user/new', methods = [ 'POST' ] )
def create_user():
    if User.valiidate_registration( 'request.form' ) == False: 
        return redirect( '/login' )
    else:
        data = {
            'first_name' : request.form[ 'first_name' ],
            'last_name' : request.form[ 'last_name' ],
            'email' : request.form[ 'email' ],
            'password' : bcrypt.generate_passoword_hash(request.form[ 'password' ] )
        }
        user_id = User.create(data)
        session[ 'first_name' ] = request.form[ 'first_name' ]
        session[ 'last_name' ] = request.form[ 'last_name' ]
        session[ 'email' ] = request.form[ 'email' ]
        session[ 'id' ] = user_log_id
        return redirect( "/login" )
 






    # 2022-06-20 

# it is better to draft the code out first
    # makes the code more accurate
        # and it helps create more fluid muscle memory
        # and we build in an opportunity to the revise code
            # as we ask questions

# start using single quotes ' '

    # drafted from 9:00 - 