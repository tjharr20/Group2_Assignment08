#Main.py
if __name__ == "__main__":
    from dataClassPackage.dataClass import Data
    
    #Instantiate an object of type Data
    myData = Data()
    #Invoke the connect method and store what it returns in another variable 
    myCursor = myData.Connect("GroceryStoreSimulator")   
    
    
    myCursor.execute(
        '''
        SELECT TOP 10 tName.NameID, tName.Name, tProduct.ProductID, tTransactionDetail.QtyOfProduct 
        FROM tName 
        INNER JOIN tProduct ON tName.NameID = tProduct.NameID 
        INNER JOIN tTransactionDetail ON tProduct.ProductID = tTransactionDetail.ProductID 
        ORDER BY tTransactionDetail.QtyOfProduct DESC
    '''
    )
    print ("The Top 10 Items sold are...")
    for row in myCursor:
        print (row[1]); # Second column
        