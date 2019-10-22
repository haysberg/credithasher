from cchashlib import stringToIntegerArray
from cchashlib import luhnAddition

def verify(ccNumber):
    intArray = stringToIntegerArray(ccNumber)
    res = 0
    for i in range(len(intArray)):
        if(i % 2 == 0):
            res += luhnAddition(intArray[i])
        else:
            res += intArray[i]
    return res
    