import requests
import json

from cchashlib import stringToIntArray

def checkVendor(ccNumber):
    infos = json.loads(getVendorAPI(ccNumber))
    print("The vendor of the card is " + infos["scheme"])
    print("This card has been issued in : " + infos["country"]["alpha2"])
    print("This card is a " + infos["brand"] + " card")

def getVendorAPI(ccNumber):
    request = requests.get(url = "https://lookup.binlist.net/" + ccNumber[:8])
    return json.dumps(request.json())