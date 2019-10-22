from cchashlib import stringToIntegerArray
from cchashlib import luhnAddition
from verify import verify
import random
import sys

def generate(inputString):
    generatedLength = 16 - (len(inputString))
    inputString += str(random.randint(0, 10 ** (generatedLength - 1) - 1))
    print("The pre-generated number is : " + str(inputString))
    print("The incomplete sum is : " + str(verify(inputString)))
    numberNeeded = 10 - (verify(inputString) % 10) % 10
    if(numberNeeded == 10):
        numberNeeded = 0
    print("The number needed is : " + str(numberNeeded))
    for i in range(10):
        if (luhnAddition(i) == numberNeeded):
            inputString += str(luhnAddition(i))
            return inputString
    sys.exit('Error during number generation !')