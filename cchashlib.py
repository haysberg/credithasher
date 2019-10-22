import sys

#This function is used to transform a string array (the one we get as an argument) into an integer array
def stringToIntegerArray(inputString):
    res = []
    #For each character in our input array, we get the character, transform it into an integer and remove 48, which is the offset of the numbers in the ASCII table.
    for i in range(len(inputString)) :
        res.append(ord(inputString[i]) - 48)
    return res

#This function is used to transform a string array (the one we get as an argument) into an integer array
def integerArrayToString(inputNumber):
    print(chr(inputNumber))
    return chr(inputNumber)

def checkNumberIntegrity(string):
    if len(string) != 16 :
        sys.exit("The credit card number you put is not 16 numbers long !")
    res = []
    for i in range(len(string)):
        if ord(string[i]) > 47 and ord(string[i]) < 58 :
            res.append(ord(string[i]) - 48)
        else:
            sys.exit("The credit card number you put is invalid !")
    return res


def luhnAddition(inputInt):
    """This function takes in an integer and doubles it. If the result is equal or greater than 10, it adds up the digits.
    
    Arguments:
        inputInt {[integer]} -- [This is the integer to be doubled by the function.]
    
    Returns:
        [integer] -- [Gives the transformed integer]
    """
    #If the number is greater than 4, doubling it will give a result equal or greater than 10 so we add the digits
    if(inputInt > 4):
        return 1 + (inputInt*2 % 10)
    #If it's not, we double it normally and send it back
    else:
        return inputInt * 2