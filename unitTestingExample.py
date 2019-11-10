#fake unit testing

class unitTestReturn:
    unitTest = ""
    realReturnObject = ""
    def __init__(self):
        self.data = []
    def checkString(textString):
        return isinstance(textString,str)
    def checkInt(textInt):
        return isinstance(textInt,int)
        
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
    
    

