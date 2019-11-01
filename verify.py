from cchashlib import stringToIntegerArray
from cchashlib import luhnAddition

def verify(ccNumber):
    """This function adds up all the digits in a credit card number using Luhn's Addition on one digit out of two.
    
    Arguments:
        ccNumber {string} -- The card number that we want to crunch into a sum.
    
    Returns:
        [integer] -- Sum of the numbers in the credit card. If all 16 digits are entered, it should given a multiple of 10 if the credit card number works.
    """
    #We convert the string that we got in parameter in an array of numbers.
    intArray = stringToIntegerArray(ccNumber)

    #We initiate the result variable.
    res = 0

    #We iterate on the number array that we got in input.
    for i in range(len(intArray)):

        #If the number is even (knowing that we start counting from the left side of the card number, not the right)
        #We double it and add its digits if needed using luhnAddition
        if(i % 2 == 0):
            res += luhnAddition(intArray[i])

        #If it's not needed, we just let the number like it is and add it to the result.
        else:
            res += intArray[i]

    #We return the result
    return res
    