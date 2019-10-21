import sys

from vendor import checkVendor

#If there is not exactly 3 arguments, we stop the program.
if(len(sys.argv) != 3):
    sys.exit("Usage : python3 chash.py <mode> <card_number>")
else:
    print("You chose mode : ", sys.argv[1])
    print("The card number is : ", sys.argv[2])

mode = sys.argv[1]
number = sys.argv[2]

if len(number) != 16 :
    sys.exit("The credit card number you put is not 16 numbers long !")

if(mode == "vendor"):
    checkVendor(number)