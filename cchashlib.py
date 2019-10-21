import sys

def stringToIntArray(string):
    res = []
    for i in range(len(string)):
        res.append(ord(string[i]) - 48)
    return res

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