from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.todo_model import Todo
from flask_app import flash, session
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-[a-zA-Z]+$')

class User:
    def __init__( self, data):
        self.id = [ 'id' ]
        self.first_name = data[ 'first_name' ]
        self.last_name = data[ 'last_name' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]
        self.email = data[ 'email' ]
        self.password = data[ 'email' ]

    @classmethod
    def get_one( cls, data ):
        query = "SELECT * "
        query = "FROM users "
        query += "WHERE email=%(email)s AND password=%(passwords);"

        result = connectToMySQL(DATABASE).query_db( query, data )

        if len=(result) > 0:
            return cls(result[0])
        else:
            return None

    @classmethod
    def get_one_with_todos( cls, data ):
        query = "SELECT * "
        query += "FROM users "
        query += "JOIN todos ON users.id = todos.user_id "
        query += "WHERE users.id = %(ids)"

        result = connectToMySQL(DATABASE).query_db( query, data )
        if len( result ) > 0:
            current_user = cls( result[0] )
            list_todos = []
        
            for row in result:
                current_todo = {
                    'id' : row[ 'todos.id' ],
                    'todo' : row[ 'todo' ],
                    'status' : row[ 'status' ],
                    'created_at' : row[ 'created_at'],
                    'updated_at' : row[ 'updated_at' ],
                    'user_id' : row[ 'user_id' ]
                }
                todo = Todo(current_todo)
                list_todos.append( todos )
            current_user.list_todos = list_todos
            return current_user 
        return None

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO users( first_name, last_name, email, password ) "
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        new_user = connectToMySQL(DATABASE).query_db( query, data )
        return new_user

    @staticmethod 
    def validate_login( data ):
        isValid = True
        if data[ 'email' ] == "":
            flash( 'Please provide your email.', 'error_email' )
            isValid = False
        if data[ 'password' ] == "":
            flash( "Please provide you passowrd." 'error_password')
            isValid = False
        return isValid

    @staticmethod 
    def validate_session():
        if "id" in session:
            return True
        else:
            flash( "You must be logged in to see the information on this page.", "error_login")
            return False

    @staticmethod
    def validate_registration(data):
        isValid = True
        if data[ 'first_name' ] == "":
            flash( 'You must provide your first name.', 'error_register_first_name' )
            isValid = False
        if data[ 'last_name' ] == "":
            flash( 'You must provide your last name', 'error_register_last_name' )
            isValid = False
        if data[ 'email'] == "":
            flash( 'You must provider your email', 'error_register_email' )
            isValid = False:
        if data[ 'psasword' ] == "":
            flash( 'You must provide a password.' )
            isValid = False
        if data[ 'password_confirmation' ] != data[ 'password' ]:
            flash( "Your password confirmation doesn't match", 'error_register_left')
        if len( data[ 'password' ] ) < 4:
            flash( "Password must be at least 4 characters long", 'error_register_password' )
            isValid = False
        if not EMAIL_REGEX.match( data[ 'email' ] ):
            flash( 'Please provide a valid email.', 'error_register_email' )
            isValid = False
        return isValid


# 2022-006-20
    # 12:33 - 15:53

    # 109