from cchashlib import stringToIntegerArray
from verify import verify
from checksum import checksum
import random
import sys

def generate(inputString):
    """This function allows us to generate a valid credit card number from a string. It can take strings from 1 to 15 characters long
    
    Arguments:
        inputString {string} -- The credit card partial number that we have. It is always placed at the start
    
    Returns:
        string -- The generated card number
    """
    print("============================")
    
    #We calculate how many numbers we need to generate in order to have 15 numbers in total.
    generatedLength = 15 - (len(inputString))

    #If we need numbers, we go through this loop. If we already have 15 characters in input, we don't.
    if generatedLength > 0:
        genString = str(random.randint(10 ** (generatedLength -1 ), (10 ** generatedLength) - 1))
        print("Generated the following numbers to append to the input : " + genString)
        inputString += genString
    
    #Printing variables...
    print("We need to generate " + str(generatedLength) + " numbers")
    print("The first 15 numbers are : " + str(inputString))
    print("The incomplete sum is : " + str(verify(inputString)))

    #We return the result of the checksum function with the numbers that we already generated, in order to add the last digit as the key.
    return checksum(inputString)