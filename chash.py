import sys

from vendor import checkVendor
from cchashlib import checkNumberIntegrity
from verify import verify
from generate import generate
from checksum import checksum

#If there is not exactly 3 arguments, we stop the program.
if(len(sys.argv) != 3):
    sys.exit("Usage : python3 chash.py <mode> <card_number>")
else:
    print("You chose mode : ", sys.argv[1])
    print("The card number is : ", sys.argv[2])

mode = sys.argv[1]
number = sys.argv[2]

if(mode == "vendor"):
    checkVendor(number)
    checkNumberIntegrity(number)


elif(mode == "verify"):
    checkNumberIntegrity(number)
    if verify(number) % 10 == 0:
        print("The card number is valid !")
    else :
        print("The card number is NOT valid, please check your input !")

        
elif(mode == "generate"):
    if number.isdigit():
        print('We generated the following number : ' + generate(number))
    else:
        sys.exit("Your card number should only contain digits !")

elif(mode == "checksum"):
    if len(number) == 15:
        if number.isdigit():
            print(checksum(number))
        else:
            sys.exit("Your card number should only contain digits !")
    else:
        sys.exit("To calculate the checksum, we need the first 15 digits. If you have less, then use the generate option.")