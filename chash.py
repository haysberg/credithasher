#default libraries imports
import sys

#custom files imports
from vendor import checkVendor
from cchashlib import checkNumberIntegrity
from verify import verify
from generate import generate
from checksum import checksum

#If there is not exactly 3 arguments, we stop the program.
if(len(sys.argv) != 3):
    sys.exit("Usage : python3 chash.py <mode> \"<card_number>\"")
else:
    print("You chose mode : ", sys.argv[1])
    print("The card number is : ", sys.argv[2])

#We create variables as it is easier to read the code. I chose to create those to avoid confusion, but really, they are not that useful.
mode = sys.argv[1]
number = sys.argv[2]

if not number.isdigit():
    raise Exception('Your number should only contain digits !')

#We check what mode the user wants to use
if(mode == "vendor"):
    checkVendor(number)

elif(mode == "verify"):
    #We check the integrity of the input beforehand.
    checkNumberIntegrity(number)

    #If, after adding all the numbers together including the checksum, it is a multiple of 10, it means the credit card number is valid
    if verify(number) % 10 == 0:
        print("The card number is valid !")
    else :
        print("The card number is NOT valid, please check your input !")
        
elif(mode == "generate"):
    print('We generated the following number : ' + generate(number))

elif(mode == "checksum"):
    #If we have the first 15 digits of the number, we calculate the last digit.
    if len(number) == 15:
        print(checksum(number))
    #If we do not, we exit the program as we need the first numbers.
    else:
        sys.exit("To calculate the checksum, we need the first 15 digits. If you have less, then use the generate option.")

#If the user doesn't input a valid mode, we exit the program and throw an exception.
else:
    raise Exception('Please input a valid mode.')