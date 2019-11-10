#fake unit testing

class unitTestReturn:
    unitTest = ""
    realReturnObject = ""
    
    def __init__(self):
        self.data = []
        
toList = list()
thingToAddToList = "this is an example"
toList.append("test")

def addToList(thing, theList):
    returnObject = unitTestReturn()
    returnObject.unitTest = False
    returnObject.realReturnObject = theList
    returnObject.realReturnObject.append(thing)
    if(len(returnObject.realReturnObject) == len(theList)):
        returnObject.unitTest = True
    return returnObject

newList = addToList(thingToAddToList, toList)

if(newList.unitTest):
    print("this tested correctly")
else:
    print("this tested incorrectly") 
    
    

