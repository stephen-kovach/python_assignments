
# 2022-06-29 8:21   use military time 
            # 

            #  14:40 - 16:40
            #  19:10 - 19:21    

# this file is called 
# 
# 82-2-lecture-notes/flask_app/config/mysqlconnection.py

    # t/f the code above displays how the file is modularized
    # t/f the way the file is structred is how it is modulariized
    # t/f the file is structured/modularized/both? correctly -

import pymysql.cursors

    # a concise definition of pymysql.cursors would be 

            # --

        # the reason pymysql.cursors is faded red at 8:48 is because 
                    # we haven't -- yet

# we are defining a class called MySQLConnection 
            # MySQLConnection is red because it is a --
            # MySQLConnection must be capitalized because it is a class

            # a concise way to summarize "definig a class" would be

                # --

class MySQLConncection:
# we are defining a function called __init__
        # t/f __init__ is also called a constructor functions
        # we are defining two parameters
            # the parameters are called self and db

            #  a concise definition of self would be

                # -
            
            # db refers to  -
                # is faded at 8:59 because we haven't -- yet

    def __init__(self, db):

        # 2022-06-19-9:08, i don't understand any of this--comeback to it --

        # the purpose of the code block below is to 
            # change the user and password as needed
            # t/f  the code below is a method
            # the purpose of the code below is to --  
        connection = pysql.connect( host = 'localhost',
                                    user = 'root',
                                    password = 'root',
                                    db= db, # db on the right is not a string because --
                                    charset = 'utf8mb4', # the string on the right means
                                                                # --  
                                    cursorclass = pymysql.cursors.DictCursor, 
                                        # pymysql.cursors.DictCursor 
                                            # is a --
                                        # the purpose of pymysql.cursors.DictCursor
                                            # is to --

                                    autocommit = True )
                                        # autocommit is a function
                                            # it means --
                                            
                                # t/f the code above is an object and a dictionary 
                                # t/f the code block above is -lined up?- correctly
                                # t/f the syntax in the code block above is correct
                                # t/f 

    # t/f the code snippet below (way below) is us defining a second function in the --class?--
        # a consice summary of what defining a class would be:

            # --

        # we the reason we define classes is because
            
            # --
    
        # we are defining 3 parameters:

            # self which means --
            # query which means --
            # data which means --

    # this is the 2nd function defined in/by the class 
                    # a "class" is a --
    def query_bd( self, query, data = None ):

            # the reason the -variable?- called data is assigned the -value?- of None
                    # is because --
                # the reason that is important to know 
                    # is because --
                # the reason the parameter called data is faded pink at 9:16 
                    # is because --
                # the reason None is capitalized 
                    # is because --

        # i do not understand the code below
        # the code below connects to mysql workbench
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify( query, data )
                print( "Running Query:", query )

                cursor.execute( query, data )
                if query.lower().find( "insert" ) >= 0:
                # a conditional statemnet 
                    # it says --

                    # JJC INSERT queries will return the ID NUMBER of the row inserted
                    # t/f the code below is spaced properly
                    self.connection.commit()

                    # we are returning --
                    return cursor.lastrowid
                elif query.lower().find( "select" ) >= 0:
                    # SELECT queries will return the data from the database a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:  
                    # JJC UPDATE and DELETE queries will return nothing
                    self.connection.commit()
                
                # i don't understand the code below
                    # 
                except Exception as e:
                    # JJC if the query fails the method FALSE
                    print ( "Something went wrong", e )
                    return False 
                
                finally:
                    # JJC close the connection

                    self.connection.close()
                    # the syntax for the code snippet above 
                            # is --

# JJC connecToMySQL receieves the databse we're uses it to create an instance of MySQLConnection

def connectToMySQL( db ):
    return MySQLConncection( db )

    # t/f the code block above is --intented?-- correctly


