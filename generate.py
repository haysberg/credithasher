from cchashlib import stringToIntegerArray
from cchashlib import luhnAddition
from verify import verify
import random
import sys

def generate(inputString):
    """This function allows us to generate a valid credit card number from a string. It can take string from 1 to 15 characters long
    
    Arguments:
        inputString {string} -- The credit card partial number that we have. It is always placed at the start
    
    Returns:
        string -- The generated card number
    """
    print("============================")
    print("The given number is : " + inputString)
    print("The number length is : " + str(len(inputString)))
    
    generatedLength = 16 - (len(inputString))
    print("We're going to generate a number between 0 and " + str(10 ** generatedLength - 1))
    genString = str(random.randint(10 ** (generatedLength -1 ), (10 ** generatedLength) - 1))
    print("The generated following numbers are : " + genString)
    inputString += genString
    inputString = inputString[:15]
    
    print("We need to generate " + str(generatedLength) + " numbers")
    print("The pre-generated number is : " + str(inputString) + " it is long of : " + str(len(str(inputString))))
    print("The incomplete sum is : " + str(verify(inputString)))

    

    numberNeeded = 10 - (verify(inputString) % 10) % 10
    if(numberNeeded == 10):
        numberNeeded = 0
    print("The number needed is : " + str(numberNeeded))
    for i in range(10):
        if (luhnAddition(i) == numberNeeded):
            inputString += str(luhnAddition(i))
            #if len(inputString) == 16 :
            return inputString
    raise RuntimeError('There was an error during credit card number generation !')