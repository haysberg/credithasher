from cchashlib import luhnAddition
from verify import verify

def checksum(incompleteNumber):
    """This function generates the last digit of an incomplete number containing the first 15 numbers of a credit card.

    Raises:
        RuntimeError: If we are unable to find any valid number, which should mathematically never happen, we throw an exception.

    Returns:
        integer -- This returns the now complete number, once the last digit has been found.
    """
    #We calculate what number we need to input to the credit card in order for the sum of all digits to be a multiple of 10.
    numberNeeded = 10 - (verify(incompleteNumber) % 10) % 10

    #We sometimes can find that the number needed is 10. When this is the case, we set the number needed to 0.
    if(numberNeeded == 10):
        numberNeeded = 0
    
    #We try numbers from 0 to 9, and compare their result when going through Luhn's Addition
    #with what we need to add to the current sum to get a multiple of 10
    for i in range(10):
            if (luhnAddition(i) == numberNeeded):
                incompleteNumber += str(luhnAddition(i))
                return incompleteNumber
    raise RuntimeError('There was an error during key calculation !')