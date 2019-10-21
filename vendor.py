import requests
import json
import io

from cchashlib import stringToIntArray

def checkVendor(ccNumber):
    return stringToIntArray(ccNumber)


def parseVendorCSV():
    return 0

def getVendorAPI(ccNumber):
    #print("https://lookup.binlist.net/" + ccNumber[:8])
    return json.dumps(requests.get(url = "https://lookup.binlist.net/" + ccNumber[:8]).json())