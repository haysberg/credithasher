#This function is used to transform a string array (the one we get as an argument) into an integer array
def stringToIntegerArray(inputString):
    res = []
    #For each character in our input array, we get the character, transform it into an integer and remove 48, which is the offset of the numbers in the ASCII table.
    for i in range(len(inputString)) :
        res.append(ord(inputString[i]) - 48)
    return res

def luhnAddition(inputInt):
    if(inputInt > 4):
        return 1 + (inputInt*2 % 10)
    else:
        return inputInt * 2

def verify(ccNumber):
    intArray = stringToIntegerArray(ccNumber)
    res = 0
    for i in range(len(intArray)):
        if(i % 2 == 0):
            res += luhnAddition(intArray[i])
        else:
            res += intArray[i]
    return res % 10 == 0
    