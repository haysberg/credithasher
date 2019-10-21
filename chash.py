import sys

from vendor import checkVendor
from cchashlib import checkNumberIntegrity
from vendor import parseVendorCSV
from vendor import getVendorAPI

#If there is not exactly 3 arguments, we stop the program.
if(len(sys.argv) != 3):
    sys.exit("Usage : python3 chash.py <mode> <card_number>")
else:
    print("You chose mode : ", sys.argv[1])
    print("The card number is : ", sys.argv[2])

mode = sys.argv[1]
number = sys.argv[2]

checkNumberIntegrity(number)

vendors = []
parseVendorCSV()

if(mode == "vendor"):
    checkVendor(number)
    print(getVendorAPI(number))