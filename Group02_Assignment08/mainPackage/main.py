#main.py
import string

# Name: TJ Harrington, Ben Klein, Ryan Wilkins
# email: harrints@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/28/24
# Course/Section: IS 4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This is a group assignment and it has us use SQL and Python together to write a sentence about grocery store.
# Brief Description of what this module does: This module is the main module and it is where we run all of our code. This fetches the data from the Grocery Store simulator and prints our findings into 1 sentence
if __name__ == "__main__":
    from dataClassPackage.dataClass import Data
    
    #Instantiate an object of type Data
    myData = Data()
    #Invoke the connect method and store what it returns in another variable 
    myCursor = myData.Connect("GroceryStoreSimulator")   
    
    #Provide the Cursor with SQL query 
    myCursor.execute(
        '''
        SELECT TOP 5 tName.NameID, tName.Name, tProduct.ProductID, tTransactionDetail.QtyOfProduct 
        FROM tName 
        INNER JOIN tProduct ON tName.NameID = tProduct.NameID 
        INNER JOIN tTransactionDetail ON tProduct.ProductID = tTransactionDetail.ProductID 
        ORDER BY tTransactionDetail.QtyOfProduct DESC
    '''
    )

    #Create a list to store cursor values 
    itemList = []
    #Create a loop to get the values
    for row in myCursor:
        itemList.append(row[1])


    #Assign the item strings the list values
    item0 = itemList[0]
    item1 = itemList[1]
    item2 = itemList[2]
    item3 = itemList[3]
    item4 = itemList[4]
    #Print end result
    print ("The Top 5 Items sold are", item0+",", item1+",",item2+",",item3,"&",item4+".")
    

    