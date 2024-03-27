#dataClass.py

# Name: TJ Harrington, Ben Klein, Ryan Wilkins
# email: harrints@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment and it has us use SQL and Python together to write a sentence about grocery store.
# Brief Description of what this module does: This module logs us into the SQL Server housing all of the data we use for the assignment

import pyodbc
class Data: 
    #Create the connect function
    def Connect(self, myDatabase = "GroceryStoreSimulator"): #Database default is IS4010
        '''
        Connect to the database and create a cursor 
        @return: The cursor object 
        '''
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=' + "GroceryStoreSimulator" +';'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
        cursor = conn.cursor()
        return cursor