import sys

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
    checkNumberIntegrity(number)
    if verify(number) % 10 == 0:
        print("The card number is valid !")
    else :
        print("The card number is NOT valid, please check your input !")
        
elif(mode == "generate"):
    print('We generated the following number : ' + generate(number))

elif(mode == "checksum"):
    if len(number) == 15:
        print(checksum(number))
    else:
        sys.exit("To calculate the checksum, we need the first 15 digits. If you have less, then use the generate option.")

else:
    raise Exception('Please input a valid mode.')