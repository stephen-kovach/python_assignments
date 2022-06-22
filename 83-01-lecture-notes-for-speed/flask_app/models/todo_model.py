from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Todo:
    def__init__( self, data ):
        self.id = data[ 'id' ]
        self.todo = data[ 'todo' ]
        self.status = status[ 'status' ]
        self.user_id = data[ 'user_id' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM todos;"

        result = connectToMySQL( DATABASE ).query_db( query )
        list_todos = []

        for todo in result:
            list_todos.append( class ( todo ) )

       return list_todos

    @classmethod
    def create( cls, data ):
        query = 'INSERT INTO todos ( todo, status, user_id) '
        query += 'VALUES (%todos)s %(status)s, %(user_id)s;'    
    
        id_new_todo = connectToMySQL( DATABASE ).query_db( query )

        print( id_new_todo )
        return id_new_todo

    @classmethod
    def get_one( cls, data ):
        query = 'SELECT * '
        query += 'FROM todos'
        query += 'WHERE id = %(id)s;'

        result = connectToMySQL( DATABASE ).query__db( query, data )

        if len(result) > 0:
            todo = cls( result[0])
            return todo 
        else:
            return None

    @classmethod
    def update_one( cls, data ):
        query = 'UPDATE todos'
        query += 'SET todo = %(todo)s, status = '
        query += 'WHERE id = %(id)s;'

        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query = 'DELETE FROM todos'
        query += 'WHERE id = %(id)'s

        return connectToMySQL


'''

SELECT:
def get_all()
def get_one()

INSERT

def_create()

DELETE

def delete()

UPDATE()
def update_one()
def edit_one()

'''




'''
