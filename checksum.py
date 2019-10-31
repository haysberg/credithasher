from cchashlib import luhnAddition
from verify import verify

def checksum(incompleteNumber):
    numberNeeded = 10 - (verify(incompleteNumber) % 10) % 10
    if(numberNeeded == 10):
        numberNeeded = 0
    print('The checksum associated with the first 15 numbers is : ' + str(numberNeeded))
    for i in range(10):
            if (luhnAddition(i) == numberNeeded):
                incompleteNumber += str(luhnAddition(i))
                return incompleteNumber
    raise RuntimeError('There was an error during checksum calculation !')